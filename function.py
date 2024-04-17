import streamlit as st
import seaborn as sns
from googletrans import Translator
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

def translate_text(text, target_language='id'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def distribution(df):
    fig, ax = plt.subplots()
    sns.histplot(df['Year of release'].dropna(), bins=20, kde=True, ax=ax)
    plt.title('Distribusi Tahun Rilis Drama Korea')
    plt.xlabel('Tahun Rilis')
    plt.ylabel('Jumlah Drama Korea')
    st.pyplot(fig)

    translate = st.checkbox("Translate to Indonesia")
    text = (""" 
        The visualization above shows the distribution of release years of Korean dramas. This diagram is a horizontal histogram with year of release on the x-axis and the number of Korean dramas released each year on the y-axis.
        Based on the visualization results according to the year of Korean drama release, the Korean drama industry has experienced significant growth in the last few years, namely there was a significant increase after 2010. Based on the visualization above, it can be seen that 2020 and 2022 have the highest number of Korean dramas. released a lot, with a total of 30 and 35 Korean dramas. Followed by 2012 and 2015 which had the same number of dramas, namely 25 Korean dramas. Meanwhile, 2002 had the least number of dramas, namely 5 dramas and this trend shows that Korean dramas are increasingly popular throughout the world. Fluctuations in the number of Korean dramas released each year are likely caused by various factors. In addition, the years 2002, 2005, 2007, and 2010 also showed a slight decrease in the number of Korean dramas released.    
    """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

def comparison(df):
    fig, ax = plt.subplots()
    sns.lineplot(x=df['Year of release'].dropna(), y=df['Rating'].dropna(), ax=ax)
    plt.title('Tren Popularitas Drama Korea')
    plt.xlabel('Tahun Rilis')
    plt.ylabel('Rating')
    st.pyplot(fig)

    translate = st.checkbox("Translate to Indonesia")
    text = (""" 
        The visualization above shows the popularity trend of Korean dramas over several years. This diagram is a horizontal histogram with release year on the x-axis and ratings of Korean dramas released each year on the y-axis.
        Based on the visualization above, we can see that the popularity of Korean dramas continues to increase from 2002 to 2022. This trend shows that Korean dramas are becoming increasingly popular every year.
        From the visualization above, it is found that:

        1. 2016 and 2022 have the highest popularity of Korean dramas, with an average rating of 8.6.
        2. 2015 and 2020 were in second place with an average rating of 8.5.
        3. 2002 had the lowest popularity of Korean dramas, with an average rating of 8.3.
        4. 2003 and 2004 had the same drama popularity, namely with an average rating of 8.4.
            
        By looking at the popularity trend of Korean dramas, we can make decisions about producing or watching Korean dramas with genres that are popular that year.""")
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

def composition(df):
    fig, ax = plt.subplots()
    sns.countplot(y='Rating', data=df, palette='Set2', ax=ax)
    plt.title('Proporsi Rating Drama Korea')
    plt.xlabel('Jumlah Drama Korea')
    plt.ylabel('Rating')
    st.pyplot(fig)

    translate = st.checkbox("Translate to Indonesia")
    text = (""" 
        Based on the visualization above, the following results are obtained.

        1. The distribution of Korean drama ratings is uneven.
        2. There are many Korean dramas with a rating of 8.0 to 8.5.
        3. The number of Korean dramas with ratings of 7.0 and 10.0 is relatively fewer.
        4. There has been an increasing trend in the number of Korean dramas with high ratings (8.5 - 10.0) in recent years. This shows that the overall quality of Korean dramas is increasing.
        5. We can also see that the number of Korean dramas with ratings of 9.1 and 9.0 is quite high, namely 9 and 8 dramas. This shows that Korean dramas with high ratings are still popular today.
        
        By looking at the distribution trend of Korean drama ratings, we can make decisions about producing or watching Korean dramas that are relevant to that rating. This can help us understand trends among our audience and maximize opportunities to take advantage of those trends.
            """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

def relationship(df):
    st.header("The Influence of Release Year on Korean Drama Ratings")
    fig, ax = plt.subplots()
    sns.scatterplot(x='Year of release', y='Rating', data=df, ax=ax)
    plt.title('Pengaruh Tahun Rilis dalam Rating Drama Korea')
    plt.xlabel('Tahun Rilis')
    plt.ylabel('Rating')
    st.pyplot(fig)

    translate = st.checkbox("Translate to Indonesia")
    text = (""" 
        From this visualization, we can see that Korean dramas released in 2017.5 have the highest rating with an average of 8.8. Apart from that, we can also see that Korean dramas released in the years 2015.0, 2017.5, and 2022.5 have a higher average rating compared to other years. This shows that Korean drama producers produced more dramas with higher ratings in those years.
        We can also see that the years 2002.5, 2005.0, 2007.5, and 2010.0 have lower average ratings compared to other years. This shows that Korean drama producers produced fewer dramas with higher ratings in those years.
            """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

    st.header("The Influence of the Number of Episodes on Korean Drama Ratings")
    fig, ax = plt.subplots()
    sns.scatterplot(x='Number of Episodes', y='Rating', data=df, ax=ax)
    plt.title('Pengaruh Jumlah Episode terhadap Rating Drama Korea')
    plt.xlabel('Jumlah Episode')
    plt.ylabel('Rating')
    st.pyplot(fig)

    trans = st.checkbox("Translate to Indonesia (Pengaruh Jumlah Episode)")
    text = (""" 
        From this visualization, we can see that Korean dramas with more episodes do not always have higher ratings. We can see this from the horizontal line which shows the average rating of Korean dramas with a certain number of episodes. The horizontal line shows that Korean dramas with episodes between 10-20 and 30-40 have a high average rating. This shows that Korean dramas with a moderate number of episodes, such as 16 episodes or 32 episodes, have a higher rating compared to Korean dramas with more or fewer episodes.
        In addition, from this visualization we can see that Korean dramas with the number of episodes between 50-60 and 100-120 have a lower average rating. This shows that Korean dramas with more or fewer episodes have higher ratings.
        In this visualization, there are two outliers visible at the number of episodes 100-120 and 50-60. Outliers with a number of episodes of 100-120 have a lower rating compared to other data for that number of episodes. This shows that Korean dramas with a larger number of episodes do not always have higher ratings. Apart from that, outliers with a number of episodes of 50-60 have a higher rating compared to other data for that number of episodes. This shows that Korean dramas with a moderate number of episodes can also have high ratings.
            """)
    if trans:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

def clustering(df):
    st.write("Elbow Plot")
    distortions = []
    K = range(2, 10)
    for k in K:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(df)
        distortions.append(kmeans.inertia_)

    fig, ax = plt.subplots()
    ax.plot(K, distortions, 'bx-')
    ax.set_xlabel('Number of Clusters')
    ax.set_ylabel('Distortion')
    ax.set_title('Elbow Method For Optimal k')
    st.pyplot(fig)


    translate = st.checkbox("Translate to Indonesia")
    text = """
    From the elbow method plot above, we can determine the optimal number of clusters (K) by looking for the "elbow" point, where the inertia starts to decrease at a slower rate. This indicates the point where additional clusters provide diminishing returns in terms of explaining the variance in the data.
    """
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

def clusters(data, labels):
    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots()
        sns.scatterplot(data=data, x='Year of release', y='Rating', hue=labels, palette='viridis', ax=ax)
        ax.set_title('Clustered Data (Year of Release)')
        ax.set_xlabel('Year of Release')
        ax.set_ylabel('Rating')
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots()
        sns.scatterplot(data=data, x='Number of Episodes', y='Rating', hue=labels, palette='viridis', ax=ax)
        ax.set_title('Clustered Data (Number of Episodes)')
        ax.set_xlabel('Number of Episodes')
        ax.set_ylabel('Rating')
        st.pyplot(fig)
