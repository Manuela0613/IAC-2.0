import streamlit as st
import pandas as pd

from api.client import (
    get_companies,
    create_company,
    update_company,
    delete_company
)

st.title("🏢 Gestión de Empresas")

# ── Crear empresa ─────────────────────────────

with st.form("company_form"):

    name = st.text_input(
        "Nombre de la empresa"
    )

    nit = st.text_input(
        "NIT"
    )

    submit = st.form_submit_button(
        "Crear Empresa"
    )

    if submit:

        try:

            create_company({
                "name": name,
                "nit": nit
            })

            st.success(
                "Empresa creada correctamente"
            )

            st.rerun()

        except Exception as e:
            st.error(str(e))

# ── Listar empresas ───────────────────────────

st.divider()

companies = get_companies()

st.subheader("📋 Empresas registradas")

st.dataframe(
    pd.DataFrame(companies),
    use_container_width=True
)

# ── Modificar empresa ─────────────────────────

if companies:

    st.divider()

    st.subheader("✏️ Modificar empresa")

    company_options = {
        f"{c['id']} - {c['name']}": c
        for c in companies
    }

    selected = st.selectbox(
        "Seleccione una empresa",
        list(company_options.keys()),
        key="update_company"
    )

    company = company_options[selected]

    with st.form("update_company_form"):

        new_name = st.text_input(
            "Nombre",
            value=company["name"]
        )

        new_nit = st.text_input(
            "NIT",
            value=company["nit"]
        )

        submit_update = st.form_submit_button(
            "Actualizar Empresa"
        )

        if submit_update:

            try:

                update_company(
                    company["id"],
                    {
                        "name": new_name,
                        "nit": new_nit
                    }
                )

                st.success(
                    "Empresa actualizada correctamente"
                )

                st.rerun()

            except Exception as e:
                st.error(str(e))

# ── Eliminar empresa ──────────────────────────

if companies:

    st.divider()

    st.subheader("🗑️ Eliminar empresa")

    delete_options = {
        f"{c['id']} - {c['name']}": c["id"]
        for c in companies
    }

    selected_delete = st.selectbox(
        "Seleccione una empresa",
        list(delete_options.keys()),
        key="delete_company"
    )

    company_id = delete_options[selected_delete]

    if st.button("Eliminar Empresa"):

        try:

            delete_company(company_id)

            st.success(
                "Empresa eliminada correctamente"
            )

            st.rerun()

        except Exception as e:
            st.error(str(e))
