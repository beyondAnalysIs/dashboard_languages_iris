import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# configuración de la pagina
st.set_page_config(
    page_title="Dashboard", 
    page_icon = '📊',
    layout="wide" # ocupa el ancho de la ventana
)

# titulo principal
st.title('📊 Visualización de Datos')
st.markdown('### Análisis de bibliotecas y visualización en Python')

# introducción
with st.expander('📝 Introducción', expanded=True):# with permite trabajar con texto
    st.markdown('''
    Esta aplicación demuestra el uso de diferentes bibliotecas de visualización en Python:
    * **Matplotlib**: Biblioteca base para la visualización
    * **Seaborn**: Visualizaciones estadísticas de alto nivel
    * **Plotly**: Gráficos interactivos
    * **Streamlit**: Framework para aplicaciones de datos 
    ''')
    
try:
    prod_df = pd.read_csv('languages.csv')
    iris_df = pd.read_excel('iris_dataset.xlsx')
    st.success('✅ Datos cargados exitosamente')
    
    # visualización con  matplotlib
    st.header('🎨 Visualizaciones con Matplotlib')

    with st.container():
        col1,col2 = st.columns(2)
        with col1:
            st.subheader('Gráfico de Dispersión')
        with col2:
            st.subheader('Grafico de Barras')


except Exception as e:
    st.error(f'❌ Error al cargar los datos: {str(e)}')
    st.error('Por favor, verifica que los archivos existan en la carpeta y tengan el formato adecuado')