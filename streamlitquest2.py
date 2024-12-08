import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


st.title("Manipulation de données et création de graphiques")

link1 =  "https://raw.githubusercontent.com/BriceNW/datasets/main/Admission.csv"
df1 = pd.read_csv(link1).head(21)
link2 = "https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv"
df2 = pd.read_csv(link2).head(21) 
link3 =  "https://raw.githubusercontent.com/BriceNW/datasets/main/Admission.csv"
df3 = pd.read_csv(link3).head(21)

#_________________________________________________________________________________________________________________________________________________________________________________________________
dataframes = {
    "DataFrame 1": df1,
    "DataFrame 2": df2,
    "DataFrame 3": df3,
}


selected_label = st.selectbox("Quel dataset veux-tu?", list(dataframes.keys()))

if selected_label:
    st.dataframe(dataframes[selected_label])
else:
    st.write("Veuillez sélectionner un dataset.")

selected_df = dataframes[selected_label]
selected_df.columns = selected_df.columns.str.strip().str.lower()
x_column = st.selectbox("Choisissez une colonne pour l'axe X :",[""]  + selected_df.columns)
y_column = st.selectbox("Choisissez une colonne pour l'axe Y :",[""] + selected_df.columns)



viz = {
    "Bar Chart": st.bar_chart,
    "Line Chart": st.line_chart,
    "Scatter Chart": st.scatter_chart,  
}



selected_chart = st.selectbox("Choisissez un type de graphique :",[""] + list(viz.keys()))

if x_column and y_column and selected_chart:
    if x_column == y_column:
        st.write("Erreur : Les colonnes X et Y doivent être différentes.")
    else:
        if selected_chart == "Bar Chart":
            st.bar_chart(selected_df.set_index(x_column)[y_column])

        elif selected_chart == "Line Chart":
            st.line_chart(selected_df.set_index(x_column)[y_column])

        elif selected_chart == "Scatter Chart":
            fig, ax = plt.subplots()
            ax.scatter(selected_df[x_column], selected_df[y_column], color="blue", label="Points")
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            ax.set_title(f"Scatter Plot: {x_column} vs {y_column}")
            ax.legend()
            st.pyplot(fig)
else:
    st.write("Veuillez sélectionner une colonne pour X, Y et un type de graphique.")


show_correlation = st.checkbox("Afficher la matrice de corrélation")
if show_correlation:
    if x_column and y_column:
        if pd.api.types.is_numeric_dtype(selected_df[x_column]) and pd.api.types.is_numeric_dtype(selected_df[y_column]):
            st.write(f"### Corrélation entre '{x_column}' et '{y_column}'")
            
            selected_data = selected_df[[x_column, y_column]]
            correlation_matrix = selected_data.corr()
            fig, ax = plt.subplots(figsize=(5, 5))
            sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="rocket", square=True, ax=ax)
            ax.set_title(f"Matrice de corrélation : {x_column} et {y_column}")
            st.pyplot(fig)
        else:
            st.write("reselectionnez vos colonnes please")
    


