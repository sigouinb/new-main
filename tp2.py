#Benjamin Sigouin, 404
#TP2
from random import randint

tries = 0 #Le nombre d'essais est 0 par défault
def jeux(): #fonction du jeux de devinette
    print("J'ai choisi un nombre entre 1 et 1000. À vous de deviner.")
    nombre = randint(0,1000) #La console choisit un nombre aléatoire entre 1 et 1000
    guess = int(input("Entre un nombre.")) #Le joueur devine un nombre
    def game(): #fonction qui détecte si le choix de nombre est >,<, ou = au nombre de la console
        global tries
        if guess != nombre:
            tries += 1 #Le nombre d'essais augmente de 1 à chaque mauvaise réponse
            print("Mauvaise réponse! Essaye encore.")
            if guess > nombre:
                print("Ton choix de nombre est plus grand que mon nombre.")
            elif guess < nombre:
                print("Ton choix de nombre est plus petit que mon nombre.") #La console nous dit si notre réponse est plus grande ou plus petite que son nombre
        elif guess == nombre:
            print("Tu as bien deviné! Ton nombre d'essais est:", tries,) #La console écrit le nombre d'essais
            quitte = str(input("Voulez-vous quitter? (y/n)")) #choix de recommencer ou pas
            if quitte == "n":
                tries = 0 #réinitialise le nombre d'essais à 0
                jeux() #fait rejouer le jeux de devinette
            elif quitte == "y":
                print("Au revoir!") #fin du code

    while guess != nombre:
        guess = int(input("Entre un nombre."))
        game() #fait rejouer les devinettes en autant que le joueur n'a pas le bon nombre
jeux() #fait jouer le jeu