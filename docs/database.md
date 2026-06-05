# Base de Datos

## Entidades

### Company

- id
- name
- nit
- is_active

### Product

- id
- company_id
- name
- price
- stock
- is_active

### Service

- id
- company_id
- name
- description
- price
- is_active

## Relaciones

Company 1 → N Product

Company 1 → N Service