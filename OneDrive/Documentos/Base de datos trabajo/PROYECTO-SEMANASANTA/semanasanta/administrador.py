import tkinter as tk
from tkinter import ttk, messagebox
from backadmin import obtener_proyectos_y_tareas, crear_proyecto, crear_tarea
from bd import Usuario, SessionLocal
import bcrypt
import datetime

# Colores
COLOR_FONDO = "#dfeee6"
COLOR_VERDE = "#3b9a6b"
COLOR_VERDE_OSCURO = "#15400e"
COLOR_GRIS_CLARO = "#ecf0f1"
COLOR_GRIS_OSCURO = "#7f8c8d"
COLOR_TEXTO = "#000000"  # Letras negras
COLOR_BORDE = "#a5c9b0"

# Función para cargar datos

def cargar_datos(usuario):
    proyectos, tareas = obtener_proyectos_y_tareas(usuario.id_usuario)

    tree_proyectos.delete(*tree_proyectos.get_children())
    tree_tareas.delete(*tree_tareas.get_children())

    for proyecto in proyectos:
        porcentaje = calcular_porcentaje_progreso(proyecto.fecha_inicio, proyecto.fecha_fin)
        color = determinar_color_progreso(porcentaje)
        tree_proyectos.insert("", "end", values=(proyecto.id_proyecto, proyecto.nombre, proyecto.fecha_inicio, proyecto.fecha_fin, f"{porcentaje}%"), tags=(color,))

    for tarea in tareas:
        porcentaje = calcular_porcentaje_progreso(datetime.datetime.now().strftime("%Y-%m-%d"), tarea.fecha_vencimiento.strftime("%Y-%m-%d"))
        color = determinar_color_progreso(porcentaje)
        tree_tareas.insert("", "end", values=(tarea.id_tarea, tarea.descripcion, tarea.estado, tarea.prioridad, f"{porcentaje}%"), tags=(color,))

# Determinar color según progreso

def determinar_color_progreso(porcentaje):
    if porcentaje < 50:
        return "rojo"
    elif porcentaje < 80:
        return "naranja"
    else:
        return "verde"

# Calcular porcentaje de progreso

def calcular_porcentaje_progreso(fecha_inicio_str, fecha_fin_str):
    try:
        fecha_inicio = datetime.datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
        fecha_fin = datetime.datetime.strptime(fecha_fin_str, "%Y-%m-%d")
        ahora = datetime.datetime.now()
        total = (fecha_fin - fecha_inicio).total_seconds()
        transcurrido = (ahora - fecha_inicio).total_seconds()
        porcentaje = min(max(int((transcurrido / total) * 100), 0), 100)
        return porcentaje
    except:
        return 0

# Mostrar tiempo restante en selección con cronómetro en vivo

def mostrar_tiempo_restante(event):
    item = tree_proyectos.selection() or tree_tareas.selection()
    if not item:
        return

    item_id = tree_proyectos.item(item[0])["values"] if tree_proyectos.selection() else tree_tareas.item(item[0])["values"]
    fecha_fin_str = item_id[3] if tree_proyectos.selection() else item_id[4]

    try:
        fecha_fin = datetime.datetime.strptime(fecha_fin_str, "%Y-%m-%d")
    except:
        messagebox.showerror("Error", "Fecha inválida")
        return

    ventana = tk.Toplevel(root)
    ventana.title("Cuenta Regresiva")
    ventana.configure(bg=COLOR_FONDO)
    ventana.geometry("300x120")
    ventana.resizable(False, False)

    label = tk.Label(ventana, text="Cuenta regresiva hasta la fecha final:", font=("Segoe UI", 11), bg=COLOR_FONDO)
    label.pack(pady=10)

    tiempo_label = tk.Label(ventana, text="", font=("Segoe UI", 16, "bold"), bg=COLOR_FONDO)
    tiempo_label.pack(pady=5)

    def actualizar_cronometro():
        ahora = datetime.datetime.now()
        restante = fecha_fin - ahora
        if restante.total_seconds() > 0:
            dias = restante.days
            horas = int((restante.total_seconds() % 86400) // 3600)
            minutos = int((restante.total_seconds() % 3600) // 60)
            segundos = int(restante.total_seconds() % 60)
            tiempo_str = f"{dias}d {horas}h {minutos}m {segundos}s"
            tiempo_label.config(text=tiempo_str)
            ventana.after(1000, actualizar_cronometro)
        else:
            tiempo_label.config(text="¡Tiempo finalizado!")

    actualizar_cronometro()

# Ver tareas y proyectos vencidos

def mostrar_vencidos():
    proyectos, tareas = obtener_proyectos_y_tareas(usuario_global.id_usuario)
    vencidos = []
    ahora = datetime.datetime.now().date()

    ventana = tk.Toplevel(root)
    ventana.title("Tareas y Proyectos Vencidos")
    ventana.configure(bg=COLOR_FONDO)
    ventana.geometry("500x400")

    texto = tk.Text(ventana, wrap="word", font=("Segoe UI", 11), bg=COLOR_GRIS_CLARO)
    texto.pack(padx=10, pady=10, fill="both", expand=True)

    for proyecto in proyectos:
        if proyecto.fecha_fin < ahora:
            vencidos.append(f"📁 Proyecto vencido: {proyecto.nombre} (Fin: {proyecto.fecha_fin.strftime('%Y-%m-%d')})")

    for tarea in tareas:
        if tarea.fecha_vencimiento < ahora:
            vencidos.append(f"📝 Tarea vencida: {tarea.descripcion} (Vence: {tarea.fecha_vencimiento.strftime('%Y-%m-%d')})")

    if vencidos:
        mensaje = "\n".join(vencidos)
    else:
        mensaje = "No hay tareas ni proyectos vencidos."

    texto.insert("1.0", mensaje)
    texto.configure(state="disabled")

# Mostrar el panel principal

def mostrar_panel_principal(usuario):
    global root, tree_proyectos, tree_tareas, usuario_global
    usuario_global = usuario
    root = tk.Tk()
    root.title("Gestor de Tareas - Panel Principal")
    root.geometry("1100x700")
    root.configure(bg=COLOR_FONDO)

    frame_left = tk.Frame(root, bg=COLOR_GRIS_CLARO, width=220, bd=2, relief="solid")
    frame_left.pack(side="left", fill="y")
    frame_left.pack_propagate(False)

    button_style = {
        "width": 20,
        "height": 2,
        "bg": COLOR_VERDE,
        "fg": COLOR_TEXTO,
        "font": ("Segoe UI", 11, "bold"),
        "relief": "flat",
        "activebackground": COLOR_VERDE_OSCURO
    }

    tk.Label(frame_left, text="Menú", font=("Segoe UI", 14, "bold"), bg=COLOR_GRIS_CLARO, fg=COLOR_TEXTO).pack(pady=20)
    tk.Button(frame_left, text="➕ Nuevo Proyecto", command=lambda: crear_proyecto_window(usuario), **button_style).pack(pady=10)
    tk.Button(frame_left, text="📝 Nueva Tarea", command=lambda: crear_tarea_window(usuario), **button_style).pack(pady=10)
    tk.Button(frame_left, text="📅 Vencidos", command=mostrar_vencidos, **button_style).pack(pady=10)
    tk.Button(frame_left, text="👥 Asignar Tarea", command=asignar_tarea_window, **button_style).pack(pady=10)

    frame_right = tk.Frame(root, bg=COLOR_FONDO)
    frame_right.pack(side="right", fill="both", expand=True)

    tk.Label(frame_right, text="📁 Proyectos", font=("Segoe UI", 16, "bold"), bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=(20, 5))
    style = ttk.Style()
    style.configure("Treeview", font=("Segoe UI", 11), rowheight=28)
    style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"))

    tree_proyectos = ttk.Treeview(frame_right, columns=("ID", "Nombre", "Inicio", "Fin", "Progreso"), show="headings", height=7)
    for col in tree_proyectos["columns"]:
        tree_proyectos.heading(col, text=col)
        tree_proyectos.column(col, anchor="center")
    tree_proyectos.tag_configure("rojo", background="#ffcccc")
    tree_proyectos.tag_configure("naranja", background="#fff0b3")
    tree_proyectos.tag_configure("verde", background="#ccffcc")
    tree_proyectos.pack(padx=20, fill="x")
    tree_proyectos.bind("<Double-1>", mostrar_tiempo_restante)

    tk.Label(frame_right, text="📋 Tareas Asignadas", font=("Segoe UI", 16, "bold"), bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=(30, 5))
    tree_tareas = ttk.Treeview(frame_right, columns=("ID", "Descripción", "Estado", "Prioridad", "Progreso"), show="headings", height=7)
    for col in tree_tareas["columns"]:
        tree_tareas.heading(col, text=col)
        tree_tareas.column(col, anchor="center")
    tree_tareas.tag_configure("rojo", background="#ffcccc")
    tree_tareas.tag_configure("naranja", background="#fff0b3")
    tree_tareas.tag_configure("verde", background="#ccffcc")
    tree_tareas.pack(padx=20, fill="x")
    tree_tareas.bind("<Double-1>", mostrar_tiempo_restante)

    cargar_datos(usuario)
    root.mainloop()

# Crear Proyecto

def crear_proyecto_window(usuario):
    def guardar_proyecto():
        nombre = entry_nombre.get()
        fecha_inicio = entry_inicio.get()
        fecha_fin = entry_fin.get()
        integrantes = entry_integrantes.get()

        if nombre and fecha_inicio:
            proyecto = crear_proyecto(nombre, fecha_inicio, fecha_fin)
            if proyecto:
                messagebox.showinfo("Éxito", f"Proyecto creado exitosamente.\nIntegrantes: {integrantes}")
                win.destroy()
                cargar_datos(usuario)
            else:
                messagebox.showerror("Error", "Hubo un problema al crear el proyecto.")
        else:
            messagebox.showerror("Error", "Complete todos los campos.")

    win = tk.Toplevel(root)
    win.title("Nuevo Proyecto")
    win.configure(bg=COLOR_FONDO)

    campos = [
        ("Nombre del Proyecto:", "nombre"),
        ("Fecha de Inicio (YYYY-MM-DD):", "inicio"),
        ("Fecha de Fin:", "fin"),
        ("Correos de Integrantes (separados por coma):", "integrantes")
    ]
    entries = {}

    for text, var in campos:
        tk.Label(win, text=text, font=("Segoe UI", 11), bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=(10, 0))
        entry = tk.Entry(win, font=("Segoe UI", 11))
        entry.pack(padx=20, pady=5, fill="x")
        entries[var] = entry

    entry_nombre = entries["nombre"]
    entry_inicio = entries["inicio"]
    entry_fin = entries["fin"]
    entry_integrantes = entries["integrantes"]

    tk.Button(win, text="Guardar", command=guardar_proyecto, bg=COLOR_VERDE_OSCURO, fg=COLOR_TEXTO,
              font=("Segoe UI", 11, "bold"), relief="flat").pack(pady=20)

# Crear Tarea

def crear_tarea_window(usuario):
    def guardar_tarea():
        descripcion = entry_desc.get()
        fecha = entry_fecha.get()

        if descripcion and fecha:
            tarea = crear_tarea(1, descripcion, fecha)
            if tarea:
                messagebox.showinfo("Éxito", "Tarea creada exitosamente.")
                win.destroy()
                cargar_datos(usuario)
            else:
                messagebox.showerror("Error", "No se pudo crear la tarea.")
        else:
            messagebox.showerror("Error", "Complete todos los campos.")

    win = tk.Toplevel(root)
    win.title("Nueva Tarea")
    win.configure(bg=COLOR_FONDO)

    tk.Label(win, text="Descripción:", font=("Segoe UI", 11), bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=(10, 0))
    entry_desc = tk.Entry(win, font=("Segoe UI", 11))
    entry_desc.pack(padx=20, pady=5, fill="x")

    tk.Label(win, text="Fecha de Vencimiento (YYYY-MM-DD):", font=("Segoe UI", 11), bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=(10, 0))
    entry_fecha = tk.Entry(win, font=("Segoe UI", 11))
    entry_fecha.pack(padx=20, pady=5, fill="x")

    tk.Button(win, text="Guardar", command=guardar_tarea, bg=COLOR_VERDE_OSCURO, fg=COLOR_TEXTO,
              font=("Segoe UI", 11, "bold"), relief="flat").pack(pady=20)

# Asignar tarea

def asignar_tarea_window():
    win = tk.Toplevel(root)
    win.title("Asignar Tarea a Usuario")
    win.configure(bg=COLOR_FONDO)

    tk.Label(win, text="(Simulado) Seleccionar tarea y usuario para asignar.", font=("Segoe UI", 11), bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(padx=20, pady=20)
    tk.Button(win, text="Cerrar", command=win.destroy, bg=COLOR_VERDE_OSCURO, fg=COLOR_TEXTO, font=("Segoe UI", 11, "bold"), relief="flat").pack(pady=10)