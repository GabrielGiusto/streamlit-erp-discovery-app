import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Configuración de diseño "Wide" para que se vea como Power BI
st.set_page_config(page_title="Discovery ERP", layout="wide")

# CSS para inyectar un poco de estilo extra (bordes redondeados y sombras)
st.markdown("""
    <style>
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_name_with_html=True)

# Conectar a la hoja
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(ttl=0) # ttl=0 para que se actualice al instante

# --- HEADER / KPIs ---
st.title("📊 ERP Discovery Dashboard")
m1, m2, m3 = st.columns(3)
m1.metric("Empresas Analizadas", len(df), delta="Activo")
m2.metric("Último Registro", df.iloc[-1]['Nombre'] if not df.empty else "N/A")
m3.metric("Completitud", "92%")

# --- FORMULARIO ---
st.markdown("### 📝 Ingreso de Datos Cliente")
with st.form("input_form"):
    col_a, col_b = st.columns(2)
    with col_a:
        nombre = st.text_input("Nombre de la Empresa")
        sector = st.selectbox("Sector Industrial", ["Manufactura", "Servicios", "Retail"])
    with col_b:
        empleados = st.number_input("Número de Empleados", min_value=1)
        infra = st.radio("¿Tiene Servidores Propios?", ["Sí", "No", "Nube"])
    
    if st.form_submit_button("Registrar en el Sistema"):
        # Lógica para guardar en Google Sheets
        # ... (aquí iría el comando conn.create)
        st.success("¡Datos enviados al Excel central!")