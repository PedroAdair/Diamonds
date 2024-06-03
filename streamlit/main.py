import streamlit as st
from func import *
import plotly.express as px

st.set_page_config(
page_title = 'Diamantes',
page_icon = 'Active',
layout = 'wide',
)
st.image("streamlit\diamond.png")

st.title('Diamantes')
st.markdown('<style>div.block-container{padding-top:1rem}</style>',unsafe_allow_html=True)
tabs = st.tabs([
    'Visualizacion de datos'
])

##############################################
df = load_data()
with tabs[0]:
    st.text(mensaje())
    col1, col2 = st.columns((2))
    with col1:
        st.subheader("Datos limpios")
        st.dataframe(df)

    with col2:
        st.subheader("Datos Faltantes")
        st.text("Se encontraron ")
        datosf = datosFaltantes()
        st.dataframe(datosf)
    col3, col4 = st.columns((2))
    with col3: 
        fig = px.scatter(df, x="carat", y="price", color="Color_num", title="Carat vs Precio por Color",
                 labels={"carat": "Carat", "price": "Precio", "Color_num": "Color"})
        st.plotly_chart(fig)
    
    with col4:
        fig = px.scatter(df, x="x", y="y", color="price", 
                        size='carat', hover_data=['Cut_num', 'Clarity_num'],
                        labels={"x": "Length (mm)", "y": "Width (mm)", "price": "Precio"},
                        title="Dispersión de Diamantes por Precio")
        st.plotly_chart(fig)

    col5, col6 = st.columns((2))