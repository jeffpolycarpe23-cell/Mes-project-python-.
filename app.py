import streamlit as st
import requests

st.set_page_config(page_title="Calculateur de Devises Pro", page_icon="💰")

st.title("💸 Convertisseur de Devises Automatique")
st.write("Données en temps réel synchronisées avec les marchés mondiaux.")

# Interface utilisateur
col1, col2 = st.columns(2)
with col1:
    montant = st.number_input("Montant à convertir :", min_value=0.0, value=100.0)
with col2:
    source = st.text_input("De (ex: USD) :", value="USD").upper()

cible = st.text_input("Vers (ex: EUR) :", value="EUR").upper()

if st.button("Calculer le taux"):
    try:
        url = f"https://open.er-api.com/v6/latest/{source}"
        reponse = requests.get(url)
        data = reponse.json()
        
        if data["result"] == "success":
            taux = data["rates"].get(cible)
            if taux:
                resultat = montant * taux
                st.metric(label=f"Résultat en {cible}", value=f"{round(resultat, 2)} {cible}")
                st.info(f"Taux actuel : 1 {source} = {taux} {cible}")
            else:
                st.error("Devise cible non trouvée.")
        else:
            st.error("Erreur lors de la récupération des données.")
    except:
        st.error("Erreur de connexion. Vérifiez internet.")
