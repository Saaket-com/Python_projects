import pygame
import sys
import random
import os

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Coin Collector")
clock = pygame.time.Clock()


player = pygame.image.load("player.jpg")
player = pygame.transform.scale(player, (32, 32))

coin = pygame.image.load("pixel_coin.png")
coin = pygame.transform.scale(coin, (24, 24))


x, y = 100, 100
speed = 4


coin_x = random.randint(0, 600)
coin_y = random.randint(0, 440)


score = 0
high_score = 0


if os.path.exists("highscore.txt"):
    with open("highscore.txt", "r") as f:
        high_score = int(f.read())

font = pygame.font.SysFont(None, 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Save high score
            if score > high_score:
                with open("highscore.txt", "w") as f:
                    f.write(str(score))
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: x -= speed
    if keys[pygame.K_d]: x += speed
    if keys[pygame.K_w]: y -= speed
    if keys[pygame.K_s]: y += speed


    player_rect = pygame.Rect(x, y, 32, 32)
    coin_rect = pygame.Rect(coin_x, coin_y, 24, 24)

    if player_rect.colliderect(coin_rect):
        score += 1
        coin_x = random.randint(0, 600)
        coin_y = random.randint(0, 440)


    screen.fill((0, 180, 0))  # green background
    screen.blit(player, (x, y))
    screen.blit(coin, (coin_x, coin_y))

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    high_text = font.render(f"High Score: {high_score}", True, (0, 0, 0))

    screen.blit(score_text, (10, 10))
    screen.blit(high_text, (10, 40))

    pygame.display.flip()
    clock.tick(60)

