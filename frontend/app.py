import streamlit as st

from api.client import (
    get_companies,
    get_products,
    get_services
)

st.set_page_config(
    page_title="IAC",
    page_icon="",
    layout="wide"
)


st.markdown("""
<style>

/* Ocultar elementos Streamlit */
header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0F172A 0%,
        #020617 100%
    );
}

[data-testid="stSidebar"] * {
    color: white;
}

/* Centrar contenido principal */
.block-container {
    max-width: 1200px;
    margin: auto;
    padding-top: 2rem;
}

/* Título principal */
.main-title {
    text-align: center;
    font-size: 4rem;
    font-weight: 800;
    color: #2563EB;
    margin-bottom: 0;
}

/* Subtítulo */
.sub-title {
    text-align: center;
    font-size: 1.4rem;
    color: #64748B;
    margin-bottom: 40px;
}

/* Texto centrado */
.center-text {
    text-align: center;
    font-size: 18px;
}

/* Secciones */
.section-title {
    font-size: 2rem;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)



with st.sidebar:

    st.markdown("""
    <h1 style='text-align:center; color:white;'>
     IAC 
    </h1>

    <p style='text-align:center; color:#CBD5E1;'>
    Panel Administrativo
    </p>

    <hr>
    """, unsafe_allow_html=True)



st.markdown("""
<div style="text-align:center;">

<img
src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
width="120">

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-title">
IAC 
</div>

<div class="sub-title">
Sistema de Gestión Empresarial
</div>
""", unsafe_allow_html=True)



st.markdown("""
<div class="center-text">

Bienvenido al panel administrativo de <b>IAC</b>.

Desde esta plataforma podrá administrar la información principal de la empresa,
manteniendo actualizado el catálogo de empresas, productos y servicios.

</div>
""", unsafe_allow_html=True)

st.write("")


try:

    companies = get_companies()
    products = get_products()
    services = get_services()

    st.markdown(
        "<h2 style='text-align:center;'>📊 Resumen General</h2>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🏢 Empresas",
            len(companies)
        )

    with col2:
        st.metric(
            "📦 Productos",
            len(products)
        )

    with col3:
        st.metric(
            "🛠 Servicios",
            len(services)
        )

except Exception:

    st.warning(
        "No fue posible conectar con la API."
    )



st.divider()

st.markdown(
    "<h2 style='text-align:center;'>⚙️ Funcionalidades Disponibles</h2>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.info("""
### 🏢 Gestión de Empresas

- Crear empresas
- Consultar información
- Actualizar registros
- Desactivar empresas
""")

    st.info("""
### 📦 Gestión de Productos

- Registrar productos
- Actualizar inventario
- Consultar catálogo
- Desactivar productos
""")

with col2:

    st.info("""
### 🛠 Gestión de Servicios

- Registrar servicios
- Modificar información
- Consultar catálogo
- Desactivar servicios
""")

    st.info("""
### 🔍 Consultas Rápidas

- Buscar productos por empresa
- Buscar servicios por empresa
- Visualizar registros activos
""")

st.divider()

st.markdown(
    "<h2 style='text-align:center;'>📋 Información del Sistema</h2>",
    unsafe_allow_html=True
)

st.success("""
El sistema utiliza **Soft Delete** para preservar la información histórica.
Los registros desactivados permanecen almacenados de forma segura en la base de datos.
""")

st.info("""
### Tecnologías Implementadas

- FastAPI
- Supabase
- Pydantic
- Pytest
- Streamlit
- Python
""")

st.markdown("""
### Recomendaciones para el Administrador

- Mantenga actualizados los datos de las empresas.
- Verifique periódicamente el inventario de productos.
- Revise la información de los servicios registrados.
- Utilice el menú lateral para acceder a cada módulo del sistema.
""")