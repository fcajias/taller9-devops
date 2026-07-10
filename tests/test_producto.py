"""Tests para la clase Producto."""
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.producto import Producto


def test_crear_producto():
    """Verifica que un producto se crea correctamente."""
    p = Producto(1, "Laptop", 999.99, 10)
    assert p.id == 1
    assert p.nombre == "Laptop"
    assert p.precio == 999.99
    assert p.stock == 10


def test_aplicar_descuento():
    """Verifica que el descuento se aplica correctamente."""
    p = Producto(1, "Laptop", 1000.0, 5)
    precio_con_descuento = p.aplicar_descuento(10)
    assert precio_con_descuento == 900.0


def test_aplicar_descuento_invalido():
    """Verifica que se lanza error con porcentaje inválido."""
    p = Producto(1, "Laptop", 1000.0, 5)
    with pytest.raises(ValueError):
        p.aplicar_descuento(110)


def test_actualizar_stock():
    """Verifica la actualización de stock."""
    p = Producto(1, "Laptop", 999.99, 10)
    p.actualizar_stock(5)
    assert p.stock == 15


def test_stock_insuficiente():
    """Verifica que no se permite stock negativo."""
    p = Producto(1, "Laptop", 999.99, 2)
    with pytest.raises(ValueError):
        p.actualizar_stock(-5)


def test_esta_disponible():
    """Verifica disponibilidad del producto."""
    p_con_stock = Producto(1, "Laptop", 999.99, 5)
    p_sin_stock = Producto(2, "Mouse", 29.99, 0)
    assert p_con_stock.esta_disponible() is True
    assert p_sin_stock.esta_disponible() is False


def test_str_producto():
    """Verifica representación en cadena."""
    p = Producto(1, "Laptop", 999.99, 5)
    resultado = str(p)
    assert "Laptop" in resultado
    assert "999.99" in resultado


def test_to_dict():
    """Verifica serialización a diccionario."""
    p = Producto(1, "Laptop", 999.99, 5)
    d = p.to_dict()
    assert d["id"] == 1
    assert d["nombre"] == "Laptop"
    assert d["precio"] == 999.99
    assert d["disponible"] is True


def test_from_dict():
    """Verifica creación de Producto desde diccionario."""
    data = {"id": 2, "nombre": "Mouse", "precio": 35.50, "stock": 10}
    p = Producto.from_dict(data)
    assert p.id == 2
    assert p.nombre == "Mouse"
    assert p.precio == 35.50


def test_precio_negativo():
    """Verifica que no se permite precio negativo."""
    with pytest.raises(ValueError):
        Producto(1, "Laptop", -100.0, 5)

