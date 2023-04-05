# Benjamin Sigouin, 404
#TP4

import arcade
import random

# Les mesures de l'ecran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Couleurs
COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK, arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY, arcade.color.AZURE, arcade.color.AIR_SUPERIORITY_BLUE, arcade.color.YELLOW, arcade.color.ARMY_GREEN, arcade.color.CHINA_ROSE, arcade.color.CRIMSON]

#classe des Rectangles
class Rectangle():
    #fonction qui definit les positions et les mesures des rectangles
    def __init__(self, x,y,w,h,c,a,b):
        self.center_x = x
        self.center_y = y
        self.width = w
        self.height = h
        self.color = (c)
        self.rectangle_change_x = a
        self.rectangle_change_y = b

    #fonction qui dessine les rectangles
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

    #fonction pour faire bouger les rectangles
    def on_update(self):
        if self.center_x < self.width and self.center_x < self.height:
            self.rectangle_change_x *= -1
        if self.center_x > SCREEN_WIDTH - self.width:
            self.rectangle_change_x *= -1
        if self.center_y < self.width and self.center_y < self.height:
            self.rectangle_change_y *= -1
        if self.center_y > SCREEN_HEIGHT - self.height:
            self.rectangle_change_y *= -1
        self.center_x += self.rectangle_change_x
        self.center_y += self.rectangle_change_y

# classe des cercles
class Cercle():
    #fonction qui definit le rayon, la position et la couleur des cercles
    def __init__(self, r,x,y,c,a,b):
        self.rayon = r
        self.center_x = x
        self.center_y = y
        self.color = (c)
        self.cercle_change_x = a
        self.cercle_change_y = b

    # fonction qui dessine les cercles
    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.rayon, self.color)

    # fonction pour faire bouger les cercles
    def on_update(self):
        if self.center_x < self.rayon:
            self.cercle_change_x *= -1
        if self.center_x > SCREEN_WIDTH - self.rayon:
            self.cercle_change_x *= -1
        if self.center_y < self.rayon:
            self.cercle_change_y *= -1
        if self.center_y > SCREEN_HEIGHT - self.rayon:
            self.cercle_change_y *= -1
        self.center_x += self.cercle_change_x
        self.center_y += self.cercle_change_y

# classe du jeu
class MyGame(arcade.Window):
    # fonction qui affiche l'ecran et son titre et permet d'afficher les objets
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #TP4")
        self.liste_cercles = []
        self.liste_rectangles = []

    # appelle la fonction de dessiner les objets sur l'ecran
    def on_draw(self):
        arcade.start_render()
        for rectangle in self.liste_rectangles:
            rectangle.draw()
        for cercle in self.liste_cercles:
            cercle.draw()

    #appelle la fonction de faire bouger les objets
    def on_update(self, delta_time: float):
        arcade.start_render()
        for rectangle in self.liste_rectangles:
            rectangle.on_update()
        for cercle in self.liste_cercles:
            cercle.on_update()

    # fonction qui definit ce qui se passe quand on click
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
            #fait apparaitre un cercle et ses parametres sur un click gauche
            if button == arcade.MOUSE_BUTTON_LEFT:
                rayon = random.randint(10, 50)
                center_x = x
                center_y = y
                color = random.choice(COLORS)
                cercle_change_x = 3
                cercle_change_y = 3
                cercle = Cercle(rayon, center_x, center_y, color, cercle_change_x, cercle_change_y)
                self.liste_cercles.append(cercle)
            # fait apparaitre un cercle et ses parametres sur un click droit
            if button == arcade.MOUSE_BUTTON_RIGHT:
                center_x = x
                center_y = y
                width = random.randint(15,70)
                height = random.randint(15,70)
                color = random.choice(COLORS)
                rectangle_change_x = 3
                rectangle_change_y = 3
                rectangle = Rectangle(center_x, center_y, width, height, color, rectangle_change_x, rectangle_change_y)
                self.liste_rectangles.append(rectangle)

# fonction qui fait jouer le programme
def main():
    MyGame()
    arcade.run()


main()