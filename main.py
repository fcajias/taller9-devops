"""
main.py - Punto de entrada del sistema de ventas.
Taller 9 DevOps - Flujo colaborativo con GitHub.
"""

from src.producto import Producto
from src.cliente import Cliente


def main():
    print("=== Sistema de Ventas - Taller 9 DevOps ===\n")

    # Crear productos (Estudiante 1 - fcajias)
    laptop = Producto(1, "Laptop HP", 1200.00, 10)
    mouse = Producto(2, "Mouse Inalámbrico", 35.50, 50)
    teclado = Producto(3, "Teclado Mecánico", 89.99, 25)

    print("Productos disponibles:")
    print(f"  {laptop}")
    print(f"  {mouse}")
    print(f"  {teclado}")

    # Crear cliente (Estudiante 2 - Fernando-Cajias)
    cliente = Cliente(1, "Ana García", "ana.garcia@email.com")
    print(f"\nCliente: {cliente}")

    # Agregar productos al carrito
    cliente.agregar_producto(laptop)
    cliente.agregar_producto(mouse)
    cliente.agregar_producto(teclado)

    print(f"\nCarrito de {cliente.nombre}:")
    for p in cliente.ver_carrito():
        print(f"  - {p.nombre}: ${p.precio:.2f}")

    total = cliente.calcular_total()
    print(f"\nTotal del carrito: ${total:.2f}")

    # Aplicar descuento
    precio_con_descuento = laptop.aplicar_descuento(15)
    print(f"Laptop con 15% de descuento: ${precio_con_descuento:.2f}")

    print("\n✔ Sistema funcionando correctamente!")


if __name__ == "__main__":
    main()
