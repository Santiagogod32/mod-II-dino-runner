from dino_runner.components.obstacle.obstacle import Obstacle


class Cactus_large (Obstacle):

    def __init__(self, image):
        super().__init__(image)
        self.rect.y = 300
