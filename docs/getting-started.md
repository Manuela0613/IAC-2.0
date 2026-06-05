# Instalación y Ejecución

## Requisitos

Antes de ejecutar el proyecto es necesario contar con:

* Python 3.13
* UV Package Manager
* Git
* Cuenta de Supabase

---

## Clonar el repositorio

```bash
git clone https://github.com/Manuela0613/IAC-2.0.git
```

```bash
cd IAC
```

---

## Crear entorno virtual

```bash
uv venv --python 3.13
```

---

## Activar entorno virtual

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

## Instalar dependencias

```bash
uv sync
```

---

## Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto.

Ejemplo:

```env
SUPABASE_URL=url_supabase
SUPABASE_KEY=key_supabase
API_TITLE=IAC API
API_VERSION=1.0.0
```

---

# Ejecución del Backend

Iniciar el servidor FastAPI:

```bash
uv run uvicorn src.api.main:app --reload
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

---

## Documentación Automática

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# Ejecución del Frontend

Abrir una segunda terminal y activar nuevamente el entorno virtual:

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Ejecutar la aplicación Streamlit:

```bash
uv run streamlit run frontend/app.py
```

La interfaz web estará disponible en:

```text
http://localhost:8501
```

---

# Ejecución de Pruebas

Para ejecutar las pruebas automatizadas:

```bash
uv run pytest
```

---

# Validación de Calidad de Código

## Ruff

Analiza estilo y buenas prácticas:

```bash
uv run ruff check .
```

## Radon

Analiza complejidad ciclomática:

```bash
radon cc src -a
```

Resultado obtenido en el proyecto:

```text
Average complexity: A (1.98)
```

---

# Arquitectura Tecnológica

El sistema está compuesto por tres capas principales:

### Frontend

* Streamlit
* Interfaz gráfica para el administrador

### Backend

* FastAPI
* API REST
* Validación mediante Pydantic

### Base de Datos

* PostgreSQL
* Supabase
* Persistencia de empresas, productos y servicios
