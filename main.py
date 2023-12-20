
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fox Coin Collector")

# Load images
fox_image = pygame.image.load("fox.png")
coin_image = pygame.image.load("coin.png")
background_image = pygame.image.load("background.jpg")

# Resize images
fox_image = pygame.transform.scale(fox_image, (50, 50))
coin_image = pygame.transform.scale(coin_image, (30, 30))
background_image = pygame.transform.scale(background_image, (width, height))

# Game variables
fox_rect = fox_image.get_rect(center=(width // 2, height // 2))
coins = []
score = 0
font = pygame.font.Font(None, 36)

# Timer
clock = pygame.time.Clock()
game_duration = 7  # in seconds
start_time = pygame.time.get_ticks()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and fox_rect.left > 0:
        fox_rect.x -= 5
    if keys[pygame.K_RIGHT] and fox_rect.right < width:
        fox_rect.x += 5
    if keys[pygame.K_UP] and fox_rect.top > 0:
        fox_rect.y -= 5
    if keys[pygame.K_DOWN] and fox_rect.bottom < height:
        fox_rect.y += 5

    # Spawn coins
    if random.randint(0, 100) < 5:
        coin_rect = coin_image.get_rect(center=(random.randint(0, width), random.randint(0, height)))
        coins.append(coin_rect)

    # Check for collisions with coins
    collected_coins = [coin for coin in coins if fox_rect.colliderect(coin)]
    for coin in collected_coins:
        coins.remove(coin)
        score += 10  # Each coin is worth 10 points

    # Draw background
    screen.blit(background_image, (0, 0))

    # Draw fox
    screen.blit(fox_image, fox_rect)

    # Draw coins
    for coin_rect in coins:
        screen.blit(coin_image, coin_rect)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Draw timer
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    remaining_time = max(0, game_duration - elapsed_time)
    timer_text = font.render(f"Time: {remaining_time}s", True, (255, 255, 255))
    screen.blit(timer_text, (width - 120, 10))

    # Check for game over condition
    if remaining_time == 0:
        game_over_text = font.render(f"Game Over! Your score: {score}", True, (255, 255, 255))
        screen.blit(game_over_text, (width // 2 - 200, height // 2 - 20))
        pygame.display.flip()
        pygame.time.delay(3000)  # Display game over message for 3 seconds
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()