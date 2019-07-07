import math
import random

from ray import obstacle
from ray import ray

class Vector:

    def __init__(self, x, y):
        self.components = [x, y]

    def __iter__(self):
        return (component for component in self.components)

    def __add__(self, other):
        result_com = []
        for self_com, other_com in zip(self, other):
            result_com.append(self_com + other_com)
        return type(self)(*result_com)

def distance(p1, p2):
    return math.pow(p1[0]-p2[0], 2) + math.pow(p1[1]-p2[1], 2)

def generate_obstacle(screen_size, number):
    obstacles = []
    for _ in range(number):
        x1 = random.randint(0, screen_size[0])
        y1 = random.randint(0, screen_size[1])
        x2 = random.randint(0, screen_size[0])
        y2 = random.randint(0, screen_size[1])
        obstacles.append(obstacle.Obstacle(x1, y1, x2, y2))
    return obstacles

def generate_rays(source, number):
    rays = []
    angles = [a for a in angle_range(number)]
    for a in angles:
        x = math.cos(a)
        y = math.sin(a)
        rays.append(ray.Ray(source, (x, y)))
    return rays

def angle_range(number):
    angle = 0
    increment = 2*math.pi/number
    for _ in range(number):
        yield angle
        angle += increment
