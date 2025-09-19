import pygame
import sys
from config import *
from pipe import Pipe
from ga import Population

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

def main():
    population = Population()
    pipes = [Pipe(SCREEN_WIDTH + i * 200) for i in range(3)]
    
    while True:
        clock.tick(FPS)
        screen.fill((135, 206, 235))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Обновление
        for bird in population.birds:
            if bird.alive:
                bird.update(pipes)
                for pipe in pipes:
                    if pipe.collide(bird):
                        bird.alive = False

        for pipe in pipes:
            pipe.update()
            if pipe.x + pipe.width < 0:
                pipes.remove(pipe)
                pipes.append(Pipe(SCREEN_WIDTH + 200))

        # Отрисовка
        for pipe in pipes:
            pipe.draw(screen)

        for bird in population.birds:
            if bird.alive:
                bird.draw(screen)

        # Текст
        alive_count = sum(b.alive for b in population.birds)
        gen_text = font.render(f"Generation: {population.generation}", True, (0, 0, 0))
        alive_text = font.render(f"Alive: {alive_count}", True, (0, 0, 0))
        screen.blit(gen_text, (10, 10))
        screen.blit(alive_text, (10, 40))

        pygame.display.flip()

        # Переход к новому поколению
        if population.all_dead():
            population.reproduce()
            pipes = [Pipe(SCREEN_WIDTH + i * 200) for i in range(3)]

if __name__ == "__main__":
    main()
