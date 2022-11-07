import pygame

FPS = 60

window = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Checkers')

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    pygame.quit

main()