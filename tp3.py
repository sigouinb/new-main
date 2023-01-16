#Benjamin Sigouin, 404
#TP3

from random import randint

playerhp = 20
enemyStrength = randint(1,5)
def jeu():
    monsternumber = 0
    global monsternumber
    print("Vous tombez face à un monstre de difficulté ", enemyStrength, ". Vous avez 4 options:")
    choix = str(input("""1. Combattre
2. Contourner
3. Afficher les règles du jeu
4. Quitter la partie"""))
    if choix == "1":
        def adversaire():
            global winstreak
            winstreak = 0
            enemyhp = 4

            monsternumber += 1
            dice = randint(1, 6)
            print("""Adversaire : numero_adversaire
            Force de l’adversaire :""", enemyStrength,
                  """Niveau de vie de l’usager :""", playerhp,
                  """Combat numero_combat :""", winstreak, """vs""", losestreak)
            print("Vous avez roulé", dice)
            if dice > enemyhp:
                winstreak += 1
                print("Vous avez gagné. Votre nombre de victoires consécutives est", winstreak)
                print("Points de vie:", playerhp + dice)
                jeu()
            elif dice < enemyhp:
                print("Vous avez perdu.")
                print("Points de vie:", playerhp - dice)
                jeu()

        adversaire()


jeu()