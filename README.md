
# IAC API 🚀  
Sistema de Gestión Empresarial con FastAPI y Supabase

## 📌 Descripción del Proyecto

IAC API es un sistema backend desarrollado para optimizar la gestión interna de la empresa IAC.  
El proyecto nace como solución a las limitaciones del manejo manual de información mediante herramientas ofimáticas tradicionales como Microsoft Office, buscando ofrecer una plataforma más moderna, escalable y eficiente.

El sistema permite administrar:

- Empresas
- Productos
- Servicios

a través de una API REST construida con **FastAPI**, utilizando **Supabase** como sistema de persistencia de datos.

---

# 🚀 Tecnologías Utilizadas

- **Python 3**
- **FastAPI**
- **Supabase**
- **Pydantic**
- **Pytest**
- **Uvicorn**
- **UV Package Manager**
- **Git & GitHub**

---

# 🧱 Arquitectura del Proyecto

El proyecto sigue una arquitectura por capas para mantener una separación clara de responsabilidades y facilitar el mantenimiento del código.

```plaintext
src/
│
├── api/            # Endpoints y routers FastAPI
├── core/           # Configuración, excepciones y utilidades
├── schemas/        # Modelos Pydantic
├── services/       # Lógica de negocio
├── storage/        # Acceso a datos y Supabase
├── tests/          # Tests unitarios e integración
```



# ✨ Características Principales

## ✅ API REST con FastAPI

El sistema expone endpoints RESTful para administrar empresas, productos y servicios.

---

## ✅ Persistencia con Supabase

Toda la información se almacena en una base de datos PostgreSQL administrada mediante Supabase.

---

## ✅ Arquitectura Modular

Separación clara entre:

- Routers
- Schemas
- Services
- Repositories
- Configuración
- Manejo de errores

---

## ✅ Validación de Datos

Uso de **Pydantic** para validar automáticamente:

- tipos de datos
- campos requeridos
- estructuras JSON

---

## ✅ Soft Delete

Los registros no se eliminan físicamente de la base de datos.  
El sistema utiliza el campo:

```plaintext
is_active
```

para desactivar registros de forma segura.

---

## ✅ Manejo Centralizado de Errores

El proyecto implementa excepciones personalizadas para manejar errores de forma uniforme y clara.

Ejemplos:

- Company not found
- Product not found
- Service not found
- Storage errors
- Validation errors

---

## ✅ Testing

Se implementaron:

- Tests unitarios
- Tests de integración

utilizando **Pytest**.

---

# 📡 Endpoints Principales

## 🏢 Companies

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/companies/` | Listar empresas |
| GET | `/companies/{id}` | Obtener empresa por ID |
| POST | `/companies/` | Crear empresa |
| PATCH | `/companies/{id}` | Actualizar empresa |
| DELETE | `/companies/{id}` | Soft delete empresa |

---

## 📦 Products

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/products/` | Listar productos |
| GET | `/products/{id}` | Obtener producto |
| POST | `/products/` | Crear producto |
| PATCH | `/products/{id}` | Actualizar producto |
| DELETE | `/products/{id}` | Soft delete producto |

---

## 🛠️ Services

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/services/` | Listar servicios |
| GET | `/services/{id}` | Obtener servicio |
| POST | `/services/` | Crear servicio |
| PATCH | `/services/{id}` | Actualizar servicio |
| DELETE | `/services/{id}` | Soft delete servicio |

---

# 📖 Documentación Swagger

FastAPI genera automáticamente documentación interactiva.

Disponible en:

```plaintext
http://127.0.0.1:8000/docs
```

Desde Swagger es posible:

- probar endpoints
- enviar requests
- visualizar respuestas
- validar esquemas

---

# ⚙️ Instalación y Ejecución

## 1️⃣ Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
```

---

## 2️⃣ Entrar al proyecto

```bash
cd IAC-2.0
```

---

## 3️⃣ Instalar dependencias

```bash
uv sync
```

---

## 4️⃣ Activar entorno virtual

### Windows

```bash
.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

## 5️⃣ Configurar variables de entorno

Crear un archivo:

```plaintext
.env
```

Ejemplo:

```env
SUPABASE_URL=tu_url
SUPABASE_KEY=tu_key
API_TITLE=IAC API
API_VERSION=1.0.0
```

---

## 6️⃣ Ejecutar el servidor

```bash
uvicorn src.api.main:app --reload
```

---

# 🧪 Ejecutar Tests

```bash
uv run pytest
```

---

# 📁 Estructura de Testing

```plaintext
tests/
│
├── integration/
│   └── test_routers.py
│
├── unit/
│   ├── test_company_service.py
│   ├── test_products_service.py
│   └── test_services_service.py
```

---

# 🔒 Buenas Prácticas Implementadas

- Arquitectura limpia
- Separación de responsabilidades
- Tipado estático
- Validaciones automáticas
- Soft delete
- Manejo de excepciones
- Testing automatizado
- Variables de entorno
- Modularidad
- Código mantenible y escalable

---

# 👨‍💻 Objetivo Académico

Este proyecto fue desarrollado con fines académicos para demostrar la implementación de buenas prácticas de desarrollo backend utilizando Python y FastAPI.

Además, busca servir como base para futuros sistemas empresariales más complejos y escalables.
````
