"""
Módulo Producto - Taller 9 DevOps
Autor: fcajias (Estudiante 1)
"""


class Producto:
    """Representa un producto en el sistema de inventario."""

    def __init__(self, id: int, nombre: str, precio: float, stock: int = 0):
        """
        Inicializa un nuevo producto.

        Args:
            id (int): Identificador único del producto.
            nombre (str): Nombre del producto.
            precio (float): Precio base del producto.
            stock (int): Cantidad disponible en inventario.
        """
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @classmethod
    def from_dict(cls, data: dict) -> "Producto":
        """Crea un Producto desde un diccionario.

        Args:
            data (dict): Diccionario con los datos del producto.

        Returns:
            Producto: Nueva instancia de Producto.
        """
        return cls(
            id=data["id"],
            nombre=data["nombre"],
            precio=data["precio"],
            stock=data.get("stock", 0)
        )

    def aplicar_descuento(self, porcentaje: float) -> float:
        """
        Calcula el precio con descuento aplicado.

        Args:
            porcentaje (float): Porcentaje de descuento (0-100).

        Returns:
            float: Precio final con descuento.

        Raises:
            ValueError: Si el porcentaje no está entre 0 y 100.
        """
        if not (0 <= porcentaje <= 100):
            raise ValueError("El porcentaje debe estar entre 0 y 100.")
        descuento = self.precio * (porcentaje / 100)
        return round(self.precio - descuento, 2)

    def actualizar_stock(self, cantidad: int) -> None:
        """
        Actualiza el stock del producto.

        Args:
            cantidad (int): Cantidad a agregar (positivo) o restar (negativo).

        Raises:
            ValueError: Si el stock resultante es negativo.
        """
        nuevo_stock = self.stock + cantidad
        if nuevo_stock < 0:
            raise ValueError(f"Stock insuficiente. Stock actual: {self.stock}")
        self.stock = nuevo_stock

    def esta_disponible(self) -> bool:
        """Retorna True si el producto tiene stock disponible."""
        return self.stock > 0

    def __str__(self) -> str:
        """Representación en cadena del producto."""
        return (
            f"Producto(id={self.id}, nombre='{self.nombre}', "
            f"precio=${self.precio:.2f}, stock={self.stock})"
        )

    def to_dict(self) -> dict:
        """Serializa el producto a un diccionario."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "disponible": self.esta_disponible()
        }

    def __repr__(self) -> str:
        return self.__str__()
