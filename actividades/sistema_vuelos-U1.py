"""
Sistema básico de gestión de pasajeros para una aerolínea.
Permite crear vuelos, reservar, cancelar y listar información.
"""


# =========================
# CLASES
# =========================

class Pasajero:
    """Representa un pasajero."""

    def __init__(self, nombre):
        self.nombre = nombre


class Vuelo:
    """Representa un vuelo."""

    def __init__(self, codigo):
        self.codigo = codigo
        self.pasajeros = []

    def reservar(self, pasajero):
        """Reserva un pasajero si no existe."""
        for p in self.pasajeros:
            if p.nombre.lower() == pasajero.nombre.lower():
                return False

        self.pasajeros.append(pasajero)
        return True

    def cancelar(self, nombre_pasajero):
        """Cancela la reserva de un pasajero."""
        for p in self.pasajeros:
            if p.nombre.lower() == nombre_pasajero.lower():
                self.pasajeros.remove(p)
                return True

        return False

    def listar_pasajeros(self):
        """Devuelve lista de nombres."""
        nombres = []

        for p in self.pasajeros:
            nombres.append(p.nombre)

        return nombres


class Aerolinea:
    """Representa la aerolínea."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.vuelos = []

    def agregar_vuelo(self, vuelo):
        """Agrega un vuelo si no existe."""
        if self.buscar_vuelo(vuelo.codigo):
            return False

        self.vuelos.append(vuelo)
        return True

    def buscar_vuelo(self, codigo):
        """Busca vuelo por código."""
        for v in self.vuelos:
            if v.codigo.lower() == codigo.lower():
                return v

        return None

    def listar_vuelos(self):
        """Devuelve lista de códigos."""
        codigos = []

        for v in self.vuelos:
            codigos.append(v.codigo)

        return codigos


# =========================
# MAIN
# =========================

def main():
    aerolinea = Aerolinea("SkyCode")

    while True:
        print("\n=== MENÚ AEROLÍNEA ===")
        print("1) Agregar vuelo")
        print("2) Reservar pasajero")
        print("3) Cancelar reserva")
        print("4) Listar pasajeros de un vuelo")
        print("5) Listar vuelos")
        print("6) Salir")

        opcion = input("Elige opción: ").strip()

        if opcion == "1":
            codigo = input("Código del vuelo: ").strip()
            vuelo = Vuelo(codigo)

            if aerolinea.agregar_vuelo(vuelo):
                print("Vuelo agregado correctamente.")
            else:
                print("Ese vuelo ya existe.")

        elif opcion == "2":
            codigo = input("Código del vuelo: ").strip()
            vuelo = aerolinea.buscar_vuelo(codigo)

            if vuelo:
                nombre = input("Nombre del pasajero: ").strip()
                pasajero = Pasajero(nombre)

                if vuelo.reservar(pasajero):
                    print("Reserva realizada con éxito.")
                else:
                    print("Ese pasajero ya está reservado.")
            else:
                print("Vuelo no encontrado.")

        elif opcion == "3":
            codigo = input("Código del vuelo: ").strip()
            vuelo = aerolinea.buscar_vuelo(codigo)

            if vuelo:
                nombre = input("Nombre del pasajero a cancelar: ").strip()

                if vuelo.cancelar(nombre):
                    print("Reserva cancelada correctamente.")
                else:
                    print("Pasajero no encontrado.")
            else:
                print("Vuelo no encontrado.")

        elif opcion == "4":
            codigo = input("Código del vuelo: ").strip()
            vuelo = aerolinea.buscar_vuelo(codigo)

            if vuelo:
                pasajeros = vuelo.listar_pasajeros()

                if not pasajeros:
                    print("No hay pasajeros en este vuelo.")
                else:
                    print(f"Pasajeros del vuelo {codigo}:")
                    for nombre in pasajeros:
                        print("-", nombre)
            else:
                print("Vuelo no encontrado.")

        elif opcion == "5":
            vuelos = aerolinea.listar_vuelos()

            if not vuelos:
                print("No hay vuelos registrados.")
            else:
                print("Vuelos disponibles:")
                for codigo in vuelos:
                    print("-", codigo)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
