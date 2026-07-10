"""Tests para la clase Cliente."""
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.producto import Producto
from src.cliente import Cliente


def test_crear_cliente():
    """Verifica que un cliente se crea correctamente."""
    c = Cliente(1, "Juan Pérez", "juan@email.com")
    assert c.id == 1
    assert c.nombre == "Juan Pérez"
    assert c.email == "juan@email.com"
    assert len(c.ver_carrito()) == 0


def test_agregar_producto():
    """Verifica que se agrega un producto al carrito."""
    c = Cliente(1, "Juan", "juan@email.com")
    p = Producto(1, "Laptop", 999.99, 5)
    c.agregar_producto(p)
    assert len(c.ver_carrito()) == 1


def test_agregar_producto_sin_stock():
    """Verifica error al agregar producto sin stock."""
    c = Cliente(1, "Juan", "juan@email.com")
    p = Producto(1, "Laptop", 999.99, 0)
    with pytest.raises(ValueError):
        c.agregar_producto(p)


def test_calcular_total():
    """Verifica el cálculo del total del carrito."""
    c = Cliente(1, "Juan", "juan@email.com")
    p1 = Producto(1, "Laptop", 1000.0, 5)
    p2 = Producto(2, "Mouse", 50.0, 3)
    c.agregar_producto(p1)
    c.agregar_producto(p2)
    assert c.calcular_total() == 1050.0


def test_eliminar_producto():
    """Verifica eliminación de producto del carrito."""
    c = Cliente(1, "Juan", "juan@email.com")
    p = Producto(1, "Laptop", 999.99, 5)
    c.agregar_producto(p)
    resultado = c.eliminar_producto(1)
    assert resultado is True
    assert len(c.ver_carrito()) == 0


def test_eliminar_producto_no_existente():
    """Verifica que retorna False si el producto no está en el carrito."""
    c = Cliente(1, "Juan", "juan@email.com")
    resultado = c.eliminar_producto(99)
    assert resultado is False


def test_vaciar_carrito():
    """Verifica que el carrito se vacía correctamente."""
    c = Cliente(1, "Juan", "juan@email.com")
    p1 = Producto(1, "Laptop", 999.99, 5)
    p2 = Producto(2, "Mouse", 29.99, 3)
    c.agregar_producto(p1)
    c.agregar_producto(p2)
    c.vaciar_carrito()
    assert len(c.ver_carrito()) == 0


def test_str_cliente():
    """Verifica representación en cadena del cliente."""
    c = Cliente(1, "Juan Pérez", "juan@email.com")
    resultado = str(c)
    assert "Juan Pérez" in resultado
    assert "juan@email.com" in resultado
