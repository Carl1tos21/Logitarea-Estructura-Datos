import datetime

class Nodo:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = 'pendiente'
        self.fecha_registro = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        self.siguiente = None

class ModeloDatos:
    def __init__(self):
        self.cabeza = None

    def agregar_al_inicio(self, titulo, descripcion):
        nuevo_nodo = Nodo(titulo, descripcion)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def agregar_al_final(self, titulo, descripcion):
        nuevo_nodo = Nodo(titulo, descripcion)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def obtener_todas_las_tareas(self):
        tareas = []
        actual = self.cabeza
        while actual:
            tareas.append({
                'titulo': actual.titulo,
                'descripcion': actual.descripcion,
                'estado': actual.estado,
                'fecha': actual.fecha_registro
            })
            actual = actual.siguiente
        return tareas

    def buscar_y_marcar_completada(self, titulo):
        actual = self.cabeza
        while actual:
            if actual.titulo.lower() == titulo.lower():
                actual.estado = 'completada'
                return True
            actual = actual.siguiente
        return False

    def buscar_y_eliminar(self, titulo):
        if not self.cabeza: return False
        if self.cabeza.titulo.lower() == titulo.lower():
            self.cabeza = self.cabeza.siguiente
            return True
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.titulo.lower() == titulo.lower():
                actual.siguiente = actual.siguiente.siguiente
                return True
            actual = actual.siguiente
        return False           