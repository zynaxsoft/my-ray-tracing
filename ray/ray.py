import pygame

from ray import util


class Ray:

    def __init__(self, source, rel_pos):
        self.source = source
        self.rel_pos = rel_pos

    def find_intersection(self, obstacle):
        x1 = obstacle.x1
        y1 = obstacle.y1
        x2 = obstacle.x2
        y2 = obstacle.y2

        x3 = self.source[0]
        y3 = self.source[1]
        x4 = self.source[0] + self.rel_pos[0]
        y4 = self.source[1] + self.rel_pos[1]

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if den == 0:
            return

        t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / den
        u = -((x1-x2)*(y1-y3) - (y1-y2)*(x1-x3)) / den

        if t > 0 and t < 1 and u > 0:
            x = x1+t*(x2-x1)
            y = y1+t*(y2-y1)
            return (x, y)
        else:
            return

    def draw(self, screen, position):
        pygame.draw.line(screen, (255, 255, 255), position, self.source)

    def cast(self, screen, obstacles):
        intersections = []
        for obstacle in obstacles:
            intersection = self.find_intersection(obstacle)
            if intersection:
                intersections.append(intersection)
        if intersections:
            self.draw(screen, min(intersections, key=lambda x: util.distance(x, self.source)))
