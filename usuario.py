import tkinter as tk

def mostrar_panel_principal(usuario):
    root = tk.Tk()
    root.title("Panel de Usuario")
    root.geometry("600x400")
    root.configure(bg="#e0f8e9")

    tk.Label(root, text=f"Bienvenido, {usuario.nombre_usuario}", font=("Arial", 18, "bold"), bg="#e0f8e9", fg="#234e1b").pack(pady=20)
    tk.Label(root, text="Este es tu panel como USUARIO.", font=("Arial", 14), bg="#e0f8e9", fg="#234e1b").pack(pady=10)

    tk.Button(root, text="Salir", command=root.destroy,
              font=("Arial", 12), bg="#a1a1a1", fg="white",
              relief="flat", padx=10, pady=5).pack(pady=30)

    root.mainloop()
