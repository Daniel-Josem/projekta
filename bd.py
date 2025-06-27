import bcrypt
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

Base = declarative_base()

# ------------------ MODELOS ------------------

class Usuario(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre_usuario = Column(String(50), nullable=False, unique=True)
    contraseña = Column(String(100), nullable=False)
    rol = Column(String(20), nullable=False, default='usuario')  # 'usuario' o 'administrador'
    correo_electronico = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Usuario(nombre_usuario='{self.nombre_usuario}', correo='{self.correo_electronico}', rol='{self.rol}')>"


class Proyecto(Base):
    __tablename__ = 'proyectos'

    id_proyecto = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date)
    usuario_id = Column(Integer, ForeignKey('usuarios.id_usuario'))

    usuario = relationship('Usuario', backref='proyectos')

    def __repr__(self):
        return f"<Proyecto(nombre='{self.nombre}')>"


class Tarea(Base):
    __tablename__ = 'tareas'

    id_tarea = Column(Integer, primary_key=True, autoincrement=True)
    id_proyecto = Column(Integer, ForeignKey('proyectos.id_proyecto'), nullable=False)
    descripcion = Column(String(255), nullable=False)
    fecha_vencimiento = Column(Date)
    id_usuario_asignado = Column(Integer, ForeignKey('usuarios.id_usuario'))
    estado = Column(String(20), nullable=False, default='pendiente')  # 'pendiente', 'en progreso', 'completada'
    prioridad = Column(String(10), nullable=False, default='media')  # 'baja', 'media', 'alta'

    def __repr__(self):
        return f"<Tarea(descripcion='{self.descripcion}', estado='{self.estado}', prioridad='{self.prioridad}')>"


class MiembroProyecto(Base):
    __tablename__ = 'miembros_proyecto'

    id_proyecto = Column(Integer, ForeignKey('proyectos.id_proyecto'), primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'), primary_key=True)
    rol = Column(String(20), nullable=False, default='colaborador')  # puede ser 'colaborador', 'responsable', etc.

    def __repr__(self):
        return f"<MiembroProyecto(id_proyecto={self.id_proyecto}, id_usuario={self.id_usuario}, rol='{self.rol}')>"


# ------------------ CONFIGURACIÓN BD ------------------

DB_HOST = 'localhost'
DB_NAME = 'gestion_proyectos_db'
DB_USER = 'root'
DB_PASSWORD = ''

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------ FUNCIONES ------------------

def verificar_contraseña(usuario, contraseña_ingresada):
    return bcrypt.checkpw(contraseña_ingresada.encode('utf-8'), usuario.contraseña.encode('utf-8'))


def crear_usuario(db, nombre_usuario, contraseña, rol, correo_electronico):
    try:
        # Validar si ya existe
        if db.query(Usuario).filter(Usuario.nombre_usuario == nombre_usuario).first():
            print("Usuario ya existe.")
            return None

        hashed_password = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())

        nuevo_usuario = Usuario(
            nombre_usuario=nombre_usuario,
            contraseña=hashed_password.decode('utf-8'),
            rol=rol,
            correo_electronico=correo_electronico
        )
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
        return nuevo_usuario
    except SQLAlchemyError as e:
        db.rollback()
        print("Error al crear usuario:", e)
        return None


def login_usuario(db, nombre_usuario, contraseña_ingresada):
    try:
        usuario = db.query(Usuario).filter(Usuario.nombre_usuario == nombre_usuario).first()
        if usuario and verificar_contraseña(usuario, contraseña_ingresada):
            print("Inicio de sesión exitoso")
            return usuario
        else:
            print("Nombre de usuario o contraseña incorrectos")
            return None
    except SQLAlchemyError as e:
        print("Error en login:", e)
        return None


# ------------------ PRUEBA DE INSERCIÓN ------------------

def prueba_insercion():
    db = SessionLocal()
    try:
        # Crear usuario
        nuevo_usuario = crear_usuario(db, "juan.perez", "miclave123", "administrador", "juan.perez@ejemplo.com")
        if not nuevo_usuario:
            print("No se pudo crear el usuario. ¿Ya existe?")
            return

        print(f"Usuario creado: {nuevo_usuario}")

        # Crear proyecto
        fecha_inicio = datetime.strptime("2025-04-15", "%Y-%m-%d").date()
        fecha_fin = datetime.strptime("2025-05-30", "%Y-%m-%d").date()
        nuevo_proyecto = Proyecto(
            nombre="Desarrollo Web",
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            usuario_id=nuevo_usuario.id_usuario
        )
        db.add(nuevo_proyecto)
        db.commit()
        db.refresh(nuevo_proyecto)
        print("Proyecto creado:", nuevo_proyecto)

        # Crear tarea
        fecha_vencimiento = datetime.strptime("2025-04-22", "%Y-%m-%d").date()
        nueva_tarea = Tarea(
            id_proyecto=nuevo_proyecto.id_proyecto,
            descripcion="Implementar la página de inicio",
            fecha_vencimiento=fecha_vencimiento,
            id_usuario_asignado=nuevo_usuario.id_usuario,
            estado="pendiente",
            prioridad="alta"
        )
        db.add(nueva_tarea)
        db.commit()
        db.refresh(nueva_tarea)
        print("Tarea creada:", nueva_tarea)

        # Asignar miembro
        nuevo_miembro = MiembroProyecto(
            id_proyecto=nuevo_proyecto.id_proyecto,
            id_usuario=nuevo_usuario.id_usuario,
            rol="desarrollador"
        )
        db.add(nuevo_miembro)
        db.commit()
        print("Miembro asignado al proyecto:", nuevo_miembro)

    except SQLAlchemyError as e:
        db.rollback()
        print("Error durante inserción de prueba:", e)
    finally:
        db.close()


# ------------------ EJECUCIÓN PRINCIPAL ------------------

if __name__ == "__main__":
    prueba_insercion()

    db = SessionLocal()
    usuario_logeado = login_usuario(db, "juan.perez", "miclave123")
    if usuario_logeado:
        print(f"Bienvenido {usuario_logeado.nombre_usuario}")
    db.close()
