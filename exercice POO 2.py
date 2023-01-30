#Benjamin Sigouin
#Groupe 404
#Exercice POO partie 2

if __name__ == "__main__":

    def some_function():
        print("Hello World!")

some_function()

import random


class NPC:
    def __init__(self, nom, race, espece, profession): # Les caractéristiques de la classe NPC
        # Pour chaque habileté, on roule 4 dés à 6 faces et on choisit les 3 plus élevés
        self.force = sum(sorted(random.sample(range(1, 7), 4))[1:])
        self.agilite = sum(sorted(random.sample(range(1, 7), 4))[1:])
        self.constitution = sum(sorted(random.sample(range(1, 7), 4))[1:])
        self.intelligence = sum(sorted(random.sample(range(1, 7), 4))[1:])
        self.sagesse = sum(sorted(random.sample(range(1, 7), 4))[1:])
        self.charisme = sum(sorted(random.sample(range(1, 7), 4))[1:])
        # définit aléatoirement la classe d'armure entre 1 et 12
        self.classe_armure = random.randint(1, 12)
        self.nom = nom
        self.race = race
        self.espece = espece
        # définit aléatoirement les points de vie entre 1 et 20
        self.point_de_vie = random.randint(1, 20)
        self.profession = profession

    def afficher_caracteristiques(self): # fonction pour afficher les caractéristiques du NPC dans la console
        # On affiche les caractéristiques du NPC
        print("Nom: ", self.nom)
        print("Race: ", self.race)
        print("Espèce: ", self.espece)
        print("Profession: ", self.profession)
        print("Force: ", self.force)
        print("Agilité: ", self.agilite)
        print("Constitution: ", self.constitution)
        print("Intelligence: ", self.intelligence)
        print("Sagesse: ", self.sagesse)
        print("Charisme: ", self.charisme)
        print("Classe d'armure: ", self.classe_armure)
        print("Point de vie: ", self.point_de_vie)




# La classe Kobold hérite de la classe NPC
class Kobold(NPC):
    def attaquer(self, cible): # fonction pour attaquer
        # on affiche qui attaque qui
        print(self.nom, "attaque", cible.nom)
        roll = random.randint(1,20) # lance un dé à 20 faces
        if roll == 20: # si on roule 20, c'est une attaque crtique et on ignore l'armure
            print("Attaque critique.")
            cible.subir_dommage(random.randint(1, 8)) # subit un nombre aléatoire de 1 à 8 de dommage
        elif roll >= self.classe_armure:
            cible.subir_dommage(random.randint(1, 6)) # subit un nombre aléatoire de 1 à 6 de dommage
        else: #si on roule moins que la classe d'armure ou 1, l'attaque n'a aucun effet
            print("Attaque ratée")

    def subir_dommage(self, dommage):
        # on soustrait les points de dommage des points de vie
        self.point_de_vie -= dommage
        # si les points de vie sont inférieurs ou égaux à 0, le Kobold est mort
        if self.point_de_vie <= 0:
            print(self.nom, "est mort!")
        else:
            print(self.nom, "subit", dommage, "points de dommage, point de vie restant:", self.point_de_vie)
            # affiche les points de vie restants

class Hero(NPC): # la classe Hero hérite de la classe NPC
    def attaquer(self, cible): #fonction pour attaquer
        # On affiche qui attaque qui
        print(self.nom, "attaque", cible.nom)
        roll = random.randint(1,20) # lance un dé à 20 faces
        if roll == 20: # si on roule 20, c'est une attaque crtique et on ignore l'armure
            print("Attaque critique.")
            cible.subir_dommage(random.randint(1, 8)) # subit un nombre aléatoire de 1 à 8 de dommage
        elif roll >= self.classe_armure:
            cible.subir_dommage(random.randint(1, 6)) # subit un nombre aléatoire de 1 à 6 de dommage
        else: #si on roule moins que la classe d'armure ou 1, l'attaque n'a aucun effet
            print("Attaque ratée")

    def subir_dommage(self, dommage):
        # on soustrait les points de dommage des points de vie
        self.point_de_vie -= dommage
        # si les points de vie sont inférieurs ou égaux à 0, le héro est mort
        if self.point_de_vie <= 0:
            print(self.nom, "est mort!")
        else:
            print(self.nom, "subit", dommage, "points de dommage, point de vie restant:", self.point_de_vie)
            # affiche les points de vie restants


# créer une instance de la classe Héro
hero1 = Hero("Bob","Humain","Homo Sapiens","Etudiant") # assigne ces caractéristiques à nom, race, espece, profession
hero1.afficher_caracteristiques()

# créer une instance de la classe Kobold
kobold1 = Kobold("Kob","Kobold","Monstre","Joueur d'echec") # assigne ces caractéristiques à nom, race, espece, profession
kobold1.afficher_caracteristiques()

hero1.attaquer(kobold1)
kobold1.subir_dommage

kobold1.attaquer(hero1)
hero1.subir_dommage