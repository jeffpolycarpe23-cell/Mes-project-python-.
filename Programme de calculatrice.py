# --- Programme de Calculatrice Interactive ---
# Développé par Jeff
# Ce script permet d'effectuer des opérations mathématiques de base.

while True:
    print("\n--- Menu des Opérations ---")
    print("1 - Addition (+)")
    print("2 - Soustraction (-)")
    print("3 - Multiplication (*)")
    print("4 - Division (/)")
    print("0 - Quitter le programme")

    try:
        # Demander le choix de l'utilisateur
        choix = int(input("\nEntrez votre choix (0-4) : "))
        
        if choix == 0:
            print("Merci d'avoir utilisé la calculatrice. Au revoir !")
            break

        # Vérifier si le choix est valide avant de demander les nombres
        if choix in [1, 2, 3, 4]:
            nombre1 = float(input("Entrez le premier nombre : "))
            nombre2 = float(input("Entrez le deuxième nombre : "))

            if choix == 1:
                resultat = nombre1 + nombre2
                print(f"Résultat : {nombre1} + {nombre2} = {resultat}")
            
            elif choix == 2:
                resultat = nombre1 - nombre2
                print(f"Résultat : {nombre1} - {nombre2} = {resultat}")
            
            elif choix == 3:
                resultat = nombre1 * nombre2
                print(f"Résultat : {nombre1} * {nombre2} = {resultat}")
            
            elif choix == 4:
                # Vérification cruciale pour éviter l'erreur de division par zéro
                if nombre2 == 0:
                    print("Erreur : La division par zéro est impossible.")
                else:
                    resultat = nombre1 / nombre2
                    print(f"Résultat : {nombre1} / {nombre2} = {resultat}")
        else:
            print("Choix invalide. Veuillez choisir un chiffre entre 0 et 4.")
            
    except ValueError:
        # Si l'utilisateur entre une lettre au lieu d'un chiffre
        print("Erreur : Veuillez entrer un nombre valide.")

print("\n--- Fin du programme ---")
