import streamlit as st
import pandas as pd

from api.client import (
    get_services,
    create_service
)

st.title("🛠 Gestión de Servicios")

with st.form("service_form"):

    company_id = st.number_input(
        "ID Empresa",
        min_value=1,
        step=1
    )

    name = st.text_input(
        "Nombre del servicio"
    )

    description = st.text_area(
        "Descripción"
    )

    price = st.number_input(
        "Precio",
        min_value=0.01,
        step=0.01
    )

    submit = st.form_submit_button(
        "Crear Servicio"
    )

    if submit:

        data = {
            "company_id": int(company_id),
            "name": name,
            "description": description,
            "price": float(price)
        }

        try:

            create_service(data)

            st.success(
                "Servicio creado correctamente"
            )

            st.rerun()

        except Exception as e:
            st.error(str(e))

st.divider()

services = get_services()

st.dataframe(
    pd.DataFrame(services),
    use_container_width=True
)