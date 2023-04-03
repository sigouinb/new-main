# Benjamin Sigouin, 404

import arcade
import random

# Les mesures de l'ecran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Couleurs des cercles
COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK, arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]

# classe des cercles
class Cercle():
    #fonction qui definit le rayon, la position et la couleur des cercles
    def __init__(self, r,x,y,c):
        self.rayon = r
        self.centre_x = x
        self.centre_y = y
        self.color = (c)
        self.cercle_change_x = 3
        self.cercle_change_y = 3

    def draw(self):
        #arcade.draw_circle_filled(center_x, center_y, rayon, color)
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)
    def on_update(self):
        if self.centre_x < self.rayon:
            self.cercle_change_x *= -1
        if self.centre_x > SCREEN_WIDTH - self.rayon:
            self.cercle_change_x *= -1
        if self.centre_y < self.rayon:
            self.cercle_change_y *= -1
        if self.centre_y > SCREEN_HEIGHT - self.rayon:
            self.cercle_change_y *= -1
        self.centre_x += self.cercle_change_x
        self.centre_y += self.cercle_change_y


# classe du jeu
class MyGame(arcade.Window):
    # fonction qui affiche l'ecran et son titre
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_cercles = []



    # fonction qui transforme la liste en cercles affiches sur l'ecran
    def on_draw(self):
        arcade.start_render()
        for cercle in self.liste_cercles:
            cercle.draw()
            cercle.on_update()

# fonction qui definit ce qui se passe quand on click
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        for cercle in self.liste_cercles:
            # pour chaque cercle, click gauche ou click droit:
            if button == arcade.MOUSE_BUTTON_LEFT:
                # si le curseur est sur un cercle
                rayon = random.randint(10, 50)
                center_x = random.randint(1,10)
                center_y = random.randint(1,10)
                color = random.choice(COLORS)
                cercle = Cercle(rayon, center_x, center_y, color, cercle_change_x, cercle_change_y,)
                self.liste_cercles.append(cercle)
            #if button == arcade.MOUSE_BUTTON_RIGHT:


# fonction qui fait jouer le programme
def main():
    MyGame()
    arcade.run()


main()