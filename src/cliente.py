"""
Módulo Cliente - Taller 9 DevOps
Autor: Fernando-Cajias (Estudiante 2)
"""

from typing import List
from src.producto import Producto


class Cliente:
    """Representa un cliente en el sistema de ventas."""

    def __init__(self, id: int, nombre: str, email: str):
        """
        Inicializa un nuevo cliente.

        Args:
            id (int): Identificador único del cliente.
            nombre (str): Nombre completo del cliente.
            email (str): Correo electrónico del cliente.
        """
        if "@" not in email:
            raise ValueError("El email no es válido.")
        self.id = id
        self.nombre = nombre
        self.email = email
        self._carrito: List[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega un producto al carrito del cliente.

        Args:
            producto (Producto): Producto a agregar al carrito.

        Raises:
            ValueError: Si el producto no está disponible.
        """
        if not producto.esta_disponible():
            raise ValueError(
                f"El producto '{producto.nombre}' no tiene stock disponible."
            )
        self._carrito.append(producto)

    def eliminar_producto(self, id_producto: int) -> bool:
        """
        Elimina un producto del carrito por su ID.

        Args:
            id_producto (int): ID del producto a eliminar.

        Returns:
            bool: True si se eliminó, False si no se encontró.
        """
        for i, p in enumerate(self._carrito):
            if p.id == id_producto:
                self._carrito.pop(i)
                return True
        return False

    def calcular_total(self) -> float:
        """
        Calcula el total de los productos en el carrito.

        Returns:
            float: Suma de precios de todos los productos en el carrito.
        """
        return round(sum(p.precio for p in self._carrito), 2)

    def ver_carrito(self) -> List[Producto]:
        """Retorna la lista de productos en el carrito."""
        return list(self._carrito)

    def vaciar_carrito(self) -> None:
        """Vacía el carrito del cliente."""
        self._carrito.clear()

    def __str__(self) -> str:
        """Representación en cadena del cliente."""
        return (
            f"Cliente(id={self.id}, nombre='{self.nombre}', "
            f"email='{self.email}', items_carrito={len(self._carrito)})"
        )

    def to_dict(self) -> dict:
        """Serializa el cliente a un diccionario."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "total_carrito": self.calcular_total(),
            "items": len(self._carrito)
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Cliente":
        """Crea un Cliente desde un diccionario.

        Args:
            data (dict): Diccionario con los datos del cliente.

        Returns:
            Cliente: Nueva instancia de Cliente.
        """
        return cls(
            id=data["id"],
            nombre=data["nombre"],
            email=data["email"]
        )

    def __repr__(self) -> str:
        return self.__str__()
