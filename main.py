import streamlit as st
import pandas as pd

from streamlit_option_menu import *
from function import *

st.title("Analisis Preferensi Penonton Drama Korea")

with st.sidebar :
    selected = option_menu('Drama Korea',['Introducing', 'Distribution', 'Relationship', 'Comparison', 'Composition', 'Clustering'],default_index=0)

if (selected == 'Introducing'):
    st.title("Introducing")
    text = ("""
    Korean Drama is a drama from South Korea which is popular throughout the world. Korean dramas have their own characteristics, such as actors' styles, music, themes and unique acting styles. This is a factor that influences the influence of Korean dramas throughout the world. The influence of Korean dramas is the impact that Korean dramas have on individuals, society and culture in various regions and countries around the world. This influence can occur in various forms and dimensions, such as cultural, marketing, social and educational influences.
    """)
    translate = st.checkbox("Translate to Indonesia")
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

    st.header("Data Drama Korea")
    df = pd.read_csv('kdrama.csv')
    st.write(df)

if (selected == 'Distribution'):
    st.header("Distribution")
    df = pd.read_csv('Before Mapping.csv')
    distribution(df)

if (selected == 'Relationship'):
    st.title("Relationship")
    df = pd.read_csv('Before Mapping.csv')
    relationship(df)

if (selected == 'Comparison'):
    st.title("Comparison")
    df = pd.read_csv('Before Mapping.csv')
    comparison(df)

if (selected == 'Composition'):
    st.title("Composition")
    df = pd.read_csv('Before Mapping.csv')
    composition(df)

if (selected == 'Clustering'):
    st.title("Clustering")
    df = pd.read_csv('Data Cleaned (1).csv')
    clustering(df)

    n_clusters = st.sidebar.slider("Select Number of Clusters", 3, 4, 5)
    kmeans_model = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans_model.fit_predict(df)

    df['Cluster'] = cluster_labels

    st.write("Data with Cluster Labels:")
    st.write(df)

    clusters(df, cluster_labels)
    
    st.subheader("Kesimpulan")
    translate = st.checkbox("Translate to Indonesia (Kesimpulan)")
    text = (""" 
    Based on the analysis, it can be concluded that Korean dramas experienced an increasing trend in popularity from 2002 to 2022, with peak popularity occurring in 2016 and 2022. Certain years, such as 2017.5, showed higher average ratings, while some other years had lower rating. Although there is no direct correlation, dramas with a moderate number of episodes tend to have higher ratings than those that are too long or too short. Understanding these trends can help in making decisions regarding the production and selection of Korean dramas that are more in line with audience preferences.
        """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

    