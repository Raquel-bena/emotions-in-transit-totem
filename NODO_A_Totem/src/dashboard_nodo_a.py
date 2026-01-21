import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

st.set_page_config(page_title="EiT - Nodo A", layout="wide")

st.title("🚉 EMOTIONS (IN)TRANSIT | NODO A")
st.write(f"Última actualización: {datetime.now().strftime('%H:%M:%S')}")

# Métricas rápidas
c1, c2, c3 = st.columns(3)
c1.metric("API Tránsito", "Online", "120ms")
c2.metric("API Emociones", "Online", "85ms")
c3.metric("CPU MacBook", "24%", "Estable")

# Gráfica de datos crudos
chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Flujo A', 'Flujo B'])
st.line_chart(chart_data)

# Visualizador de JSON
st.subheader("📦 Raw Data Stream")
st.json({"status": "active", "node": "totem_01", "buffer": "cleared"})

time.sleep(2)
st.rerun()
