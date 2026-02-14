from logger import log_state
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    
    
    while True:
        log_state()
        #player.update(dt)
        updatable.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        #player.draw(screen)
        for drawables in drawable:
            drawables.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
        
if __name__ == "__main__":    
    main()
    

