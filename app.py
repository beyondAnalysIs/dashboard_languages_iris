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
        
        with st.container():
            col1,col2 = st.columns(2)
        
        with col1:
            st.subheader('Gráfico de Dispersión')
            fig, ax = plt.subplots(figsize=(8,6))
            languages = prod_df['title'].head(10)
            popularity = prod_df['language_rank'].sort_values(ascending=False).head(10)
            ax.scatter(languages, popularity, color= 'blue', alpha= 0.6, )
            plt.xticks(rotation = 45)
            plt.title('Popularidad de Lenguajes de Programación')
            plt.xlabel('Lenguaje')
            plt.ylabel('Popularidad')
            st.pyplot(fig)
            plt.close()

        with col2:
            st.subheader('Grafico de Barras')
            fig, ax = plt.subplots(figsize=(8,6))
            languages_col_2 = prod_df['title'].head(10)
            popularity_col_2 = prod_df['number_of_users'].sort_values(ascending=False).head(10)    
            ax.bar(languages_col_2, popularity_col_2, color='skyblue')
            plt.xticks(rotation=45)
            plt.title('Top 10 de Lenguages con más Usuarios')            
            plt.xlabel('Lenguaje')
            plt.ylabel('Cantidad de Usuarios')
            plt.ylim(0,8000000)
            st.pyplot(fig)
            plt.close()        
            
    # Visualización con Seaborn
    st.header('🎨 Visualización con Seaborn')      
    with st.container():
        col1,col2 = st.columns(2) 
        
        with col1:
            st.subheader('Gráfico de Violín')
            fig, ax = plt.subplots(figsize=(8,6))
            sns.violinplot(data=iris_df, x='species', y='sepal_length')
            plt.xticks(rotation=45)
            plt.title('Longitud del Sépalo por Especie')
            st.pyplot(fig)
            plt.close()           
            
        with col2:
            st.subheader('Gráfico de cajas')
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.boxplot(data= iris_df, x='species', y='sepal_length')
            plt.xticks(rotation=45)
            plt.title('Estadística de Longitud de Pétalo por Especie')
            st.pyplot(fig)
            plt.close()
    
    # Visualización con Plotly
    st.header('🎇 Visualización con Plotly')
    with st.container(): 
        
        # Grafico lineal
        top_10_df = prod_df.sort_values('number_of_users',ascending=False).head(10)
        fig = px.line(top_10_df,
                        x='title',
                        y='number_of_users',
                        title='Tendencia de Popularidad',
                        markers=True)
        st.plotly_chart(fig, use_container_width=True)
        
        # Gráfico de pastel
        fig = px.pie(top_10_df,
                        names='title',
                        values='number_of_users',
                        title='Distribución de Popularidad',
                        hole=0.2)
        st.plotly_chart(fig, use_container_width=True)
    
    # Sección Interactiva
    st.header('🛠 Sección Interactiva')
    
    # Selector de Dataset
    dataset_choice = st.radio(
        'Selecciona el conjunto de datos',
        ['Lenguajes de Programación', 'Iris Dataset']
    )
    
    if dataset_choice == 'Lenguajes de Programación':
        df = prod_df.head(15)    
    else:
        df = iris_df.head(10)
    
    # Selector de visualización
    chart_type= st.selectbox(
        'Selecciona el tipo de Gráfico',
        ['Barras', 'Dispersión', 'Línea']
    )

    # Selector de Datos
    x_axis = st.selectbox('Selecciona el eje X', df.columns)
    y_axis = st.selectbox('Selecciona el eje Y', df.columns)
    
    # Generar el gráfico seleccionado
    if chart_type=='Barras':
        fig = px.bar(df, x=x_axis, y=y_axis, title=f'{chart_type}')
    elif chart_type == 'Dispersión':
        fig = px.scatter(df, x=x_axis, y=y_axis, title=f'{chart_type}')
    else:
        fig = px.line(df, x=x_axis, y=y_axis, title=f'{chart_type}')

    # gráfica
    st.plotly_chart(fig, use_container_width=True)
    
except Exception as e:
    st.error(f'❌ Error al cargar los datos: {str(e)}')
    st.error('Por favor, verifica que los archivos existan en la carpeta y tengan el formato adecuado')
    
    
    

