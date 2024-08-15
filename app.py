import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV en un DataFrame
@st.cache
def load_data():
    ruta_completa = '/Users/camilomorales/Mi-proyecto-6/vehicles_us.csv'
    return pd.read_csv(ruta_completa)

car_data = load_data()

# Crear el contenido de la aplicación
st.header('Explorador de Datos de Vehículos')

# Botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button:
    # Escribir un mensaje en la interfaz
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma con Plotly Express
    fig_hist = px.histogram(car_data, x="odometer", title="Histograma de Odometer")

    # Mostrar el gráfico Plotly interactivo en la aplicación
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    # Escribir un mensaje en la interfaz
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión con Plotly Express
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersión: Odometer vs Price")

    # Mostrar el gráfico Plotly interactivo en la aplicación
    st.plotly_chart(fig_scatter, use_container_width=True)