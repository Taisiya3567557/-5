import pygame
from config import *
from neural_network import NeuralNetwork

class Bird:
    def __init__(self, x=100, y=SCREEN_HEIGHT//2, brain=None):
        self.x = x
        self.y = y
        self.radius = 10
        self.velocity = 0
        self.alive = True
        self.score = 0
        self.fitness = 0
        self.brain = brain.copy() if brain else NeuralNetwork()

    def update(self, pipes):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.score += 1

        if self.y < 0 or self.y > SCREEN_HEIGHT:
            self.alive = False
            return

        next_pipe = None
        for pipe in pipes:
            if pipe.x + pipe.width > self.x:
                next_pipe = pipe
                break

        if next_pipe:
            inputs = [
                self.y / SCREEN_HEIGHT,
                next_pipe.x / SCREEN_WIDTH,
                (next_pipe.height + PIPE_GAP / 2 - self.y) / SCREEN_HEIGHT
            ]
            if self.brain.predict(inputs):
                self.flap()

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)
