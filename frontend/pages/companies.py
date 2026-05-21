import streamlit as st
import pandas as pd

from api.client import (
    get_companies,
    create_company
)

st.title("🏢 Gestión de Empresas")

with st.form("company_form"):

    name = st.text_input("Nombre de la empresa")

    nit = st.text_input(
        "NIT",
        help="Solo números"
    )

    submit = st.form_submit_button(
        "Crear Empresa"
    )

    if submit:

        data = {
            "name": name,
            "nit": nit
        }

        try:

            create_company(data)

            st.success(
                "Empresa creada correctamente"
            )

            st.rerun()

        except Exception as e:
            st.error(str(e))

st.divider()

companies = get_companies()

st.dataframe(
    pd.DataFrame(companies),
    use_container_width=True
)