import arcade
import random

# Les mesures de l'ecran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Couleurs des cercles
COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK, arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]


# classe des cercles
class Cercle():
    # fonction qui definit le rayon, la position et la couleur des cercles
    def __init__(self, r, x, y, c):
        self.rayon = r
        self.centre_x = x
        self.centre_y = y
        self.color = (c)

# fonction qui dessine les cercles remplis
    def draw(self):
        # arcade.draw_circle_filled(center_x, center_y, rayon, color)
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


# classe du jeu
class MyGame(arcade.Window):
    # fonction qui affiche l'ecran et son titre
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_cercles = []

    def setup(self):
        # remplir la liste avec 20 objets de type Cercle
        for _ in range(20):
            rayon = random.randint(10, 50)
            center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLORS)
            cercle = Cercle(rayon, center_x, center_y, color)
            self.liste_cercles.append(cercle)

    def on_update(self):
        self.

    # fonction qui transforme la liste en cercles affiches sur l'ecran
    def on_draw(self):
        arcade.start_render()
        for cercle in self.liste_cercles:
            cercle.draw()

    # fonction qui definit ce qui se passe quand on click
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        for cercle in self.liste_cercles:
            # pour chaque cercle, click gauche ou click droit:
            if button == arcade.MOUSE_BUTTON_LEFT:
                # si le curseur est sur un cercle
                if x > cercle.centre_x - cercle.rayon and x < cercle.centre_x + cercle.rayon and y < cercle.centre_y + cercle.rayon and y > cercle.centre_y - cercle.rayon:
                    self.liste_cercles.remove(cercle)  # enleve le cercle clique
            if button == arcade.MOUSE_BUTTON_RIGHT:
                # si le curseur est sur un cercle
                if x > cercle.centre_x - cercle.rayon and x < cercle.centre_x + cercle.rayon and y < cercle.centre_y + cercle.rayon and y > cercle.centre_y - cercle.rayon:
                    cercle.color = random.choice(COLORS)  # change la couleur du cercle clique


# fonction qui fait joeur le programme
def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
