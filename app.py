import plotly.express as px
import streamlit as st
import pandas as pd
import numpy as np

# Carregamento do css


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("assets/dash.css")

# Dataset
# https://www.kaggle.com/datasets/harlfoxem/housesalesprediction

df = pd.read_csv("data/kc_house_data.csv")

# Limpeza de dados
df = df.drop(df[df['bedrooms'] > 30].index)

img = 'https://img.freepik.com/fotos-gratis/foto-aproximada-de-uma-pessoa-pensando-em-comprar-ou-vender-uma-casa_181624-24672.jpg?w=1380&t=st=1675520119~exp=1675520719~hmac=1a35cbac75a6a0e857db43d1bb05811f7e8e09ffe222a2fa39fdd23eae8bf577'

# Header
with st.container():
    st.title("House Sales in King County, USA")
    st.image(img)

    # valor_min = int(df["price"].min())
    # valor_max = int(df["price"].max())

    # values = st.slider(
    #     'Valor para pesquisa das casas',
    #     min_value=valor_min,
    #     max_value=valor_max,
    #     value=(0, valor_max),
    # ),

# Cria o index dos dropdowns
col1, col2, col3 = st.columns(3)

bedrooms = df['bedrooms'].unique()
bedrooms.sort()

with col1:
    selected_bedrooms = st.selectbox(
        label='Quantidade de Quartos',
        options=bedrooms,
    ),

with col2:
    bathrooms = df['bathrooms'][df['bedrooms'] == selected_bedrooms].unique()
    bathrooms.sort()
    selected_bathrooms = st.selectbox(
        label='Quantidade de Banheiros',
        options=bathrooms,
    ),

with col3:
    selected_grade = df['grade'][(df['bedrooms'] == selected_bedrooms) &
                                 (df['bathrooms'] == selected_bathrooms)].unique()
    selected_grade.sort()
    selected_grade = st.selectbox(
        label='Nível de design do imóvel',
        options=selected_grade,
    ),

    # Gráfico para selecionar o preço da casa
    data_mapa = df[["id", "lat", "long", "price",
                    "bedrooms", 'bathrooms', 'grade']]
    data_mapa['price'] = df['price'].astype(int)

with st.container():
    fig4 = px.scatter_mapbox(
        data_mapa[(data_mapa.bedrooms == selected_bedrooms) &
                  (data_mapa.bathrooms == selected_bathrooms) &
                  (data_mapa.grade == selected_grade)],
        lat="lat",
        lon="long",
        hover_data=["id", "price", "bedrooms"],
        color_continuous_scale=px.colors.cyclical.IceFire,
        color='price',
        zoom=8,
        height=500,
        mapbox_style="open-street-map",
        size='price'
    )
    st.plotly_chart(fig4, use_container_width=True)

    tab1, tab2, tab3 = st.tabs(
        ["Quartos(Fig1)", "Banheiros(Fig2)", "Qualidade(Fig3)"])

    with tab1:
        # Gráfico para quantidade de quartos
        df1 = df[df['bedrooms'] == selected_bedrooms]
        fig1 = px.box(
            x=df1['bedrooms'],
            y=df1['price'],
            labels=dict(x='Quartos', y='Preço'),
            title='Preço por quarto')
        st.plotly_chart(fig1, use_container_width=True)

    with tab2:
        # Gráfico para quantidade de banheiros
        df2 = df[df['bedrooms'] == selected_bedrooms]
        fig2 = px.scatter(
            x=df2['bathrooms'],
            y=df2['price'],
            labels=dict(x='Banheiros', y='Preço'),
            title='Variação de preços por banheiros em relação aos quartos selecionados')
        st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        df3 = df[df['grade'] == selected_grade]
        fig3 = px.bar(
            title='Preço por ano de construção e qualidade do imóvel',
            labels=dict(x='Ano de construção',
                        y='Preços'),
            x=df3['yr_built'],
            y=df3['price'],
            color=df3['condition'],
        )
        st.plotly_chart(fig3, use_container_width=True)
