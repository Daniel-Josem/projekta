from sqlalchemy.orm import Session
from bd import Proyecto, Tarea, SessionLocal

# Función para obtener proyectos y tareas
def obtener_proyectos_y_tareas(usuario_id):
    db = SessionLocal()
    try:
        # Obtiene proyectos asociados al usuario
        proyectos = db.query(Proyecto).filter(Proyecto.usuario_id == usuario_id).all()
        # Obtiene tareas asociadas al usuario
        tareas = db.query(Tarea).filter(Tarea.id_usuario_asignado == usuario_id).all()
        return proyectos, tareas
    except Exception as e:
        print(f"Error al obtener proyectos y tareas: {e}")
        return [], []
    finally:
        db.close()
from bd import Proyecto, Tarea, SessionLocal
from datetime import datetime


# Función para crear un nuevo proyecto
def crear_proyecto(nombre, fecha_inicio, fecha_fin=None):
    db = SessionLocal()
    try:
        fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        if fecha_fin:
            fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
        nuevo_proyecto = Proyecto(nombre=nombre, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
        db.add(nuevo_proyecto)
        db.commit()
        db.refresh(nuevo_proyecto)
        return nuevo_proyecto
    except Exception as e:
        print(f"Error al crear proyecto: {e}")
        return None
    finally:
        db.close()

# Función para crear una nueva tarea
def crear_tarea(id_proyecto, descripcion, fecha_vencimiento, estado="pendiente", prioridad="media"):
    db = SessionLocal()
    try:
        fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
        nueva_tarea = Tarea(id_proyecto=id_proyecto, descripcion=descripcion, fecha_vencimiento=fecha_vencimiento, estado=estado, prioridad=prioridad)
        db.add(nueva_tarea)
        db.commit()
        db.refresh(nueva_tarea)
        return nueva_tarea
    except Exception as e:
        print(f"Error al crear tarea: {e}")
        return None
    finally:
        db.close()

# Función para obtener proyectos y tareas asignadas a un usuario
def obtener_proyectos_y_tareas(usuario_id):
    db = SessionLocal()
    try:
        proyectos = db.query(Proyecto).all()
        tareas = db.query(Tarea).filter(Tarea.id_usuario_asignado == usuario_id).all()
        return proyectos, tareas
    except Exception as e:
        print(f"Error al obtener proyectos y tareas: {e}")
        return [], []
    finally:
        db.close()