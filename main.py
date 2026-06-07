# Example file showing a circle moving on screen
import pygame
import random
import sys

# pygame setup
pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True


player_size = 60
player = pygame.Rect(WIDTH // 2, HEIGHT - 100, player_size, player_size)
player_speed = 10

enemy_size = 60
enemy = pygame.Rect(random.randint(0, WIDTH - enemy_size), HEIGHT - 600, enemy_size, enemy_size)
enemy_speed = 5

score = 0


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed


    enemy.y += enemy_speed 
    
    if enemy.y > HEIGHT:
        enemy.y = 0
        enemy.x = random.randint(0, WIDTH - enemy_size)
        enemy_speed += 0.5  # Increase speed for next time
        score += 1
        print(score)
        
        
    if player.colliderect(enemy):
        print("Game Over!")
        pygame.quit() 
        sys.exit()
        
    player.x = max(0, min(WIDTH - player_size, player.x))
    player.y = max(0, min(HEIGHT - player_size, player.y))
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.rect(screen, (255, 0, 255), player)
    pygame.draw.rect(screen, (0, 250, 250), enemy)


    text = pygame.font.SysFont("Times New Roman", bold=True, italic=True, size=30).render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (600, 10))
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    clock.tick(60)

pygame.quit()