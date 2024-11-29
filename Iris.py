import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris


st.set_page_config(
    page_title="Analyse des données Iris",  # Titre de l'onglet
    page_icon="🌸",  # Icône de l'onglet
    layout="wide",  # Mise en page large
    initial_sidebar_state="expanded"  # Optionnel : afficher ou réduire la barre latérale
)

st.sidebar.title("Iris App")
texte_sidebar = st.sidebar.write("Analysons Iris")
button_sidebar = st.sidebar.button("Commençons")


st.title("Analyse de la base de données Iris")
st.write("Cette application analyse quelques données de la base Iris")

iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)


tab__1 , tab__2, tab__3, tab__4, tab__5 = st.tabs(["Base de données", "Premières et dernières lignes", "Filtrage", "Diagrammes", "Courbes"])

with tab__1 :
    st.title("Base de données Iris 🌸")
    st.write("Voici les données de la célèbre base Iris :")
    st.write(data)

with tab__2 :
    st.write("Les 5 premières lignes de la base de données")
    st.write(data.head())  # Affiche les 5 premières lignes
    st.write("Les 5 dernière lignes de la base de données")
    st.write(data.tail())  # Affiche les 5 dernières lignes

with tab__3 :
    filtered_data = data[data['species'] == 'setosa']
    second_filtered_data = data[data['petal length (cm)'] == 1.4]
    st.write("Affichage des informations uniquement pour Setosa")
    st.write(filtered_data)  # Affiche uniquement les observations pour "setosa"
    st.write("Les espèces pour lesquelles la longueur des pétales est égale à 1.4")
    st.write(second_filtered_data)  # Affiche uniquement les observations pour "setosa"

with tab__4 :
    number = data['species'].value_counts()
    st.write("Comptage par espèce")
    st.bar_chart(number)

with tab__5 :
    st.subheader("ANalyse de la longueur des pétales en fonction de l'espèce")
    fig, ax = plt.subplots()
    sns.boxplot(data=data, x='species', y='petal length (cm)', ax=ax, palette="pastel")
    ax.set_title("Longueur des pétales par espèce")
    ax.set_xlabel("Espèce")
    ax.set_ylabel("Longueur des pétales (cm)")
    st.pyplot(fig)










st.write(data.info())


