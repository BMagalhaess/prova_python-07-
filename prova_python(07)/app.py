import streamlit as st      
import pandas as pd      
import plotly.express as px 

df = pd.read_excel("saeb_aprendizado_territorios-7-2023-EM.xlsx",
sheet_name="estados", engine="openpyxl")

st.set_page_config(page_title="Prova Final - Gráficos", layout="wide")
st.title("📊 Prova Final")
