import streamlit as st
import pandas as pd

from api.client import (
    get_products,
    get_products_by_company,
    get_companies,
    create_product,
    update_product,
    delete_product
)

st.title("📦 Gestión de Productos")

companies = get_companies()
products = get_products()

company_map = {
    f"{c['id']} - {c['name']}": c["id"]
    for c in companies
}

# ── Crear producto ───────────────────────────

with st.form("product_form"):

    selected_company = st.selectbox(
        "Empresa",
        list(company_map.keys())
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

        try:

            create_product({
                "company_id": company_map[selected_company],
                "name": name,
                "price": float(price),
                "stock": int(stock)
            })

            st.success(
                "Producto creado correctamente"
            )

            st.rerun()

        except Exception as e:
            st.error(str(e))

# ── Listar productos ─────────────────────────

st.divider()

st.subheader("📋 Productos registrados")

st.dataframe(
    pd.DataFrame(products),
    use_container_width=True
)

# ── Modificar producto ───────────────────────

if products:

    st.divider()

    st.subheader("✏️ Modificar producto")

    product_options = {
        f"{p['id']} - {p['name']}": p
        for p in products
    }

    selected = st.selectbox(
        "Seleccione un producto",
        list(product_options.keys()),
        key="update_product"
    )

    product = product_options[selected]

    with st.form("update_product_form"):

        new_name = st.text_input(
            "Nombre",
            value=product["name"]
        )

        new_price = st.number_input(
            "Precio",
            min_value=0.01,
            value=float(product["price"])
        )

        new_stock = st.number_input(
            "Stock",
            min_value=0,
            value=int(product["stock"])
        )

        submit_update = st.form_submit_button(
            "Actualizar Producto"
        )

if submit_update:

    try:

        data = {
            "name": new_name,
            "price": float(new_price),
            "stock": int(new_stock)
        }

        st.write("ID:", product["id"])
        st.write("DATA:", data)

        result = update_product(
            product["id"],
            data
        )

        st.write("RESPUESTA:", result)

        st.success(
            "Producto actualizado correctamente"
        )

    except Exception as e:
        st.error(str(e))

# ── Eliminar producto ────────────────────────

if products:

    st.divider()

    st.subheader("🗑️ Eliminar producto")

    delete_options = {
        f"{p['id']} - {p['name']}": p["id"]
        for p in products
    }

    selected_delete = st.selectbox(
        "Seleccione un producto",
        list(delete_options.keys()),
        key="delete_product"
    )

    product_id = delete_options[selected_delete]

    if st.button("Eliminar Producto"):

        try:

            delete_product(product_id)

            st.success(
                "Producto eliminado correctamente"
            )

            st.rerun()

        except Exception as e:
            st.error(str(e))

# ── Buscar productos por empresa ─────────────

st.divider()

st.subheader("🔍 Buscar productos por empresa")

selected_company_search = st.selectbox(
    "Seleccione una empresa",
    list(company_map.keys()),
    key="search_products_company"
)

if st.button("Buscar Productos"):

    try:

        company_products = get_products_by_company(
            company_map[selected_company_search]
        )

        if company_products:

            st.dataframe(
                pd.DataFrame(company_products),
                use_container_width=True
            )

        else:

            st.info(
                "No existen productos para esta empresa."
            )

    except Exception as e:
        st.error(str(e))