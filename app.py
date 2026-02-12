import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Configuración de página
st.set_page_config(page_title="ERP Discovery Dashboard", layout="wide")

# ESTILO CSS (Corregido)
st.markdown("""
    <style>
    /* Estilo para las tarjetas de KPI */
    [data-testid="stMetric"] {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 1px solid #e0e0e0;
    }
    /* Estilo para los botones */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #0047AB;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Título Principal
st.title("📊 ERP Discovery & Strategy")
st.subheader("Diagnóstico de Infraestructura y Operaciones")

# --- CONEXIÓN ---
# Asegúrate de tener configurado el secreto 'connections.gsheets' en Streamlit Cloud
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except Exception as e:
    st.error("Error de conexión. Revisa los 'Secrets' en Streamlit Cloud.")
    df = pd.DataFrame() # DataFrame vacío para que no rompa el diseño

# --- DISEÑO TIPO POWER BI (KPIs) ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Registros", len(df))
with col2:
    st.metric("Sectores", "8", "+1")
with col3:
    st.metric("Nivel de Digitalización", "65%", "5%")
with col4:
    st.metric("Estatus", "Activo", "Online")

st.markdown("---")

# --- FORMULARIO DE ENTRADA ---
with st.container():
    st.markdown("### 📝 Nuevo Registro de Cliente")
    with st.form(key="erp_form"):
        c1, c2 = st.columns(2)
        with c1:
            empresa = st.text_input("Nombre de la Empresa")
            sector = st.selectbox("Sector", ["Retail", "Manufactura", "Servicios", "Logística"])
        with c2:
            contacto = st.text_input("Persona de Contacto")
            empleados = st.select_slider("Número de Empleados", options=["1-10", "11-50", "51-200", "200+"])
        
        # Botón de envío
        submit = st.form_submit_button("Guardar Datos")
        
        if submit:
            if empresa:
                # Lógica para guardar (requiere que el Sheet tenga permisos de escritura)
                st.success(f"✅ ¡Datos de {empresa} guardados con éxito!")
                st.balloons()
            else:
                st.warning("Por favor, ingresa al menos el nombre de la empresa.")

# --- VISUALIZACIÓN ---
if not df.empty:
    st.markdown("### 📈 Resumen de Datos")
    st.bar_chart(df.iloc[:, 0:2]) # Muestra las primeras dos columnas como ejemplo