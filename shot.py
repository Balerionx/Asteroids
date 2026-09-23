import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, white

class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            (white),
            (round(self.position.x), round(self.position.y)),
            SHOT_RADIUS)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt