import arcade
import random

class MyGame(arcade.Window):
   def __init__(self, width, height, title):
       # Call the parent class's init function
       super().__init__(width, height, title)

liste_couleur = [arcade.color.BLUE, arcade.color.RED]

def main():
    window = MyGame(640, 480, "Drawing Example")
    def on_draw():
        arcade.start_render()
        for i in range(20):
            arcade.draw_circle_filled(random.randint(10,640), random.randint(10,480), 10, (255, 54, 34))
        arcade.run()
    on_draw()

main()