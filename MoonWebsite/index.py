# C# c'est pas en tabulation

#API européenne/gratuite et sans inscription, data de la NASA et de l'ESA, termainal : pip install requests et import requests mais le firewall de l'école bloque

#methode sans paramètre avec () vides, tout tabuler pour qu'il prend en compte

#python affiche seulement si une fois je l'appelle genre accueil(), sinon il exécute mais sans rien montrer

def accueil():
    print("=== AstroLab ===")
    print("Vous pouvez faire un choix")
    print("")

    print("1 - Planètes")
    print("2 - Fusées")
    print("3 - Calculs")
    print("4 - Missions")
    print("5 - Simulateur")

    # je veux que si c'est + petit que 1 ou + grand que choixPossible
    choixPossible = 5

    #while True: crée une boucle qui ne s'arrête jamais par elle-même.
    while True:
        # c'est comme try catch en C#, là c'est try execpt
        try:
            choixNombre = int(input("Faire un choix : "))
            
            if choixNombre >= 1 and choixNombre <= choixPossible:
                break  # On sort de la while
            else:
                print("Pas possible, le nombre doit être entre 1 et", choixPossible)

        # Si choixNombre pas INT, alors catch l'erreur ici, ça ne quitte pas le programme
        except ValueError:
            print("Erreur : Vous devez entrer un CHIFFRE, pas une lettre !")

    #retourne la valeur pour pouvoir l'utiliser ailleurs
    return choixNombre

#autres méthodes
def planetes():
    print("\n--- Menu Planètes ---")
    print("Voici le système solaire (du plus petit au plus grand) :")
    print("")
    print("Mercure   .")
    print("Mars      .")
    print("Vénus     o")
    print("Terre     o")
    print("Neptune   o")
    print("Uranus    o")
    print("Saturne ==O==")
    print("Jupiter   O")
    print("\n---------------------")

    #dictionnaire avec nom planète et data genre gravity Planetes["CeQuOnVeut"]
    #Gemini m'a aidé pour avoir toutes es datas
    SimulationDatas = {
        "Mercure": {"gravity": 3.7, "meanRadius": 2439.4, "distanceFromSun": 57.9, "dayLength": 4222.6, "temperature": 167},
        "Venus": {"gravity": 8.87, "meanRadius": 6051.8, "distanceFromSun": 108.2, "dayLength": 2802.0, "temperature": 464},
        "Terre": {"gravity": 9.81, "meanRadius": 6371.0, "distanceFromSun": 149.6, "dayLength": 24.0, "temperature": 15},
        "Mars": {"gravity": 3.71, "meanRadius": 3389.5, "distanceFromSun": 227.9, "dayLength": 24.7, "temperature": -65},
        "Jupiter": {"gravity": 24.79, "meanRadius": 69911.0, "distanceFromSun": 778.5, "dayLength": 9.9, "temperature": -110},
        "Saturne": {"gravity": 10.44, "meanRadius": 58232.0, "distanceFromSun": 1434.0, "dayLength": 10.7, "temperature": -140},
        "Uranus": {"gravity": 8.69, "meanRadius": 25362.0, "distanceFromSun": 2871.0, "dayLength": 17.2, "temperature": -195},
        "Neptune": {"gravity": 11.15, "meanRadius": 24622.0, "distanceFromSun": 4495.1, "dayLength": 16.1, "temperature": -200}
    }

    while True:
        # capitalize() met première lettre en majuscule mars = Mars
        choosePlanet = input("\nEntrez le nom d'une planète (Mars, Terre, Jupiter...) : ").capitalize()
        
        # si valeur user est dans dico
        if choosePlanet in SimulationDatas:
            # alors mettre ligne dico dans une variable, comme ça utilisable + simplement pour avoir chaque partie
            infos = SimulationDatas[choosePlanet]

            # prendre tout infos
            gravite = infos["gravity"]
            rayon = infos["meanRadius"]
            distance = infos["distanceFromSun"]
            journee = infos["dayLength"]
            temperature = infos["temperature"]
            
            # f + simple au lieu d'ajouter genre + entre texte et variable, {} met valeur des variables
            print(f"Planète : {choosePlanet} | Gravité : {gravite} m/s² | Rayon : {rayon} km | Distance : {distance} Mkm | Jour : {journee}h | Temp : {temperature}°C")
        
            try:
                #\n retour a la ligne
                rejouer = int(input("\nVoulez-vous faire une autre planète (1) ou quitter vers le menu (autre touche) ? "))
                if rejouer == 1:
                    pass  # rien faire, la boucle while recommence
                else:
                    break # On quitte la fonction
            except ValueError:
                break
        else:
            # Si la planète est fausse, le message s'affiche et la boucle "while" recommence DIRECTEMENT au début
            print("Planète inconnue ou erreur. Merci de réessayer.")

    #utile pour calcul
    return SimulationDatas


#dictionnaire de planètes
def fusees(SimulationDatas):
    # Dictionnaire de secours, je pouvais pas accéder sans ça
    if not SimulationDatas:
        SimulationDatas = {
            "Mercure": {"gravity": 3.7, "distanceFromSun": 57.9},
            "Venus":   {"gravity": 8.87, "distanceFromSun": 108.2},
            "Terre":   {"gravity": 9.81, "distanceFromSun": 149.6},
            "Mars":    {"gravity": 3.71, "distanceFromSun": 227.9},
            "Jupiter": {"gravity": 24.79, "distanceFromSun": 778.5},
            "Saturne": {"gravity": 10.44, "distanceFromSun": 1434.0},
            "Uranus":  {"gravity": 8.69, "distanceFromSun": 2871.0},
            "Neptune": {"gravity": 11.15, "distanceFromSun": 4495.1}
        }

    print("\n--- Menu Fusées ---")
    print("1. Sélectionner une fusée et simuler un décollage")
    print("2. Retour au menu principal")
    
    try:
        choixMenuFusees = int(input("\nFaire un choix : "))
        
        if choixMenuFusees == 2:
            print("Retour au menu principal...")
            return

        elif choixMenuFusees == 1:
            print("\n=== Choisissez votre lanceur ===")
            print("1 - Ariane 6 (Idéal pour les planètes proches)")
            print("2 - Starship (Idéal pour le système solaire lointain)")
            print("3 - Saturn V (Le classique indémodable)")    
            
            try:
                choixLanceur = int(input("Votre choix de fusée (1-3) : "))
            except ValueError:
                print("Choix invalide. Retour au menu.")
                return

            if choixLanceur == 1:
                nomFusee = "Ariane 6"
                # Dessins ASCII Gemini
                asciiFusee = """
       /\\
      |  |
      |  |
     /____\\
     |    |
     |NASA|
    /|    |\\
   /_|____|_\\
     * * *
    * *
"""
            elif choixLanceur == 2:
                nomFusee = "Starship"
                asciiFusee = """
       /\\
      /  \\
     |    |
     |    |
     |    |
    /|    |\\
   / |____| \\
  /_/ |||| \\_\\
      ****
     ******
"""
            elif choixLanceur == 3:
                nomFusee = "Saturn V"
                asciiFusee = """
       ^
      /|\\
     | | |
     | | |
     |USA|
     | | |
    /| | |\\
   /_|_|_|_\\
     vvvvv
      vvv
"""
            else:
                print("Fusée inconnue")
                return

            while True:
                PlanetCible = input("Entrez la planète de destination : ").capitalize()
                if PlanetCible in SimulationDatas:
                    PlanetGravity = SimulationDatas[PlanetCible]["gravity"]
                    break
                else:
                    print("Planète inconnue. Réessayez.")

            CarburantNecessaire = 1000 * PlanetGravity

            #afficher 40 fois le =
            print("\n" + "="*40)
            print(f"PRÉPARATION DU DÉCOLLAGE DE : {nomFusee}")
            print("="*40)
            print(asciiFusee)
            print(f"Destination : {PlanetCible}")
            print(f"Gravité à l'atterrissage : {PlanetGravity} m/s²")
            print(f"Estimation du carburant requis : {CarburantNecessaire:.0f} Tonnes")
            print("="*40)
            print("3... 2... 1...")

        else:
            print("Pas possible, le nombre doit être 1 ou 2.")

    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide !")


# On sépare complètement la fonction calculs pour éviter les chevauchements
def calculs(SimulationDatas):
    choixPossibleCalculs = 5

    while True:
        print("\n--- Menu Calculs ---")
        print("1. Calculer mon poids sur une autre planète")
        print("2. Calculer la hauteur de mon saut sur une autre planète")
        print("3. Calculer le temps de voyage vers une planète")
        print("4. Calculer mon âge cosmique (en années locales)")
        print("5. Retour au menu principal")

        try: 
            choixMenuCalculs = int(input("\nFaire un choix : "))
            
            if choixMenuCalculs == 5:
                print("Retour au menu principal...")
                break

            elif choixMenuCalculs == 1:
                print("\n--- Calcul du Poids ---")
                PoidsTerre = float(input("Entrez votre poids sur Terre (en kg) : "))
                
                while True:
                    PlanetCible = input("Entrez le nom de la planète cible : ").capitalize()
                    if PlanetCible in SimulationDatas:
                        PlanetGravity = SimulationDatas[PlanetCible]["gravity"]
                        break
                    else:
                        print("Planète inconnue. Réessayez.")
                
                PoidsFinal = (PoidsTerre / 9.81) * PlanetGravity
                print(f" Sur {PlanetCible}, vous pèseriez : {PoidsFinal:.2f} kg !")

            elif choixMenuCalculs == 2:
                print("\n--- Calcul du Saut ---")
                SautTerre = float(input("Combien de centimètres sautez-vous sur Terre ? (ex: 40) : "))
                
                while True:    
                    PlanetCible = input("Entrez le nom de la planète cible : ").capitalize()
                    if PlanetCible in SimulationDatas:
                        PlanetGravity = SimulationDatas[PlanetCible]["gravity"]
                        break
                    else:
                        print("Planète inconnue. Réessayez.")
                
                SautFinal = SautTerre * (9.81 / PlanetGravity)
                print(f"👉 Sur {PlanetCible}, vous sauteriez à : {SautFinal:.2f} cm de hauteur !")

            elif choixMenuCalculs == 3:
                print("\n--- Temps de Voyage ---")
                VitesseKmh = float(input("Entrez la vitesse de votre fusée (en km/h, ex: 40000) : "))
                
                while True:
                    PlanetCible = input("Entrez le nom de la planète de destination : ").capitalize()
                    if PlanetCible in SimulationDatas:
                        DistanceMkm = SimulationDatas[PlanetCible]["distanceFromSun"]
                        break
                    else:
                        print("Planète inconnue. Réessayez.")
                
                Heures = (DistanceMkm * 1000000) / VitesseKmh
                Jours = Heures / 24
                
                print(f"Le voyage vers {PlanetCible} prendrait environ {Heures:.0f} heures, soit {Jours:.1f} jours terrestres !")

            elif choixMenuCalculs == 4:
                print("\n--- Âge Cosmique ---")
                AgeTerre = float(input("Entrez votre âge sur Terre : "))
                
                while True:
                    PlanetCible = input("Entrez le nom de la planète cible : ").capitalize()
                    if PlanetCible in SimulationDatas:
                        AnneesConversion = {
                            "Mercure": 0.24, "Venus": 0.62, "Terre": 1.0, "Mars": 1.88,
                            "Jupiter": 11.86, "Saturne": 29.45, "Uranus": 84.02, "Neptune": 164.8
                        }
                        AnneePlanete = AnneesConversion[PlanetCible]
                        break
                    else:
                        print("Planète inconnue. Réessayez.")
                
                AgeFinal = AgeTerre / AnneePlanete
                print(f"👉 Sur {PlanetCible}, vous auriez : {AgeFinal:.1f} ans !")

            try:
                rejouer = int(input("\nFaire un autre calcul (1) ou quitter (autre touche) ? "))
                if rejouer != 1: 
                    break         
            except ValueError:
                break
                
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide !")


def missions():
    print("--- Menu Missions ---")


def simulateur():
    print("--- Menu Simulateur ---")


ConteneurDonnees = {}

#faut stocker dans une variable pour réutiliser la valeur de return, sinon ça relance la méthode
choix = accueil()

#bonne méthode selon le chiffre retourné
if choix == 1:
    #stocke le dictionnaire retourné par planetes() pour pouvoir le passer à calculs() plus tard
    ConteneurDonnees = planetes()

elif choix == 2:
    #le return
    fusees(ConteneurDonnees) 

elif choix == 3:
#crée ce dictionnaire de secours pour éviter que le programme ne plante avec une erreur KeyError si l'utilisateur va directement dans le menu "Calculs" sans être passé par le menu "Planètes" d'abord.
    if not ConteneurDonnees:
        ConteneurDonnees = {
            "Mercure": {"gravity": 3.7, "distanceFromSun": 57.9},
            "Venus": {"gravity": 8.87, "distanceFromSun": 108.2},
            "Terre": {"gravity": 9.81, "distanceFromSun": 149.6},
            "Mars": {"gravity": 3.71, "distanceFromSun": 227.9},
            "Jupiter": {"gravity": 24.79, "distanceFromSun": 778.5},
            "Saturne": {"gravity": 10.44, "distanceFromSun": 1434.0},
            "Uranus": {"gravity": 8.69, "distanceFromSun": 2871.0},
            "Neptune": {"gravity": 11.15, "distanceFromSun": 4495.1}
        }
    calculs(ConteneurDonnees)

elif choix == 4:
    missions()

elif choix == 5:
    simulateur()
else:
    print("Il y a une erreur")