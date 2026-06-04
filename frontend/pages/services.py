import streamlit as st
import pandas as pd

from api.client import (
    get_services,
    get_services_by_company,
    get_companies,
    create_service,
    update_service,
    delete_service
)

st.title("🛠 Gestión de Servicios")

companies = get_companies()
services = get_services()

company_map = {
    f"{c['id']} - {c['name']}": c["id"]
    for c in companies
}

# ── Crear servicio ───────────────────────────

with st.form("service_form"):

    selected_company = st.selectbox(
        "Empresa",
        list(company_map.keys())
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

        try:

            create_service({
                "company_id": company_map[selected_company],
                "name": name,
                "description": description,
                "price": float(price)
            })

            st.success(
                "Servicio creado correctamente"
            )

            st.rerun()

        except Exception as e:
            st.error(str(e))

# ── Listar servicios ─────────────────────────

st.divider()

st.subheader("📋 Servicios registrados")

st.dataframe(
    pd.DataFrame(services),
    use_container_width=True
)

# ── Modificar servicio ───────────────────────

if services:

    st.divider()

    st.subheader("✏️ Modificar servicio")

    service_options = {
        f"{s['id']} - {s['name']}": s
        for s in services
    }

    selected = st.selectbox(
        "Seleccione un servicio",
        list(service_options.keys()),
        key="update_service"
    )

    service = service_options[selected]

    with st.form("update_service_form"):

        new_name = st.text_input(
            "Nombre",
            value=service["name"]
        )

        new_description = st.text_area(
            "Descripción",
            value=service["description"]
        )

        new_price = st.number_input(
            "Precio",
            min_value=0.01,
            value=float(service["price"])
        )

        submit_update = st.form_submit_button(
            "Actualizar Servicio"
        )

        if submit_update:

            try:

                update_service(
                    service["id"],
                    {
                        "name": new_name,
                        "description": new_description,
                        "price": float(new_price)
                    }
                )

                st.success(
                    "Servicio actualizado correctamente"
                )

                st.rerun()

            except Exception as e:
                st.error(str(e))

# ── Eliminar servicio ────────────────────────

if services:

    st.divider()

    st.subheader("🗑️ Eliminar servicio")

    delete_options = {
        f"{s['id']} - {s['name']}": s["id"]
        for s in services
    }

    selected_delete = st.selectbox(
        "Seleccione un servicio",
        list(delete_options.keys()),
        key="delete_service"
    )

    service_id = delete_options[selected_delete]

    if st.button("Eliminar Servicio"):

        try:

            delete_service(service_id)

            st.success(
                "Servicio eliminado correctamente"
            )

            st.rerun()

        except Exception as e:
            st.error(str(e))

# ── Buscar servicios por empresa ─────────────

st.divider()

st.subheader("🔍 Buscar servicios por empresa")

selected_company_search = st.selectbox(
    "Seleccione una empresa",
    list(company_map.keys()),
    key="search_services_company"
)

if st.button("Buscar Servicios"):

    try:

        company_services = get_services_by_company(
            company_map[selected_company_search]
        )

        if company_services:

            st.dataframe(
                pd.DataFrame(company_services),
                use_container_width=True
            )

        else:

            st.info(
                "No existen servicios para esta empresa."
            )

    except Exception as e:
        st.error(str(e))