import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mplsoccer import Pitch

# Charger les données
df = pd.read_csv("df_Big2025.csv")

# Configuration de l'application
st.title("Visualisation des Heatmaps des Joueurs")

# Filtres de personnalisation
min_minutes = st.slider("Minutes jouées minimum", min_value=0, max_value=int(df["Minutes jouees"].max()), value=500)
selected_leagues = st.multiselect("Sélectionner les ligues", df["Ligue"].unique(), default=df["Ligue"].unique())
num_labels = st.slider("Nombre de joueurs affichés", min_value=1, max_value=20, value=10)
label_size = st.slider("Taille du texte des labels", min_value=5, max_value=20, value=10)

# Filtrage des données
filtered_df = df[(df["Minutes jouees"] >= min_minutes) & (df["Ligue"].isin(selected_leagues))]

# Sélection des joueurs pour comparaison
players = filtered_df["Joueur"].unique()
player1 = st.selectbox("Sélectionner le premier joueur", players)
player2 = st.selectbox("Sélectionner le deuxième joueur", players, index=min(1, len(players)-1))

# Fonction pour générer la heatmap
def draw_heatmap(player_name, ax):
    player_data = filtered_df[filtered_df["Joueur"] == player_name]
    
    # Simuler des coordonnées d'activité (remplacer par des données réelles si disponible)
    x = np.random.uniform(0, 100, size=player_data.shape[0])
    y = np.random.uniform(0, 100, size=player_data.shape[0])
    
    pitch = Pitch(line_color='white', pitch_type='statsbomb', pitch_color='grass', stripe=True)
    pitch.draw(ax=ax)
    
    sns.kdeplot(x=x, y=y, shade=True, cmap="Reds", alpha=0.6, ax=ax)
    ax.set_title(player_name, fontsize=12)

# Affichage des heatmaps
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
draw_heatmap(player1, axes[0])
draw_heatmap(player2, axes[1])
st.pyplot(fig)
