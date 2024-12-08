# Manipulation de données et création de graphiques

Ce projet est une application Streamlit qui permet de manipuler des datasets, de visualiser des graphiques interactifs, et d'analyser la corrélation entre deux colonnes sélectionnées.

---

## Fonctionnalités principales

- **Affichage de datasets :**
  - Trois datasets sont chargés dynamiquement depuis des liens CSV.
  - L'utilisateur peut sélectionner un dataset pour visualiser son contenu.

- **Visualisation de graphiques interactifs :**
  - L'utilisateur peut sélectionner deux colonnes pour les axes X et Y.
  - Trois types de graphiques disponibles :
    - Bar Chart
    - Line Chart
    - Scatter Chart

- **Analyse de corrélation :**
  - L'utilisateur peut afficher une matrice de corrélation basée sur les colonnes sélectionnées.
  - La matrice de corrélation est visualisée sous forme de tableau et de heatmap.

---

## Structure du code

1. **Chargement des datasets :**
   - Les datasets sont importés via des liens CSV et stockés dans un dictionnaire pour un accès facile.

2. **Sélection des données :**
   - L'utilisateur choisit un dataset parmi les trois disponibles.
   - Les colonnes du dataset sont proposées pour les axes X et Y.

3. **Affichage des graphiques :**
   - Un graphique interactif est généré en fonction des colonnes et du type de graphique sélectionné.

4. **Matrice de corrélation :**
   - Si les colonnes sélectionnées sont numériques, une matrice de corrélation est affichée.
   - Si les colonnes ne sont pas numériques, un message d'erreur invite l'utilisateur à sélectionner des colonnes valides.

---

## Instructions pour exécuter l'application

1. **Prérequis :**
   - Python 3.7 ou version supérieure
   - Modules nécessaires :
     - `streamlit`
     - `pandas`
     - `seaborn`
     - `matplotlib`

   Vous pouvez installer les dépendances avec la commande :
   ```bash
   pip install streamlit pandas seaborn matplotlib


   ![image](https://github.com/user-attachments/assets/e20348e4-aa35-4fce-b4fa-08399a6d1cd2)

