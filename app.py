import streamlit as st
import requests

# Configuration de la page
st.set_page_config(page_title="Convertisseur Pro", page_icon="💰")

# Style personnalisé pour cacher le menu technique
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_status_code=True)

st.title("💰 Convertisseur Universel")
st.subheader("Taux de change officiels en temps réel")

@st.cache_data
def get_currencies():
    url = "https://open.er-api.com/v6/latest/USD"
    data = requests.get(url).json()
    return sorted(list(data["rates"].keys()))

try:
    liste_devises = get_currencies()

    # Entrées du client
    montant = st.number_input("Montant à convertir", min_value=0.01, value=1.0, step=1.0)
    
    col1, col2 = st.columns(2)
    with col1:
        source = st.selectbox("De", liste_devises, index=liste_devises.index("USD"))
    with col2:
        cible = st.selectbox("Vers", liste_devises, index=liste_devises.index("HTG"))

    if st.button("Calculer le montant", use_container_width=True):
        res = requests.get(f"https://open.er-api.com/v6/latest/{source}").json()
        taux = res["rates"][cible]
        total = montant * taux
        
        st.divider()
        st.metric(label=f"Total en {cible}", value=f"{total:,.2f} {cible}")
        st.caption(f"Dernière mise à jour : 1 {source} = {taux} {cible}")

except Exception:
    st.error("Connexion aux marchés impossible. Vérifiez votre accès internet.")

