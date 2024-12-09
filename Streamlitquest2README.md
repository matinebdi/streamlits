# Bienvenue sur le site web de Matin 🌍

Ce projet est une application interactive créée avec **Streamlit**. Elle permet aux utilisateurs de sélectionner une ville parmi trois options et d'afficher une image correspondante de la ville.

---

## Fonctionnalités principales

1. **Affichage dynamique d'images :**
   - L'utilisateur peut choisir une ville parmi les options disponibles : **Brooklyn**, **Paris**, et **Téhéran**.
   - Une image représentative de la ville est affichée directement sur la page.

2. **Interface intuitive :**
   - Utilisation d'une interface simple et conviviale grâce à **Streamlit**.

3. **Message d'erreur :**
   - Si une image ne peut pas être chargée, un message d'erreur est affiché pour informer l'utilisateur.

---

## Structure du code

1. **Bibliothèques utilisées :**
   - `streamlit` : pour l'interface utilisateur.
   - `datetime` : inclus mais non utilisé dans cette version.

2. **Éléments interactifs :**
   - `st.title` : pour afficher un titre sur la page.
   - `st.selectbox` : pour permettre la sélection d'une ville.
   - `st.image` : pour afficher l'image de la ville sélectionnée.

3. **Gestion des images :**
   - Les images des villes sont récupérées depuis des URLs et affichées dynamiquement.
   - Un dictionnaire (`city_images`) associe chaque ville à son URL d'image.

4. **Gestion des erreurs :**
   - Si une image ne peut pas être chargée, un message d'erreur informatif est affiché à l'utilisateur.

---

## Instructions pour exécuter l'application

### Prérequis
- **Python 3.7 ou supérieur**
- **Modules nécessaires :**
  - Installez Streamlit avec la commande :
    ```bash
    pip install streamlit
    ```

### Étapes pour lancer l'application
1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
