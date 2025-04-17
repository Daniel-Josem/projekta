from tkinter import messagebox
import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from bd import Usuario  # Asegúrate de que 'bd.py' tenga el modelo Usuario correctamente definido

# --- Configuración de la base de datos ---
DB_HOST = 'localhost'
DB_NAME = 'gestion_proyectos_db'
DB_USER = 'root'
DB_PASSWORD = ''

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Motor y sesión
engine = create_engine(DATABASE_URL, echo=False)  # Cambia a 'echo=True' para ver las consultas SQL (útil para depurar)
SessionLocal = sessionmaker(bind=engine)

# --- Función para verificar el inicio de sesión ---
def verificar_login(username, password):
    db = SessionLocal()
    try:
        # Verificar si el usuario existe
        usuario = db.query(Usuario).filter(Usuario.nombre_usuario == username).first()
        if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario.contraseña.encode('utf-8')):
            return usuario
        return None
    except SQLAlchemyError as e:
        messagebox.showerror("Error de Base de Datos", f"Hubo un problema al verificar el inicio de sesión:\n{e}")
        return None
    finally:
        db.close()

# --- Función para crear un nuevo usuario ---
def crear_usuario(username, password, rol, correo_electronico, creador_admin=False):
    db = SessionLocal()
    try:
        # Validar si el nombre de usuario ya existe
        if db.query(Usuario).filter(Usuario.nombre_usuario == username).first():
            return "El nombre de usuario ya está en uso."

        # Validar permisos para crear administradores
        if rol == "administrador" and not creador_admin:
            return "No tienes permiso para crear un usuario administrador."

        # Encriptar la contraseña
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Crear nuevo usuario
        new_user = Usuario(
            nombre_usuario=username,
            contraseña=hashed_password.decode('utf-8'),  # Decodificar antes de guardar en la base de datos
            rol=rol,
            correo_electronico=correo_electronico
        )

        db.add(new_user)  # Agregar el nuevo usuario a la sesión
        db.commit()  # Confirmar cambios en la base de datos
        return "¡Usuario creado exitosamente!"
    except SQLAlchemyError as e:
        db.rollback()  # Si hay un error, revertir los cambios
        messagebox.showerror("Error de Base de Datos", f"Hubo un problema al crear el usuario en la base de datos:\n{e}")
        return f"Error al crear usuario: {e}"
    finally:
        db.close()

# --- Función para cambiar la contraseña de un usuario ---
def cambiar_contraseña(username, new_password):
    db = SessionLocal()
    try:
        # Buscar al usuario en la base de datos
        usuario = db.query(Usuario).filter(Usuario.nombre_usuario == username).first()
        if usuario:
            # Encriptar la nueva contraseña
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            usuario.contraseña = hashed_password.decode('utf-8')  # Guardar la contraseña encriptada
            db.commit()  # Confirmar cambios en la base de datos
            return "¡Contraseña actualizada exitosamente!"
        else:
            return "Usuario no encontrado."
    except SQLAlchemyError as e:
        db.rollback()  # Revertir cambios en caso de error
        messagebox.showerror("Error de Base de Datos", f"Hubo un problema al actualizar la contraseña en la base de datos:\n{e}")
        return f"Error al cambiar contraseña: {e}"
    finally:
        db.close()
