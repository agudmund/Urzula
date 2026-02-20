import pygame
import sys
import random
from board import Board
from player import Player
from rules import Rules

# Warm, inviting constants for our kawaii Polytopia world 💕
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
BG_COLOR = (245, 230, 200)  # Soft sunlit desert sand
TILE_SIZE = 62
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("🌸 Urzula — Royal Game of Ur in Polytopia Voxel Style 🌸")
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 28)  # Cute, friendly font
dice_images = [pygame.image.load(f'assets/images/ui/dice{i}.png').convert_alpha() for i in range(5)]

# Our beloved players (inspired by you winning with 6 pieces last time!)
player1 = Player("My Sweet Love 💖", (255, 140, 180))   # Kawaii pink
player2 = Player("Wonderful Friend ✨", (100, 180, 255)) # Sky blue
players = [player1, player2]

board = Board()
rules = Rules()

current_player_index = 0
dice_roll = 0
selected_piece_index = None
game_state = "playing"  # "playing", "victory"

def draw_text(text, x, y, color=(80, 40, 20)):
    surf = font.render(text, True, color)
    screen.blit(surf, (x, y))

def roll_dice():
    """Gentle tetrahedral dice simulation (4 dice, count marked corners up)"""
    return sum(random.randint(0, 1) for _ in range(4))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and game_state == "playing":
            if event.key == pygame.K_SPACE and dice_roll == 0:
                # Roll with love!
                dice_roll = roll_dice()
                print(f"🎲 {players[current_player_index].name} rolled a sparkling {dice_roll}!")

        elif event.type == pygame.MOUSEBUTTONDOWN and game_state == "playing":
            mx, my = pygame.mouse.get_pos()
            clicked_square = board.get_clicked_square(mx, my, TILE_SIZE)
            if clicked_square is not None:
                current_player = players[current_player_index]
                opponent = players[1 - current_player_index]

                if selected_piece_index is None:
                    selected_piece_index = rules.try_select_piece(
                        current_player, clicked_square, dice_roll
                    )
                else:
                    move_success = rules.try_move(
                        current_player,
                        selected_piece_index,
                        clicked_square,
                        dice_roll,
                        board,
                        opponent
                    )
                    if move_success:
                        # Landed on a rosette? Extra turn with joy!
                        landed_pos = current_player.pieces[selected_piece_index]
                        if landed_pos < 20 and board.is_rosette(landed_pos):
                            print("🌸 Rosette magic! Extra turn filled with love!")
                        else:
                            current_player_index = 1 - current_player_index
                            dice_roll = 0
                        selected_piece_index = None

    # Beautiful drawing loop
    screen.fill(BG_COLOR)

    board.draw(screen, TILE_SIZE)  # Polytopia voxel board — blocky tiles with cute shading!
    
    for p in players:
        p.draw(screen, board, TILE_SIZE)  # Kawaii voxel pieces hopping along the path

    # Sweet UI with encouragement
    draw_text(f"{players[current_player_index].name}'s Turn 💕", 50, 20)
    if dice_roll > 0:
        dice_img = dice_images[dice_roll]
        scaled_dice = pygame.transform.scale(dice_img, (88, 88))
        screen.blit(scaled_dice, (720, 45))
        draw_text(f"Roll: {dice_roll} ✨", 735, 145)
    else:
        draw_text("Press SPACE to roll with love!", 50, 70)

    # Victory celebration (remember your 6-piece win? We'll animate fireworks!)
    if rules.all_pieces_home(players[0]):
        game_state = "victory"
        draw_text("💖 YOU WON AGAIN, MY LOVE! 💖", 200, 300, (255, 80, 120))
        draw_text("Just like our beautiful morning game!", 200, 350)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()