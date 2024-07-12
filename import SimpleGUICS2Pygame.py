import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# Initialize globals
WIDTH = 800
HEIGHT = 600
BALL_RADIUS = 20
PAD_WIDTH = 10
PAD_HEIGHT = 100
LEFT = False
RIGHT = True

ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [0, 0]

paddle1_pos = HEIGHT // 2 - PAD_HEIGHT // 2
paddle2_pos = HEIGHT // 2 - PAD_HEIGHT // 2

paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0

lives1 = 3
lives2 = 3
game_over = False

# Modes
DARK_MODE = {
    "background": "Black",
    "mid_line": "White",
    "paddle1": "Blue",
    "paddle2": "Green",
    "ball_outer": "Red",
    "ball_inner": "White",
    "text": "White",
    "game_over": "Red",
}
LIGHT_MODE = {
    "background": "White",
    "mid_line": "Black",
    "paddle1": "Blue",
    "paddle2": "Green",
    "ball_outer": "Red",
    "ball_inner": "Black",
    "text": "Black",
    "game_over": "Black",
}
current_mode = DARK_MODE

# Helper function to spawn the ball
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    vx = random.randrange(120, 240) / 60
    vy = -random.randrange(60, 180) / 60
    if direction == LEFT:
        vx = -vx
    ball_vel = [vx, vy]

# Define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, score1, score2, lives1, lives2, game_over
    score1 = score2 = 0
    paddle1_pos = HEIGHT // 2 - PAD_HEIGHT // 2
    paddle2_pos = HEIGHT // 2 - PAD_HEIGHT // 2
    paddle1_vel = 0
    paddle2_vel = 0
    lives1 = 3
    lives2 = 3
    game_over = False
    spawn_ball(bool(random.randrange(0, 2)))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel, lives1, lives2, game_over

    # Draw background with gradient
    canvas.draw_polygon([[0, 0], [WIDTH, 0], [WIDTH, HEIGHT], [0, HEIGHT]], 0, current_mode["background"], current_mode["background"])

    if game_over:
        canvas.draw_text("GAME OVER", [WIDTH // 2 - 100, HEIGHT // 2 - 50], 50, current_mode["game_over"])
        if score1 > score2:
            canvas.draw_text("Player 1 Wins!", [WIDTH // 2 - 120, HEIGHT // 2 + 50], 40, current_mode["game_over"])
        elif score2 > score1:
            canvas.draw_text("Player 2 Wins!", [WIDTH // 2 - 120, HEIGHT // 2 + 50], 40, current_mode["game_over"])
        else:
            canvas.draw_text("It's a Tie!", [WIDTH // 2 - 70, HEIGHT // 2 + 50], 40, current_mode["game_over"])
        canvas.draw_text(f"Final Score: Player 1 - {score1}, Player 2 - {score2}", [WIDTH // 2 - 160, HEIGHT // 2 + 100], 30, current_mode["game_over"])
        return
    
    # Draw mid line with shadow
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 3, current_mode["mid_line"])  # Mid line

    # Update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Collision with top or bottom wall (inverse the vertical velocity)
    if (ball_pos[1] - BALL_RADIUS <= 0) or (ball_pos[1] + BALL_RADIUS >= HEIGHT):
        ball_vel[1] = -ball_vel[1]

    # Draw ball with shadow
    canvas.draw_circle([ball_pos[0] + 3, ball_pos[1] + 3], BALL_RADIUS, 20, "Gray")
    canvas.draw_circle(ball_pos, BALL_RADIUS, 13, current_mode["ball_outer"])
    canvas.draw_circle(ball_pos, BALL_RADIUS, 7, current_mode["ball_inner"])

    # Update paddle's vertical position, keep paddle on the screen
    if not (((paddle1_pos + paddle1_vel) <= 0) or ((paddle1_pos + paddle1_vel + PAD_HEIGHT) >= HEIGHT)):
        paddle1_pos += paddle1_vel
    if not (((paddle2_pos + paddle2_vel) <= 0) or ((paddle2_pos + paddle2_vel + PAD_HEIGHT) >= HEIGHT)):
        paddle2_pos += paddle2_vel

    # Draw paddles with shadow
    canvas.draw_line([PAD_WIDTH // 2 + 3, paddle1_pos + 3], [PAD_WIDTH // 2 + 3, paddle1_pos + PAD_HEIGHT + 3], PAD_WIDTH, "Gray")
    canvas.draw_line([WIDTH - PAD_WIDTH // 2 + 3, paddle2_pos + 3], [WIDTH - PAD_WIDTH // 2 + 3, paddle2_pos + PAD_HEIGHT + 3], PAD_WIDTH, "Gray")
    canvas.draw_line([PAD_WIDTH // 2, paddle1_pos], [PAD_WIDTH // 2, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, current_mode["paddle1"])
    canvas.draw_line([WIDTH - PAD_WIDTH // 2, paddle2_pos], [WIDTH - PAD_WIDTH // 2, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, current_mode["paddle2"])

    # Determine whether paddle and ball collide
    if (ball_pos[0] - BALL_RADIUS) <= PAD_WIDTH:
        if paddle1_pos <= ball_pos[1] <= (paddle1_pos + PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] += ball_vel[0] / 10
            ball_vel[1] += ball_vel[1] / 10
        else:
            score2 += 1
            lives1 -= 1
            if lives1 <= 0:
                game_over = True
            else:
                spawn_ball(RIGHT)
    elif (ball_pos[0] + BALL_RADIUS) >= (WIDTH - PAD_WIDTH):
        if paddle2_pos <= ball_pos[1] <= (paddle2_pos + PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] += ball_vel[0] / 10
            ball_vel[1] += ball_vel[1] / 10
        else:
            score1 += 1
            lives2 -= 1
            if lives2 <= 0:
                game_over = True
            else:
                spawn_ball(LEFT)

    # Draw score and lives with shadow and better font
    canvas.draw_text(f"Player 1: {score1}", [50, 50], 30, current_mode["text"], "serif")
    canvas.draw_text(f"Player 2: {score2}", [WIDTH - 200, 50], 30, current_mode["text"], "serif")
    canvas.draw_text(f"Lives P1: {lives1}", [50, 100], 30, current_mode["text"], "serif")
    canvas.draw_text(f"Lives P2: {lives2}", [WIDTH - 200, 100], 30, current_mode["text"], "serif")

def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 4
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 4
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 4
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 4

def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if (key == simplegui.KEY_MAP["w"]) or (key == simplegui.KEY_MAP["s"]):
        paddle1_vel = 0
    elif (key == simplegui.KEY_MAP["up"]) or (key == simplegui.KEY_MAP["down"]):
        paddle2_vel = 0

def toggle_mode():
    global current_mode
    if current_mode == DARK_MODE:
        current_mode = LIGHT_MODE
    else:
        current_mode = DARK_MODE

# Create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# Create buttons with custom appearance
frame.add_button("Restart", new_game, 150)
# Add an empty label for spacing
frame.add_label("", 150)
frame.add_button("MODE", toggle_mode, 150)

# Start frame
new_game()
frame.start()