import pygame
import argparse
import os

from ray import obstacle
from ray import ray
from ray import util

os.environ['SDL_AUDIODRIVER'] = 'dsp'

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number-of-rays', type=int, default=100)
parser.add_argument('-o', '--number-of-objects', type=int, default=10)
parser.add_argument('--width', type=int, default=800)
parser.add_argument('--height', type=int, default=800)
args = parser.parse_args()

pygame.init()
screen_size = (args.width, args.height)
screen = pygame.display.set_mode(screen_size)

white = (255, 255, 255)

obstacles = util.generate_obstacle(screen_size, args.number_of_objects)
obstacles.append(obstacle.Obstacle(0, 0, 0, screen_size[1]))
obstacles.append(obstacle.Obstacle(0, 0, screen_size[0], 0))
obstacles.append(obstacle.Obstacle(screen_size[0], screen_size[1], screen_size[0], 0))
obstacles.append(obstacle.Obstacle(screen_size[0], screen_size[1], 0, screen_size[1]))

source = (100, 200)

while True:
    screen.fill((0, 0, 0))
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.MOUSEMOTION:
        source = event.pos
    for obs in obstacles:
        obs.draw(screen)
    rays = util.generate_rays(source, args.number_of_rays)
    for r in rays:
        r.cast(screen, obstacles)
    pygame.display.flip()
