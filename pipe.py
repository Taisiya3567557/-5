import pygame
import random
from config import *

class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = PIPE_WIDTH
        self.gap = PIPE_GAP
        self.height = random.randint(50, SCREEN_HEIGHT - self.gap - 50)
        self.passed = False

    def update(self):
        self.x -= 3

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, self.width, self.height))
        bottom_y = self.height + self.gap
        pygame.draw.rect(screen, (0, 255, 0), (self.x, bottom_y, self.width, SCREEN_HEIGHT))

    def collide(self, bird):
        bird_rect = bird.get_rect()
        top_pipe = pygame.Rect(self.x, 0, self.width, self.height)
        bottom_pipe = pygame.Rect(self.x, self.height + self.gap, self.width, SCREEN_HEIGHT)
        return bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe)
