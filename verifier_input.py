
def entrer_utilisateur():
    chaine = input("Antre kantite sekens lan separe pa yon espas :").strip()

    while not chaine:
        chaine = input("Antre kantite sekens valid lan separe pa yon espas :").strip()
    return chaine
