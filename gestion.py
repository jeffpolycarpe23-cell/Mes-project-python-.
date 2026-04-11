# Système de Gestion de Vente d'Eau
# Développé par Jeff

def verifier_statut(quantite):
    """Détermine le statut du client selon la quantité achetée."""
    if quantite >= 18:
        return "Client Grossiste"
    elif quantite >= 10:
        return "Client Régulier"
    else:
        return "Vente au Détail"

total_gallons = 0
total_recette = 0

print("--- Bienvenue dans le Système de Vente ---")

while True:
    try:
        reponse = input("\nQuantité de gallons (0 pour quitter) : ")
        gallons = float(reponse)

        if gallons == 0:
            print("Fermeture du programme... Au revoir !")
            break

        prix_unitaire = float(input("Prix par gallon : "))
        sous_total = gallons * prix_unitaire

        # Application d'une remise de 5% si plus de 10 gallons
        if gallons > 10:
            remise = sous_total * 0.05
            sous_total -= remise
            print(f"Remise de 5% appliquée ! Nouveau total : {sous_total:.2f}")

        statut = verifier_statut(gallons)
        print(f"Statut : {statut}")
        print(f"Total pour cette vente : {sous_total:.2f}")

        # Accumulation des données
        total_gallons += gallons
        total_recette += sous_total

    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")

# Affichage du rapport final
print("\n" + "="*30)
print("      RÉSUMÉ DES VENTES")
print("="*30)
print(f"Total gallons vendus : {total_gallons}")
print(f"Recette totale : {total_recette:.2f} HTG")
print("="*30)
