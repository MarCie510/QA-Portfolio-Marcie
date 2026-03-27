# 🎭 Web UI Automation Portfolio

Framework de automatización de pruebas E2E utilizando **Python** y **Playwright**.
Diseñado con **Page Object Model (POM)** para escalabilidad y mantenimiento.

## 🛠 Tech Stack
- **Lenguaje:** Python
- **Framework:** Playwright
- **Runner:** Pytest
- **Reporting:** Pytest-HTML / Video / Screenshots

## 📂 Estructura del Proyecto
- `pages/`: Objetos de página (POM) con lógica de interacción.
- `tests/`: Scripts de prueba (Happy Paths y Edge Cases).
- `conftest.py` Configuración de Fixtures compartidos.
- `pytest.ini`: Configuración del runner y marcadores.

## 🚀 Setup & Ejecución

1. **Instalar dependencias:**
   ```bash
   pip install pytest pytest-playwright
   playwright install
   ```

2. **Ejecutar Tests:**
   - Todos los tests: `pytest`
   - Smoke tests (Happy Path): `pytest -m smoke`
   - Casos borde (Negativos): `pytest -m edge_case`

## 🧪 Estrategia de Pruebas
Incluye validaciones de:
- ✅ **Happy Path:** Flujos críticos de usuario (Login, Compra, Búsqueda).
- ⚠️ **Edge Cases:** Manejo de errores, inputs inválidos, timeouts.
