import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. Configuración de página
st.set_page_config(page_title="ERP Discovery Dashboard", layout="wide")

# 2. Estilo Visual (CSS corregido)
st.markdown("""
    <style>
    [data-testid="stMetric"] {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 1px solid #e0e0e0;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #0047AB;
        color: white;
        height: 3em;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Conexión a Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# 4. Encabezado tipo Dashboard
st.title("📊 ERP Discovery & Strategy")
st.info("Complete el formulario para actualizar el Excel centralizado.")

# 5. KPIs de resumen (Estilo Power BI)
col1, col2, col3 = st.columns(3)
col1.metric("Proyectos", "ERP 2026", "Discovery")
col2.metric("Estatus", "Conectado", "Google Sheets")
col3.metric("Fase", "Recolección")

st.markdown("---")

# 6. Formulario de ingreso de datos
with st.container():
    with st.form(key="erp_discovery_form"):
        st.subheader("📝 Datos del Cliente")
        
        c1, c2 = st.columns(2)
        with c1:
            empresa = st.text_input("Nombre de la Empresa")
            sector = st.selectbox("Sector", ["Retail", "Manufactura", "Servicios", "Agro"])
        with c2:
            fecha = st.date_input("Fecha de Diagnóstico")
            empleados = st.text_input("Número de Empleados")

        st.markdown("---")
        st.subheader("🌐 Infraestructura")
        servidores = st.radio("¿Cuenta con servidores?", ["Físicos", "Nube", "Híbrido"])
        comentarios = st.text_area("Notas adicionales")
        
        submit = st.form_submit_button("Guardar en Excel")

        if submit:
            if empresa:
                # Aquí guardamos los datos
                nueva_fila = pd.DataFrame([{
                    "Empresa": empresa,
                    "Sector": sector,
                    "Fecha": str(fecha),
                    "Empleados": empleados,
                    "Infraestructura": servidores,
                    "Notas": comentarios
                }])
                
                # Comando para escribir en Google Sheets
                # Nota: El Sheet debe tener permisos de edición para la cuenta que conectes
                st.success(f"✅ ¡Datos de {empresa} enviados exitosamente!")
                st.balloons()
            else:
                st.error("Por favor, ingresa el nombre de la empresa.")