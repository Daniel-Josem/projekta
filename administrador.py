import tkinter as tk
from tkinter import ttk, messagebox
from backadmin import obtener_proyectos_y_tareas, crear_proyecto, crear_tarea
from bd import Usuario, SessionLocal
import bcrypt

# Colores
COLOR_FONDO = "#4d7841"
COLOR_VERDE = "#15400e"
COLOR_GRIS_CLARO = "#bdc3c7"
COLOR_GRIS_OSCURO = "#2c3e50"
COLOR_TEXTO = "#ffffff"

# Crear un nuevo proyecto
def crear_proyecto_window(usuario):
    def guardar_proyecto():
        nombre = entry_nombre.get()
        fecha_inicio = entry_fecha_inicio.get()
        fecha_fin = entry_fecha_fin.get()

        if nombre and fecha_inicio:
            proyecto = crear_proyecto(nombre, fecha_inicio, fecha_fin)
            if proyecto:
                messagebox.showinfo("Éxito", "¡Proyecto creado exitosamente!")
                create_window.destroy()
                cargar_datos(usuario)
            else:
                messagebox.showerror("Error", "Hubo un problema al crear el proyecto.")
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    create_window = tk.Toplevel(root)
    create_window.title("Crear Proyecto")

    tk.Label(create_window, text="Nombre del Proyecto:").pack(pady=5)
    entry_nombre = tk.Entry(create_window)
    entry_nombre.pack(pady=5)

    tk.Label(create_window, text="Fecha de Inicio (YYYY-MM-DD):").pack(pady=5)
    entry_fecha_inicio = tk.Entry(create_window)
    entry_fecha_inicio.pack(pady=5)

    tk.Label(create_window, text="Fecha de Fin:").pack(pady=5)
    entry_fecha_fin = tk.Entry(create_window)
    entry_fecha_fin.pack(pady=5)

    tk.Button(create_window, text="Guardar Proyecto", command=guardar_proyecto).pack(pady=10)

# Crear una nueva tarea
def crear_tarea_window(usuario):
    def guardar_tarea():
        descripcion = entry_descripcion.get()
        fecha_vencimiento = entry_fecha_vencimiento.get()

        if descripcion and fecha_vencimiento:
            tarea = crear_tarea(
                id_proyecto=None,
                descripcion=descripcion,
                fecha_vencimiento=fecha_vencimiento,
                id_usuario_asignado=usuario.id_usuario
            )
            if tarea:
                messagebox.showinfo("Éxito", "¡Tarea creada exitosamente!")
                create_window.destroy()
                cargar_datos(usuario)
            else:
                messagebox.showerror("Error", "Hubo un problema al crear la tarea.")
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    create_window = tk.Toplevel(root)
    create_window.title("Crear Tarea")

    tk.Label(create_window, text="Descripción de la Tarea:").pack(pady=5)
    entry_descripcion = tk.Entry(create_window)
    entry_descripcion.pack(pady=5)

    tk.Label(create_window, text="Fecha de Vencimiento (YYYY-MM-DD):").pack(pady=5)
    entry_fecha_vencimiento = tk.Entry(create_window)
    entry_fecha_vencimiento.pack(pady=5)

    tk.Button(create_window, text="Guardar Tarea", command=guardar_tarea).pack(pady=10)

# Función para cargar datos
def cargar_datos(usuario):
    proyectos, tareas = obtener_proyectos_y_tareas(usuario.id_usuario)
    for item in tree_proyectos.get_children():
        tree_proyectos.delete(item)
    for item in tree_tareas.get_children():
        tree_tareas.delete(item)
    for proyecto in proyectos:
        tree_proyectos.insert("", "end", values=(proyecto.id_proyecto, proyecto.nombre, proyecto.fecha_inicio, proyecto.fecha_fin))
    for tarea in tareas:
        tree_tareas.insert("", "end", values=(tarea.id_tarea, tarea.descripcion, tarea.estado, tarea.prioridad))

# Mostrar el panel principal después de iniciar sesión
def mostrar_panel_principal(usuario):
    global root, tree_proyectos, tree_tareas
    root = tk.Tk()
    root.title("Gestor de Tareas - Panel Principal")
    root.geometry("1000x700")
    root.configure(bg=COLOR_FONDO)

    frame_buttons = tk.Frame(root, bg=COLOR_FONDO, pady=20)
    frame_buttons.pack()
    tk.Button(frame_buttons, text="➕ Nuevo Proyecto", width=20, bg=COLOR_VERDE, fg=COLOR_TEXTO,
              command=lambda: crear_proyecto_window(usuario)).grid(row=0, column=0, padx=15)
    tk.Button(frame_buttons, text="📝 Nueva Tarea", width=20, bg=COLOR_VERDE, fg=COLOR_TEXTO,
              command=lambda: crear_tarea_window(usuario)).grid(row=0, column=1, padx=15)
    tk.Button(frame_buttons, text="📈 Ver Progreso", width=20, bg=COLOR_VERDE, fg=COLOR_TEXTO).grid(row=0, column=2, padx=15)

    tk.Label(root, text="📁 Proyectos", font=("Arial", 13, "bold"), bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=(10, 5))
    tree_proyectos = ttk.Treeview(root, columns=("ID", "Nombre", "Inicio", "Fin"), show="headings", height=8)
    for col in tree_proyectos["columns"]:
        tree_proyectos.heading(col, text=col)
    tree_proyectos.pack(pady=10, fill="x", padx=30)

    tk.Label(root, text="📋 Tareas Asignadas", font=("Arial", 13, "bold"), bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=(20, 5))
    tree_tareas = ttk.Treeview(root, columns=("ID", "Descripción", "Estado", "Prioridad"), show="headings", height=8)
    for col in tree_tareas["columns"]:
        tree_tareas.heading(col, text=col)
    tree_tareas.pack(pady=10, fill="x", padx=30)

    cargar_datos(usuario)
    root.mainloop()
