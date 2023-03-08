import random
import pygame
from dino_runner.components.obstacle.bird import Bird
from dino_runner.components.obstacle.cactus import Cactus
from dino_runner.components.obstacle.cactus_large import Cactus_large
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
           range = random.randint(0, 2)

           list_cactus = [
               Cactus(SMALL_CACTUS[range]), 
               Cactus_large(LARGE_CACTUS[range]),
               Bird(BIRD[0]),
                 ]
           
           self.obstacles.append(list_cactus[random.randint(0, 2)])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen) 

    def remove_obstacle(self):
        self.obstacles = []