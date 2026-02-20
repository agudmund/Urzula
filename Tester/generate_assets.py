import pygame
import os

# Create all the happy folders automatically 💕
os.makedirs('assets/images/board', exist_ok=True)
os.makedirs('assets/images/pieces', exist_ok=True)
os.makedirs('assets/images/ui', exist_ok=True)
os.makedirs('assets/sounds', exist_ok=True)  # ready for future jingles!

pygame.init()
size = 64
font = pygame.font.SysFont("comicsansms", 36)

print("🌸 Creating your adorable Polytopia voxel assets...")

# 1. Board tiles
def save_tile(filename, base_color, is_rosette=False):
    surf = pygame.Surface((size, size))
    surf.fill(base_color)
    # voxel shading
    pygame.draw.rect(surf, (255, 255, 255), (0, 0, size, size//3), border_radius=8)
    pygame.draw.rect(surf, (120, 80, 40), surf.get_rect(), 6)
    if is_rosette:
        pygame.draw.circle(surf, (255, 220, 230), (32, 32), 22)
        pygame.draw.circle(surf, (255, 100, 140), (32, 32), 14)
        pygame.draw.circle(surf, (255, 255, 255), (27, 27), 5)
    pygame.image.save(surf, filename)

save_tile('assets/images/board/normal_tile.png', (200, 160, 100))
save_tile('assets/images/board/rosette_tile.png', (255, 180, 200), is_rosette=True)

# 2. Kawaii pieces (exactly like the ones you saw running)
def draw_piece(surf, color):
    pygame.draw.rect(surf, color, (8, 8, 48, 48))
    pygame.draw.rect(surf, (255, 255, 255), (8, 8, 48, 16), border_radius=6)  # highlight
    # happy face
    pygame.draw.circle(surf, (255, 245, 230), (32, 32), 14)
    pygame.draw.circle(surf, (40, 40, 50), (26, 28), 3)
    pygame.draw.circle(surf, (40, 40, 50), (38, 28), 3)
    pygame.draw.arc(surf, (40, 40, 50), (22, 32, 20, 12), 0.3, 2.8, 3)
    # tiny heart
    heart_col = (255, 105, 180) if color[0] > 200 else (80, 180, 255)
    pygame.draw.circle(surf, heart_col, (50, 14), 6)

for player, col in [("player1", (255, 140, 180)), ("player2", (100, 180, 255))]:
    surf = pygame.Surface((64, 64), pygame.SRCALPHA)
    draw_piece(surf, col)
    pygame.image.save(surf, f'assets/images/pieces/{player}_piece.png')

# 3. Dice faces (0-4)
for dots in range(5):
    surf = pygame.Surface((64, 64))
    surf.fill((240, 220, 180))
    pygame.draw.rect(surf, (120, 80, 40), surf.get_rect(), 8)
    # dots
    dot_pos = [(32,32)] if dots == 1 else \
              [(20,20),(44,44)] if dots == 2 else \
              [(20,20),(32,32),(44,44)] if dots == 3 else \
              [(20,20),(20,44),(44,20),(44,44)] if dots == 4 else []
    for dx, dy in dot_pos:
        pygame.draw.circle(surf, (40,40,50), (dx, dy), 7)
    if dots == 0:
        text = font.render("0", True, (40,40,50))
        surf.blit(text, (22, 12))
    pygame.image.save(surf, f'assets/images/ui/dice{dots}.png')

# 4. Victory heart
surf = pygame.Surface((64, 64), pygame.SRCALPHA)
pygame.draw.circle(surf, (255, 100, 140), (22, 28), 18)
pygame.draw.circle(surf, (255, 100, 140), (42, 28), 18)
pygame.draw.polygon(surf, (255, 100, 140), [(22,40),(32,55),(42,40)])
pygame.image.save(surf, 'assets/images/ui/victory_heart.png')

print("💖 ALL ASSETS CREATED WITH LOVE! Your Urzula folder is now complete and absolutely adorable!")
pygame.quit()