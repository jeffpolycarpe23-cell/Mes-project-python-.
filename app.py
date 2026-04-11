import streamlit as st
import requests

# Configuration de la page
st.set_page_config(page_title="Convertisseur Pro", page_icon="💰")

st.title("💰 Convertisseur Universel")
st.subheader("Taux de change officiels en temps réel")

@st.cache_data
def get_currencies():
    try:
        url = "https://open.er-api.com/v6/latest/USD"
        data = requests.get(url).json()
        return sorted(list(data["rates"].keys()))
    except:
        return ["USD", "EUR", "HTG", "XOF"]

liste_devises = get_currencies()

# Entrées du client
montant = st.number_input("Montant à convertir", min_value=0.01, value=1.0)

col1, col2 = st.columns(2)
with col1:
    source = st.selectbox("De", liste_devises, index=liste_devises.index("USD") if "USD" in liste_devises else 0)
with col2:
    cible = st.selectbox("Vers", liste_devises, index=liste_devises.index("HTG") if "HTG" in liste_devises else 0)

if st.button("Calculer le montant", use_container_width=True):
    try:
        res = requests.get(f"https://open.er-api.com/v6/latest/{source}").json()
        taux = res["rates"][cible]
        total = montant * taux
        
        st.divider()
        st.metric(label=f"Total en {cible}", value=f"{total:,.2f} {cible}")
        st.caption(f"Taux actuel : 1 {source} = {taux} {cible}")
    except:
        st.error("Erreur lors du calcul. Vérifiez votre connexion.")

