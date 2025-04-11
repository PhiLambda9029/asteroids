import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self , x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), int(self.radius), 2)

    def update(self, dt):
        self.position += self.velocity * dt