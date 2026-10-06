import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Car Analysis')

car_data = pd.read_csv('Vehicles_us.csv')  # lendo os dados
hist_button = st.button('Create histogram')  # criando botao

if hist_button:  # se o botao for clicado

    # vai escrever uma mensagem
    st.write('Creating Histogram graphic for car sales dataset')

    # criar histograma
    fig = px.histogram(car_data, x='odometer')

    # exibir um grafico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Create Shatter graph')  # criando botao

if disp_button:  # se o botao for clicado

    # vai escrever uma mensagem
    st.write('Creating shatter Graphic for car sales dataset')

    # criar histograma
    fig = px.scatter(car_data, x='odometer', y='price')

    # exibir um grafico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
