import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV en un DataFrame
@st.cache
def load_data():
    ruta_completa = '/Users/camilomorales/Mi-proyecto-6/vehicles_us.csv'
    return pd.read_csv(ruta_completa)

car_data = load_data()


st.header('Explorador de Datos de Vehículos')


hist_button = st.button('Construir histograma')

if hist_button:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma con Plotly Express
    fig = px.histogram(car_data, x="odometer", title="Histograma de Odometer")

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)