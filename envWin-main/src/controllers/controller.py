from tkinter import messagebox

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

        # Botones Principales
        self.vista.btn_inicio.config(command=self.agregar_inicio)
        self.vista.btn_final.config(command=self.agregar_final)
        self.vista.btn_completar.config(command=self.marcar_hecho)
        self.vista.btn_eliminar.config(command=self.eliminar_tarea)
        
        # Botones de Búsqueda por Texto
        self.vista.btn_buscar_marcar.config(command=self.buscar_marcar)
        self.vista.btn_buscar_quitar.config(command=self.buscar_quitar)

        # Evento de doble clic
        self.vista.tabla.bind("<Double-1>", self.abrir_detalle)

    def abrir_detalle(self, event):
        datos = self.vista.obtener_seleccion()
        if datos:
            self.vista.ventana_detalle(datos)

    def agregar_inicio(self):
        t, d = self.vista.obtener_datos()
        if t:
            self.modelo.agregar_al_inicio(t, d)
            self.vista.limpiar_campos()
            self.refrescar()

    def agregar_final(self):
        t, d = self.vista.obtener_datos()
        if t:
            self.modelo.agregar_al_final(t, d)
            self.vista.limpiar_campos()
            self.refrescar()

    def marcar_hecho(self):
        datos = self.vista.obtener_seleccion()
        titulo = datos['titulo'] if datos else self.vista.obtener_datos()[0]
        if titulo:
            self.modelo.buscar_y_marcar_completada(titulo)
            self.refrescar()

    def eliminar_tarea(self):
        datos = self.vista.obtener_seleccion()
        titulo = datos['titulo'] if datos else self.vista.obtener_datos()[0]
        if titulo and messagebox.askyesno("Eliminar", f"¿Desea eliminar '{titulo}'?"):
            self.modelo.buscar_y_eliminar(titulo)
            self.refrescar()

    def buscar_marcar(self):
        titulo, _ = self.vista.obtener_datos()
        if self.modelo.buscar_y_marcar_completada(titulo):
            self.refrescar()
        else:
            messagebox.showwarning("Búsqueda", "Tarea no encontrada.")

    def buscar_quitar(self):
        titulo, _ = self.vista.obtener_datos()
        if titulo and self.modelo.buscar_y_eliminar(titulo):
            self.refrescar()

    def refrescar(self):
        self.vista.actualizar_tabla(self.modelo.obtener_todas_las_tareas())