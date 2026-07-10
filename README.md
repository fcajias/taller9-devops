# Taller 9 – GitHub Colaborativo con Fork, Pull Request y GitHub Actions

##  Descripción
Sistema de ventas desarrollado en **Python** como parte del Taller 9 de la materia de DevOps  
Implementa un flujo colaborativo usando **Forks, Branches, Pull Requests y GitHub Actions**

## Integrantes
| Estudiante | GitHub | Rama | Funcionalidad |
|-----------|--------|------|--------------|
| Estudiante 1 | [@fcajias](https://github.com/fcajias) | `feature-fcajias` | Clase `Producto` |
| Estudiante 2 | [@Fernando-Cajias](https://github.com/Fernando-Cajias) | `feature-fernando` | Clase `Cliente` |

##  Estructura del Proyecto
```
taller9-devops/
├── .github/
│   └── workflows/
│       └── build.yml       # GitHub Actions CI
├── src/
│   ├── producto.py         # Clase Producto (Estudiante 1)
│   └── cliente.py          # Clase Cliente (Estudiante 2)
├── tests/
│   ├── test_producto.py    # Tests unitarios Producto
│   └── test_cliente.py     # Tests unitarios Cliente
├── main.py                 # Punto de entrada
├── requirements.txt        # Dependencias Python
└── README.md
```

##  Ejecución Local

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python main.py

# Ejecutar tests
python -m pytest tests/ -v
```

##  GitHub Actions
El workflow `build.yml` se ejecuta automáticamente en cada **push** y **pull request**:
-  Checkout del repositorio
-  Configura Python 3.11
-  Instala dependencias
-  Ejecuta tests con pytest
-  Muestra estado exitoso

## Criterios de Evaluación
- [x] Fork realizado correctamente
- [x] Uso de ramas independientes
- [x] Commits significativos (mín. 3 por estudiante)
- [x] Pull Request creado
- [x] Revisión y aprobación del PR
- [x] GitHub Actions funcionando
