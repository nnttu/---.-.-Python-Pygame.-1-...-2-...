import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 60
FPS = 60
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Create the paddles and ball
player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)

# Set initial ball speed
ball_speed = [4, 4]

# Game loop
clock = pygame.time.Clock()

while True:
    import pygame
    import sys

    # Initialize Pygame
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 600, 400
    BALL_RADIUS = 15
    PADDLE_WIDTH, PADDLE_HEIGHT = 15, 60
    FPS = 60
    WHITE = (255, 255, 255)
    FONT = pygame.font.Font(None, 36)

    # Create the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ping Pong Game")

    # Create the paddles and ball
    player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    opponent_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH,
                                  PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)

    # Set initial ball speed
    ball_speed = [4, 4]

    # Initialize scores
    player_score = 0
    opponent_score = 0

    # Game loop
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_paddle.top > 0:
            player_paddle.y -= 5
        if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
            player_paddle.y += 5

        # Move opponent paddle (basic AI)
        if ball.centery < opponent_paddle.centery:
            opponent_paddle.y -= 3
        elif ball.centery > opponent_paddle.centery:
            opponent_paddle.y += 3

        # Move the ball
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # Ball collision with walls
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed[1] = -ball_speed[1]

        # Ball collision with paddles
        if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
            ball_speed[0] = -ball_speed[0]

        # Ball out of bounds
        if ball.left <= 0:
            # Opponent scores a point
            opponent_score += 1
            ball.x = WIDTH // 2 - BALL_RADIUS // 2
            ball.y = HEIGHT // 2 - BALL_RADIUS // 2
            ball_speed[0] = -ball_speed[0]

        elif ball.right >= WIDTH:
            # Player scores a point
            player_score += 1
            ball.x = WIDTH // 2 - BALL_RADIUS // 2
            ball.y = HEIGHT // 2 - BALL_RADIUS // 2
            ball_speed[0] = -ball_speed[0]

        # Draw everything
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, WHITE, player_paddle)
        pygame.draw.rect(screen, WHITE, opponent_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)

        # Draw scores
        player_text = FONT.render(str(player_score), True, WHITE)
        opponent_text = FONT.render(str(opponent_score), True, WHITE)
        screen.blit(player_text, (WIDTH // 4, 20))
        screen.blit(opponent_text, (3 * WIDTH // 4 - player_text.get_width(), 20))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)
