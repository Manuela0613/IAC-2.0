# README del Proyecto

## Descripción

IAC es un sistema de gestión empresarial desarrollado para administrar empresas, productos y servicios mediante una arquitectura fullstack.

El proyecto implementa una API REST construida con FastAPI, una base de datos PostgreSQL gestionada mediante Supabase y una interfaz web desarrollada con Streamlit.

---

## Tecnologías Utilizadas

- Python 3.13
- FastAPI
- Supabase
- PostgreSQL
- Streamlit
- Pydantic
- Pytest
- Ruff
- Radon
- MkDocs Material

---

## Funcionalidades Principales

### Gestión de Empresas

- Crear empresas
- Consultar empresas
- Actualizar información
- Desactivar registros

### Gestión de Productos

- Crear productos
- Consultar productos
- Actualizar inventario
- Desactivar productos

### Gestión de Servicios

- Crear servicios
- Consultar servicios
- Actualizar información
- Desactivar servicios

---

## Arquitectura

El proyecto implementa una arquitectura por capas:

- API
- Services
- Repositories
- Schemas
- Supabase
- Frontend Streamlit

Cada capa tiene responsabilidades claramente definidas para facilitar el mantenimiento y escalabilidad del sistema.