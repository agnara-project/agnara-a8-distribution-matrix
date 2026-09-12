# Agnara 0.1.0a8 Distribution Matrix

Este repositorio contiene la validación exclusiva (desde fuera del monorepo) de las 7 distribuciones de la versión `0.1.0a8` de Agnara. Su propósito principal es asegurar que los paquetes se instalan limpiamente desde PyPI sin depender de repositorios Git, instalaciones editables, o paths locales, y documentar la superficie de API pública expuesta.

## Objetivo
Validar que las 7 distribuciones de `0.1.0a8` se instalan de forma aislada, que exponen únicamente superficies públicas coherentes y que la instalación sea reproducible en una matriz de sistemas operativos.

## Estructura
- `pyproject.toml`: Define el proyecto de validación con dependencias estrictas (`==0.1.0a8`) apuntando a PyPI.
- `tests/test_distributions.py`: Casos de prueba (`pytest`) que verifican la presencia de los paquetes, sus versiones y la superficie pública de API (especialmente confirmando que `agnara_a2a` y `agnara_events` son namespaces reservados vacíos).
- `src/example.py`: Un ejecutable mínimo que demuestra la instanciación de las distribuciones, revelando el "gap" o comportamiento real documentado.
- `.github/workflows/ci.yml`: Matriz de instalación limpia (Linux, Windows, macOS) usando un entorno virtual (`venv`) nuevo.

---

## Release validation

### Información de Versión
- **Versión de Agnara:** `0.1.0a8`
- **Requisito de Python:** `>=3.14`
- **Fuente de instalación:** PyPI

### Paquetes Instalados
La validación engloba las siguientes distribuciones, fijadas a sus versiones exactas:
1. `agnara==0.1.0a8`
2. `agnara-a2a==0.1.0a8`
3. `agnara-cli==0.1.0a8`
4. `agnara-events==0.1.0a8`
5. `agnara-http==0.1.0a8`
6. `agnara-mcp==0.1.0a8`
7. `agnara-telemetry==0.1.0a8`

### Comandos Reproducibles

Para recrear el entorno de validación (requiere Python 3.14):

```bash
# Crear un entorno limpio
python -m venv venv
source venv/bin/activate # En Windows: venv\Scripts\activate

# Actualizar pip e instalar distribuciones exactas
python -m pip install --upgrade pip
pip install agnara==0.1.0a8 agnara-a2a==0.1.0a8 agnara-cli==0.1.0a8 agnara-events==0.1.0a8 agnara-http==0.1.0a8 agnara-mcp==0.1.0a8 agnara-telemetry==0.1.0a8

# Ejecutar pruebas y demostración de API
pip install pytest
pytest tests/
python src/example.py
```

### Hallazgos y Limitaciones (Gaps en la API)

Durante la validación de la superficie pública, se ha detectado y documentado el estado real (sin simulaciones ni suposiciones) de las extensiones `agnara-a2a` y `agnara-events` en la versión `0.1.0a8`:

1. **agnara_a2a**: La distribución se instala correctamente desde PyPI, pero actúa exclusivamente como un *namespace* reservado para el trabajo Post-v0.1. El archivo principal expone de manera intencional una superficie pública vacía (`__all__ = []`) y no contiene APIs funcionales (ej. adaptadores, tareas o binding de protocolos).
2. **agnara_events**: Similar al paquete A2A, se instala exitosamente pero sólo reserva la frontera del paquete para abstracciones de exposición de eventos. Expresa explícitamente `__all__ = []`.
3. **Ausencia de Importaciones Namespace (agnara.events / agnara.a2a)**: No es posible importar desde `agnara.events` ni `agnara.a2a`. Los paquetes se instalan como módulos *top-level* (`agnara_a2a` y `agnara_events`). Intentar importar, por ejemplo, `from agnara.events import Broker` resulta en un `ImportError`.

El proyecto comprueba esta situación programáticamente en `tests/test_distributions.py` y genera un caso de uso mínimo en `src/example.py` que captura las excepciones reales. No se ha intentado ocultar, "mockear" ni inventar APIs para estas librerías. Todo el ecosistema ha sido congelado exitosamente contra `0.1.0a8`.