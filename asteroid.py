import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH, white
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (white),
            (round(self.position.x), round(self.position.y)),
            self.radius,
            LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:  
            return []
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        asteroid1_velocity = self.velocity.rotate(random_angle)
        asteroid2_velocity = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = asteroid1_velocity * 1.2
        asteroid2.velocity = asteroid2_velocity * 1.2
        return [asteroid1, asteroid2]