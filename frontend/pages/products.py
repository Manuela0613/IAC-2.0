import streamlit as st
import pandas as pd

from api.client import (
    get_products,
    create_product
)

st.title("📦 Gestión de Productos")

with st.form("product_form"):

    company_id = st.number_input(
        "ID Empresa",
        min_value=1,
        step=1
    )

    name = st.text_input(
        "Nombre del producto"
    )

    price = st.number_input(
        "Precio",
        min_value=0.01,
        step=0.01
    )

    stock = st.number_input(
        "Stock",
        min_value=0,
        step=1
    )

    submit = st.form_submit_button(
        "Crear Producto"
    )

    if submit:

        data = {
            "company_id": int(company_id),
            "name": name,
            "price": float(price),
            "stock": int(stock)
        }

        try:

            create_product(data)

            st.success(
                "Producto creado correctamente"
            )

            st.rerun()

        except Exception as e:
            st.error(str(e))

st.divider()

products = get_products()

st.dataframe(
    pd.DataFrame(products),
    use_container_width=True
)