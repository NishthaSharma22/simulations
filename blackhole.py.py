# this has to be my fav and the most satisfying project I ever made. 
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
width, height = 800, 600
black_hole_mass = 1000  
star_mass = 1  
G = 1

black = (0, 0, 0)
yellow = (255, 255, 0)

# Create a window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Black Hole Consumption Simulation")

# Initial positions and velocities
black_hole_pos = [width // 2, height // 2]
star_distance = 300
star_angle = 0
star_velocity = 0.02  # Angular velocity

# Simulation loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update star position
    star_pos = [
        black_hole_pos[0] + star_distance * math.cos(star_angle),
        black_hole_pos[1] + star_distance * math.sin(star_angle),
    ]

    # Draw the objects
    screen.fill(black)
    pygame.draw.circle(screen, yellow, (int(star_pos[0]), int(star_pos[1])), 5)
    pygame.draw.circle(screen, black, (int(black_hole_pos[0]), int(black_hole_pos[1])), 10)

    # Update the star angle based on angular velocity
    star_angle += star_velocity

    # Calculate distance between star and black hole
    distance = math.sqrt((star_pos[0] - black_hole_pos[0]) ** 2 + (star_pos[1] - black_hole_pos[1]) ** 2)

    # Update gravitational force based on star's distance
    force = G * (black_hole_mass * star_mass) / (distance ** 2)
    star_velocity -= force / star_distance  # Adjusting angular velocity based on force

    # If the star gets too close, break the loop (star is consumed)
    if distance < 10:
        break

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Display a message once the star is consumed
print("The star has been consumed by the black hole!")
pygame.quit()
sys.exit()
