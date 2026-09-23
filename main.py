import sys
import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # Initialize the clock for frame rate control
    dt = 0.0
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)  # Set the containers for the Player class
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Create a player instance at the center of the screen
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)  # Set the containers for the Asteroid class
    AsteroidField.containers = (updatable,)  # Set the containers for the AsteroidField class
    asteroid_field = AsteroidField()  # Create an asteroid field instance
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)  # Set the containers for the Shot class

    while True:
        log_state() # Log the game state
        for event in pygame.event.get(): # Handle events
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        updatable.update(dt)  # Update each updatable object
        for asteroid in asteroids:  # Check for collisions between the player and asteroids
            if player.collides_with(asteroid):
                log_event("player_hit")  # Log the collision event
                print("Game over!")
                sys.exit()  # Exit the game
                return
            if shots:  # Check for collisions between shots and asteroids
                for shot in shots:
                    if shot.collides_with(asteroid):
                        log_event("asteroid_shot")  # Log the collision event
                        asteroid.split()  # Split the asteroid
                        shot.kill()  # Remove the shot from the game
        screen.fill((0, 0, 0))  # Clear the screen with black
        for item in drawable:  # Draw each drawable object
            item.draw(screen)  # Draw each drawable object
        pygame.display.flip()  # Update the display
        dt = clock.tick(60)/1000.0

if __name__ == "__main__":
    main()
