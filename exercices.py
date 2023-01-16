#Benjamin Sigouin
#Groupe 404
#Exercices

#Exercice 1
print("EXERCICE 1:")
class StringFoo:
    def __init__(self):
        self.string = ""

    def set_string(self, string):
        self.string = string

    def print_string(self):
        print(self.string)

#Exercice 2
print("EXERCICE 2:")
class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur

    def calcul_aire(self):
        return self.largeur * self.longueur

    def afficher_infos(self):
        print("Largeur :", self.largeur)
        print("Longueur :", self.longueur)
        print("Aire :", self.calcul_aire())
rectangle = Rectangle(5,10)
rectangle.afficher_infos()

#Exercice 3
print("EXERCICE 3:")
import math


class Calcul:
    def calcul_aire_cercle(self, rayon):
        return math.pi * (rayon ** 2)

    def calcul_circonference_cercle(self, rayon):
        return 2 * math.pi * rayon
calcul = Calcul()
aire = calcul.calcul_aire_cercle(15)
circonference = calcul.calcul_circonference_cercle(15)

print(aire)
print(circonference)


#Exercice 4
print("EXERCICE 4:")
import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = random.randint(2, 20)
        self.attack_strength = random.randint(1, 6)
        self.defense_strength = random.randint(1, 6)

    def attack(self):
        return random.randint(1, 6) + self.attack_strength

    def take_damage(self, damage):
        self.hp -= max(0, damage - self.defense_strength)

    def is_alive(self):
        return self.hp > 0
hero = Hero("Robert")
print(hero.name)
print(hero.hp)
print(hero.attack_strength)
print(hero.defense_strength)

damage = hero.attack()
print(f"{hero.name} attaque et inflige {damage} points de dégâts")

hero.take_damage(10)
print(f"{hero.name} a {hero.hp} points de vie restants")

if hero.is_alive():
  print(f"{hero.name} est en vie")
else:
  print(f"{hero.name} est mort")