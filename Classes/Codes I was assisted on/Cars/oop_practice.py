# https://www.youtube.com/watch?v=cgxTwQT1ahw

import pygame
import random
import os

# place Pygame window at a specific location
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)

class Vehicle:
    def __init__(self,
                color: str = "green",
                x: int = 400,
                y: int = 400
                ) -> None:
        self.img_path = "sedan_" + color + ".png"
        self.location = x, y
        self.draw()
    
    def draw(self):
        # load image and set its location
        self.img = pygame.image.load(self.img_path)
        self.img_location = self.img.get_rect()
        self.img_location.center = self.location

class Truck(Vehicle):
    def __init__(self,
                x:int,
                y:int,
                kind:str = "truck_tractor"):
        super().__init__("green")
        self.img_path = kind + ".png"
        self.location = x, y
        self.draw()

class Police(Vehicle):
    def __init__(self, x = 400, y = 400):
        super().__init__("green", x, y)
        self.img_path = "police_car.png"
        self.location = x, y
        self.draw()
    
# pygame settings
pygame.init()
screen = pygame.display.set_mode((800, 800))
running = True

cars = []

for i in range(10):
    x = random.randint(0, 800)
    y = random.randint(0, 800)
    vehicle_class = random.choice(["sedan", "truck", "police"])

    if vehicle_class == "sedan":
        c = random.choice(["red", "green", "blue"])
        cars.append(Vehicle(c, x, y))
    elif vehicle_class == "truck":
        k = random.choice(["truck_tractor", "box_truck"])
        cars.append(Truck(x, y, k))
    else:
        cars.append(Police(x, y))
    
    

truck = Truck(50, 50)

# set background colour
screen.fill("white")
# place image on the screen
for car in cars:
    screen.blit(car.img, car.img_location)

screen.blit(truck.img, truck.img_location)

# start game loop
while running:
    # if we click on the "exit" button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # stop game loop
            running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()

