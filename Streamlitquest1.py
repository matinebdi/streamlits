import streamlit as st
st.write("Hello World")

from datetime import date






# Title
st.title("Bienvenue sur le site web de Matin")

# Dropdown to select city
city = st.selectbox(
    "Indiquez votre arrondissement de récupération",
    ['Brooklyn', 'Paris', 'Teheran']
)

# Dictionary to map city names to image file paths
city_images = {
    'Brooklyn':"https://www.tripsavvy.com/thmb/vLYBPvqAZyqbdHsIxZkvHbZISMg=/2121x1414/filters:fill(auto,1)/GettyImages-540763429-58fb923c5f9b581d59426e03.jpg",
    'Paris': "https://s1.1zoom.me/big0/488/France_Paris_Eiffel_443254.jpg",
    'Teheran': "https://i.pinimg.com/originals/08/dd/fd/08ddfdcdf954bd81a3a90d176b468a2c.jpg"
}

# Display the selected city's image
if city in city_images:
    image_path = city_images[city]
    try:
        st.image(image_path, caption=f"Image de {city}")
    except FileNotFoundError:
        st.error(f"L'image pour {city} est introuvable. Vérifiez le chemin.")





