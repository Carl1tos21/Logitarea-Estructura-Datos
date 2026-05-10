import tkinter as tk
from tkinter import ttk

class Vista:
    def __init__(self, maestro):
        self.maestro = maestro
        maestro.title("Logitarea - Gestión de Tareas") 
        maestro.geometry("1100x700")

        # --- PANEL DE CONTROL (IZQUIERDA) ---
        self.sidebar = tk.Frame(maestro, bg="#2f3542", width=250)
        self.sidebar.pack(side="left", fill="y")

        tk.Label(self.sidebar, text="PANEL DE CONTROL", font=("Helvetica", 10, "bold"), 
                 bg="#2f3542", fg="#a4b0be", pady=30).pack()

        self.btn_inicio = self._crear_boton(self.sidebar, "Agregar al Inicio", "#57606f")
        self.btn_final = self._crear_boton(self.sidebar, "Agregar al Final", "#57606f")
        
        tk.Frame(self.sidebar, height=20, bg="#2f3542").pack()

        self.btn_completar = self._crear_boton(self.sidebar, "Marcar como Hecho", "#10ac84")
        self.btn_eliminar = self._crear_boton(self.sidebar, "Eliminar Tarea", "#ee5253")

        tk.Frame(self.sidebar, height=20, bg="#2f3542").pack()

        self.btn_buscar_marcar = self._crear_boton(self.sidebar, "Buscar y Marcar", "#1e90ff")
        self.btn_buscar_quitar = self._crear_boton(self.sidebar, "Buscar y Quitar", "#ffa502")

        # --- ÁREA CENTRAL ---
        self.contenedor = tk.Frame(maestro, bg="#dfe4ea")
        self.contenedor.pack(side="right", fill="both", expand=True, padx=30, pady=20)

        # SECCIÓN DE ENTRADA CON COMBOBOX (LISTAS DESPLEGABLES)
        tk.Label(self.contenedor, text="Título de la tarea (Seleccione Materia):", font=("Helvetica", 10, "bold"), bg="#dfe4ea").pack(anchor="w")
        
        # Opciones para el Título
        opciones_titulo = ["Programación", "Ensamblador", "ED1", "Ecuaciones Diferenciales"]
        self.ent_titulo = ttk.Combobox(self.contenedor, values=opciones_titulo, font=("Arial", 12))
        self.ent_titulo.pack(fill="x", ipady=5, pady=(2, 10))
        self.ent_titulo.set(opciones_titulo[0]) # Valor por defecto

        tk.Label(self.contenedor, text="Descripción de la tarea (Seleccione Plazo):", font=("Helvetica", 10, "bold"), bg="#dfe4ea").pack(anchor="w")
        
        # Opciones para la Descripción
        opciones_desc = ["Tarea el martes", "Examen el lunes", "Exposición de proyecto el lunes"]
        self.ent_desc = ttk.Combobox(self.contenedor, values=opciones_desc, font=("Arial", 12))
        self.ent_desc.pack(fill="x", ipady=5, pady=(2, 20))
        self.ent_desc.set(opciones_desc[0]) # Valor por defecto

        # TABLA Y RESTO DE LA INTERFAZ
        self.tabla = ttk.Treeview(self.contenedor, columns=("Estado", "Titulo", "Fecha", "FullDesc"), show="headings")
        self.tabla.heading("Estado", text="ESTADO")
        self.tabla.heading("Titulo", text="TÍTULO DE LA TAREA")
        self.tabla.heading("Fecha", text="FECHA DE REGISTRO")

        self.tabla.column("Estado", width=120, anchor="center")
        self.tabla.column("Titulo", width=400, anchor="w")
        self.tabla.column("Fecha", width=180, anchor="center")
        self.tabla.column("FullDesc", width=0, stretch=tk.NO)

        self.tabla.pack(fill="both", expand=True)
        
        tk.Label(self.contenedor, text="* Doble clic en una tarea para ver la descripción completa", 
                 font=("Helvetica", 9, "italic"), bg="#dfe4ea", fg="#57606f").pack(pady=5)

    def _crear_boton(self, parent, texto, color):
        btn = tk.Button(parent, text=texto, bg=color, fg="white", font=("Helvetica", 9, "bold"),
                        relief="flat", cursor="hand2", pady=10, bd=0)
        btn.pack(fill="x", padx=20, pady=5)
        return btn

    def ventana_detalle(self, datos):
        ventana = tk.Toplevel(self.maestro)
        ventana.title("Detalles de la Tarea")
        ventana.geometry("400x350")
        ventana.configure(bg="white")
        tk.Label(ventana, text=datos['titulo'], font=("Arial", 13, "bold"), bg="white", pady=15).pack()
        frame_info = tk.Frame(ventana, bg="#f1f2f6", padx=15, pady=15)
        frame_info.pack(fill="both", expand=True, padx=20, pady=10)
        tk.Label(frame_info, text=f"Estado: {datos['estado']}", bg="#f1f2f6", font=("Arial", 10, "bold")).pack(anchor="w")
        tk.Label(frame_info, text=f"Fecha: {datos['fecha']}", bg="#f1f2f6").pack(anchor="w", pady=(0, 10))
        tk.Label(frame_info, text="Descripción:", bg="#f1f2f6", font=("Arial", 10, "bold")).pack(anchor="w")
        desc_text = tk.Label(frame_info, text=datos['descripcion'], bg="white", wraplength=300, justify="left", padx=10, pady=10)
        desc_text.pack(fill="x", pady=5)

    def obtener_datos(self):
        return self.ent_titulo.get().strip(), self.ent_desc.get().strip()

    def obtener_seleccion(self):
        item = self.tabla.selection()
        if item:
            v = self.tabla.item(item[0])['values']
            return {'estado': v[0], 'titulo': v[1], 'fecha': v[2], 'descripcion': v[3]}
        return None

    def limpiar_campos(self):
        # Para Combobox no es obligatorio limpiar, pero se puede resetear al primer valor
        self.ent_titulo.set("Programación")
        self.ent_desc.set("Tarea el martes")

    def actualizar_tabla(self, tareas):
        for i in self.tabla.get_children(): self.tabla.delete(i)
        for t in tareas:
            est = "✓ HECHO" if t['estado'] == 'completada' else "PENDIENTE"
            self.tabla.insert("", "end", values=(est, t['titulo'], t['fecha'], t['descripcion']))