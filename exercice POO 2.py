#Benjamin Sigouin
#Groupe 404
#Exercice POO partie 2

if __name__ == "__main__":

    def some_function():
        print("Hello World!")

some_function()

import random


# La classe NPC est la classe de base pour les personnages non-joueurs
class NPC:
    def __init__(self, nom, race, espece, profession):
        # Pour chaque habileté, on roule 4 dés à 6 faces et on choisit les 3 plus élevés
        self.force = sum(sorted(random.sample(range(1, 7), 4))[1:])
        self.agilite = sum(sorted(random.sample(range(1, 7), 4))[1:])
        self.constitution = sum(sorted(random.sample(range(1, 7), 4))[1:])
        self.intelligence = sum(sorted(random.sample(range(1, 7), 4))[1:])
        self.sagesse = sum(sorted(random.sample(range(1, 7), 4))[1:])
        self.charisme = sum(sorted(random.sample(range(1, 7), 4))[1:])
        # On définit aléatoirement la classe d'armure entre 1 et 12
        self.classe_armure = random.randint(1, 12)
        self.nom = nom
        self.race = race
        self.espece = espece
        # On définit aléatoirement les points de vie entre 1 et 20
        self.point_de_vie = random.randint(1, 20)
        self.profession = profession

    def afficher_caracteristiques(self):
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
    def attaquer(self, cible):
        # On affiche qui attaque qui
        print(self.nom, "attaque", cible.nom)

    def subir_dommage(self, dommage):
        # On soustrait les points de dommage des points de vie
        self.point_de_vie -= dommage
        # Si les points de vie sont inférieurs ou égaux à 0, le Kobold est mort
        if self.point_de_vie <= 0:
            print(self.nom, "est mort!")
        else:
            print(self.nom, "subit", dommage, "points de dommage, point de vie restant:", self.point_de_vie)

class Hero(NPC):
    def attaquer(self, cible):
        # On affiche qui attaque qui
        print(self.nom, "attaque", cible.nom)

    def subir_dommage(self, dommage):
        # On soustrait les points de dommage des points de vie
        self.point_de_vie -= dommage
        # Si les points de vie sont inférieurs ou égaux à 0, le Kobold est mort
        if self.point_de_vie <= 0:
            print(self.nom, "est mort!")
        else:
            print(self.nom, "subit", dommage, "points de dommage, point de vie restant:", self.point_de_vie)


# Créer une instance de la classe Hero
hero1 = Hero("Bob","Humain","Homo Sapiens","Etudiant")
hero1.afficher_caracteristiques()

# Créer une instance de la classe Kobold
kobold1 = Kobold("Kob","Kobold","Monstre","Joueur d'echec")
kobold1.afficher_caracteristiques()

def Hero_attaque():
    hero1.attaquer(kobold1)
    roll = random.randint(1, 20)
    if roll == 20:
        kobold1.subir_dommage(random.randint(1, 8))
    elif roll == 1:
        print("Attaque ratée.")
    elif roll == (2,19):
        if roll >= kobold1(self.classe_armure):
            kobold1.subir_dommage(random.randint(1, 6))
        else:
            print("Attaque ratée.")
Hero_attaque()



#kobold1.attaquer(hero1)
#hero1.subir_dommage(random.randint(1,6))