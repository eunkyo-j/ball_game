Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pygame
import random

# 초기화
pygame.init()

# 화면 설정
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("공 피하기 게임")

# FPS
clock = pygame.time.Clock()

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 플레이어 설정
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 5

# 공 설정
ball_width = 50
ball_height = 50
ball_x = random.randint(0, SCREEN_WIDTH - ball_width)
ball_y = 0
ball_speed = 5

# 점수
start_ticks = pygame.time.get_ticks()

# 게임 루프
running = True
while running:
    dt = clock.tick(60)  # 프레임 설정 (60FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력
    keys = pygame.key.get_pressed()
...     if keys[pygame.K_LEFT] and player_x > 0:
...         player_x -= player_speed
...     if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
...         player_x += player_speed
... 
...     # 공 떨어뜨리기
...     ball_y += ball_speed
...     if ball_y > SCREEN_HEIGHT:
...         ball_y = 0
...         ball_x = random.randint(0, SCREEN_WIDTH - ball_width)
... 
...     # 충돌 처리
...     player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
...     ball_rect = pygame.Rect(ball_x, ball_y, ball_width, ball_height)
...     if player_rect.colliderect(ball_rect):
...         print("Game Over!")
...         running = False
... 
...     # 배경
...     screen.fill(WHITE)
... 
...     # 플레이어 그리기
...     pygame.draw.rect(screen, BLACK, player_rect)
... 
...     # 공 그리기
...     pygame.draw.ellipse(screen, (255, 0, 0), ball_rect)
... 
...     # 점수 표시
...     elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000
...     font = pygame.font.SysFont(None, 36)
...     score_text = font.render(f"Time: {elapsed_time}s", True, BLACK)
...     screen.blit(score_text, (10, 10))
... 
...     pygame.display.update()
... 
... # 종료
... pygame.quit()
>>> [DEBUG ON]
>>> [DEBUG OFF]
