import tkinter as tk
from tkinter import ttk, messagebox
from backadmin import obtener_proyectos_y_tareas, crear_proyecto, crear_tarea
from bd import Usuario, SessionLocal
import bcrypt
from backlogin import verificar_login, crear_usuario, cambiar_contraseña
from usuario import mostrar_panel_principal

def salir():
    if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?"):
        root.quit()


# ------ INICIAR SESIÓN ------
def abrir_login_window():
    login_window = tk.Toplevel(root)
    login_window.title("Iniciar Sesión")
    login_window.geometry("400x400")
    login_window.configure(bg="#d9f4d0")

    tk.Label(login_window, text="Nombre de usuario:", font=("Arial", 14), bg="#d9f4d0", fg="#234e1b").pack(pady=5)
    entry_username_login = tk.Entry(login_window, font=("Arial", 12))
    entry_username_login.pack(pady=5)

    tk.Label(login_window, text="Contraseña:", font=("Arial", 14), bg="#d9f4d0", fg="#234e1b").pack(pady=5)
    entry_password_login = tk.Entry(login_window, font=("Arial", 12), show="*")
    entry_password_login.pack(pady=5)

    def intentar_login():
        username = entry_username_login.get()
        password = entry_password_login.get()
        user = verificar_login(username, password)

        if user:
            messagebox.showinfo("Éxito", "¡Inicio de sesión exitoso!")
            login_window.destroy()
            root.destroy()
            if user.rol == "administrador":
                import administrador
                administrador.mostrar_panel_principal(user)
            elif user.rol == "usuario":
                import usuario
                usuario.mostrar_panel_principal(user)
            else:
                messagebox.showerror("Rol inválido", f"Rol desconocido: {user.rol}")
        else:
            messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos.")

    tk.Button(login_window, text="Entrar", command=intentar_login,
              font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=20)


# ------ CREAR USUARIO ------
def crear_usuario_window():
    create_window = tk.Toplevel(root)
    create_window.title("Crear Nuevo Usuario")
    create_window.geometry("400x500")
    create_window.configure(bg="#d9f4d0")

    selected_role = tk.StringVar(value="usuario")  # valor por defecto

    tk.Label(create_window, text="Nombre de usuario:", font=("Arial", 14), bg="#d9f4d0", fg="#234e1b").pack(pady=5)
    entry_new_username = tk.Entry(create_window, font=("Arial", 12))
    entry_new_username.pack(pady=5)

    tk.Label(create_window, text="Contraseña:", font=("Arial", 14), bg="#d9f4d0", fg="#234e1b").pack(pady=5)
    entry_new_password = tk.Entry(create_window, font=("Arial", 12), show="*")
    entry_new_password.pack(pady=5)

    tk.Label(create_window, text="Selecciona tu rol:", font=("Arial", 14), bg="#d9f4d0", fg="#234e1b").pack(pady=10)

    role_frame = tk.Frame(create_window, bg="#d9f4d0")
    role_frame.pack(pady=5)

    def seleccionar_rol(rol):
        selected_role.set(rol)
        btn_usuario.configure(bg="#b6e7c9" if rol == "usuario" else "white")
        btn_admin.configure(bg="#b6e7c9" if rol == "administrador" else "white")

    btn_usuario = tk.Button(role_frame, text="Usuario", width=10, font=("Arial", 12),
                            command=lambda: seleccionar_rol("usuario"), bg="#b6e7c9")
    btn_usuario.grid(row=0, column=0, padx=10)

    btn_admin = tk.Button(role_frame, text="Administrador", width=12, font=("Arial", 12),
                          command=lambda: seleccionar_rol("administrador"), bg="white")
    btn_admin.grid(row=0, column=1, padx=10)

    tk.Label(create_window, text="Correo electrónico:", font=("Arial", 14), bg="#d9f4d0", fg="#234e1b").pack(pady=5)
    entry_new_email = tk.Entry(create_window, font=("Arial", 12))
    entry_new_email.pack(pady=5)

    def guardar_usuario():
        new_username = entry_new_username.get()
        new_password = entry_new_password.get()
        new_email = entry_new_email.get()
        rol = selected_role.get()

        if new_username and new_password and rol and new_email:
            # Permitir crear administrador desde la ventana de registro
            result = crear_usuario(new_username, new_password, rol, new_email, creador_admin=True)
            if result == "¡Usuario creado exitosamente!":
                messagebox.showinfo("Éxito", result)
                create_window.destroy()
            else:
                messagebox.showerror("Error", result)
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    tk.Button(create_window, text="Guardar Usuario", command=guardar_usuario,
              font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=20)


# ------ CAMBIAR CONTRASEÑA ------
def cambiar_contraseña_window():
    cambio_window = tk.Toplevel(root)
    cambio_window.title("Recuperar Contraseña")
    cambio_window.geometry("400x400")
    cambio_window.configure(bg="#d9f4d0")

    tk.Label(cambio_window, text="Nombre de usuario:", font=("Arial", 14), bg="#d9f4d0", fg="#234e1b").pack(pady=5)
    entry_user = tk.Entry(cambio_window, font=("Arial", 12))
    entry_user.pack(pady=5)

    tk.Label(cambio_window, text="Nueva contraseña:", font=("Arial", 14), bg="#d9f4d0", fg="#234e1b").pack(pady=5)
    entry_new_pass = tk.Entry(cambio_window, font=("Arial", 12), show="*")
    entry_new_pass.pack(pady=5)

    def cambiar():
        user = entry_user.get()
        new_pass = entry_new_pass.get()
        if user and new_pass:
            result = cambiar_contraseña(user, new_pass)
            if result == "¡Contraseña actualizada!":
                messagebox.showinfo("Éxito", result)
                cambio_window.destroy()
            else:
                messagebox.showerror("Error", result)
        else:
            messagebox.showerror("Error", "Por favor, complete los campos.")

    tk.Button(cambio_window, text="Actualizar", command=cambiar,
              font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=20)


# ------ VENTANA PRINCIPAL ------
root = tk.Tk()
root.title("Bienvenido")
root.geometry("800x600")
root.configure(bg="#c7f5cc")

tk.Label(root, text="Bienvenido a la aplicación", font=("Arial", 24, "bold"),
         bg="#c7f5cc", fg="#234e1b").pack(pady=60)

tk.Button(root, text="REGISTRARSE", command=crear_usuario_window,
          font=("Arial", 16, "bold"), bg="white", fg="#2d8f47",
          relief="flat", bd=3, padx=20, pady=10).pack(pady=10)

tk.Button(root, text="INICIAR SESIÓN", command=abrir_login_window,
          font=("Arial", 16, "bold"), bg="white", fg="#2d8f47",
          relief="flat", bd=3, padx=20, pady=10).pack(pady=10)

tk.Button(root, text="¿Olvidaste tu contraseña?", command=cambiar_contraseña_window,
          font=("Arial", 12, "underline"), bg="#c7f5cc", fg="#234e1b",
          relief="flat", cursor="hand2").pack(pady=5)

tk.Button(root, text="SALIR", command=salir,
          font=("Arial", 12), bg="#a1a1a1", fg="white",
          relief="flat", padx=10, pady=5).pack(pady=30)

root.mainloop()
