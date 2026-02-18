import random as rd


# =========================
# CLASES
# =========================

class Jugador:
    """Representa a un jugador del juego."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.exp = 0
        self.nivel = 1

    def subir_nivel(self, experiencia):
        """Aumenta experiencia y sube nivel cada 10 puntos."""
        self.exp += experiencia
        print(f"Experiencia actual: {self.exp}")

        while self.exp >= 10:
            self.nivel += 1
            self.exp -= 10
            print(f"¡Subiste a nivel {self.nivel}!")


class Item:
    """Representa un objeto del juego."""

    def __init__(self, nombre, experiencia):
        self.nombre = nombre
        self.experiencia = experiencia

    def __str__(self):
        return self.nombre


class SlotInventario:
    """Nodo de la lista enlazada."""

    def __init__(self, objeto):
        self.objeto = objeto
        self.siguiente = None


class Inventario:
    """Inventario implementado con lista enlazada simple."""

    def __init__(self, jugador):
        self.head = None
        self.jugador = jugador

    def contar_slots(self):
        actual = self.head
        contador = 0

        while actual:
            contador += 1
            actual = actual.siguiente

        return contador

    def tomar_item(self, objeto):
        capacidad = self.jugador.nivel * 5

        if self.contar_slots() >= capacidad:
            print("Inventario lleno.")
            return False

        nuevo = SlotInventario(objeto)
        nuevo.siguiente = self.head
        self.head = nuevo

        print(f"Tomaste {objeto.nombre}")
        return True

    def tirar_item(self, nombre_objeto):
        if not self.head:
            print("Inventario vacío")
            return

        if self.head.objeto.nombre == nombre_objeto:
            self.head = self.head.siguiente
            print(f"Tiraste {nombre_objeto}")
            return

        actual = self.head

        while actual.siguiente and actual.siguiente.objeto.nombre != nombre_objeto:
            actual = actual.siguiente

        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
            print(f"Tiraste {nombre_objeto}")
        else:
            print("Ese objeto no está en el inventario")

    def abrir_inventario(self):
        if not self.head:
            print("Inventario vacío")
            return

        actual = self.head
        print("Inventario:")

        while actual:
            print("-", actual.objeto.nombre)
            actual = actual.siguiente


# =========================
# DATOS
# =========================

objetos = [
    Item("Espada", 5),
    Item("Hacha", 5),
    Item("Madera", 2),
    Item("Hierro", 3),
    Item("Bomba", -5)
]


# =========================
# MAIN
# =========================

def main():
    nombre = input("Ingresa tu nombre: ")
    jugador = Jugador(nombre)
    inventario = Inventario(jugador)

    while True:
        print("\n=== OBJETO DROPEADO ===")
        objeto_dropeado = rd.choice(objetos)
        print(f"Apareció: {objeto_dropeado.nombre}")

        print("\n1) Abrir inventario")
        print("2) Tomar objeto")
        print("3) Ignorar")
        print("4) Salir")

        opcion = int(input("Elige opción: "))

        if opcion == 1:
            inventario.abrir_inventario()
            print("1) Tirar objeto")
            print("2) Volver")

            sub = int(input("Opción: "))
            if sub == 1:
                nombre_obj = input("Nombre del objeto a tirar: ")
                inventario.tirar_item(nombre_obj)

        elif opcion == 2:
            if inventario.tomar_item(objeto_dropeado):
                jugador.subir_nivel(objeto_dropeado.experiencia)

        elif opcion == 3:
            print("Ignoraste el objeto.")

        elif opcion == 4:
            print("Saliendo del juego...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
