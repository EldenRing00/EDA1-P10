# Importar la biblioteca "os" para limpiar la pantalla
import os

# Lista para almacenar los libros
biblioteca = []

# Función para agregar un libro a la biblioteca
def agregar_libro():
    libro = input("Ingrese el nombre del libro: ")
    biblioteca.append(libro)
    print("Libro agregado correctamente.")

# Función para eliminar un libro de la biblioteca
def eliminar_libro():
    libro = input("Ingrese el nombre del libro a eliminar: ")
    if libro in biblioteca:
        biblioteca.remove(libro)
        print("Libro eliminado correctamente.")
    else:
        print("El libro no existe en la biblioteca.")

# Función para ordenar la biblioteca alfabéticamente
def ordenar_biblioteca():
    biblioteca.sort()
    print("Biblioteca ordenada correctamente.")

# Función para mostrar los libros de la biblioteca
def ver_biblioteca():
    if len(biblioteca) == 0:
        print("La biblioteca está vacía.")
    else:
        print("Libros en la biblioteca:")
        for libro in biblioteca:
            print(libro)

# Función principal del programa
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla
        print("Bienvenido a la biblioteca")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Ordenar biblioteca")
        print("4. Ver biblioteca")
        print("5. Salir")
        opcion = input("Ingresa una opción: ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            eliminar_libro()
        elif opcion == "3":
            ordenar_biblioteca()
        elif opcion == "4":
            ver_biblioteca()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            input("Opción inválida. Presiona Enter para continuar.")

# Llamar a la función principal del programa
main()
