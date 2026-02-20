import pygame

class Board:
    def __init__(self):
        # Classic 20-square layout
        self.squares = list(range(20))
        self.rosettes = {3, 7, 11, 15, 4, 8, 12, 16}
        
        # Voxel positions (same loving layout)
        self.positions = [
            (180, 120), (250, 120), (320, 120), (390, 120), (460, 120),
            (180, 190), (460, 190),
            (180, 260), (250, 260), (320, 260), (390, 260), (460, 260),
            (530, 190),
            (180, 330), (250, 330), (320, 330), (390, 330), (460, 330),
            (180, 400), (460, 400),
            (180, 470), (250, 470), (320, 470), (390, 470), (460, 470),
        ]

        # Load the beautiful voxel tiles we just created!
        self.normal_tile = pygame.transform.scale(
            pygame.image.load('assets/images/board/normal_tile.png').convert_alpha(), (62, 62))
        self.rosette_tile = pygame.transform.scale(
            pygame.image.load('assets/images/board/rosette_tile.png').convert_alpha(), (62, 62))

    def is_rosette(self, square):
        return square in self.rosettes

    def get_clicked_square(self, mx, my, tile_size):
        for i, (x, y) in enumerate(self.positions):
            rect = pygame.Rect(x, y, tile_size, tile_size)
            if rect.collidepoint(mx, my):
                return i
        return None

    def draw(self, screen, tile_size):
        for i, (x, y) in enumerate(self.positions):
            tile_img = self.rosette_tile if self.is_rosette(i) else self.normal_tile
            screen.blit(tile_img, (x, y))

        # Sweet labels & exit arrows (still there with love)
        font = pygame.font.SysFont("comicsansms", 18)
        label1 = font.render("Your Home Path 💖", True, (80, 40, 20))
        label2 = font.render("Friend's Path ✨", True, (80, 40, 20))
        screen.blit(label1, (50, 420))
        screen.blit(label2, (50, 150))

        pygame.draw.polygon(screen, (255, 100, 140), [(680, 190), (720, 170), (720, 210)])
        pygame.draw.polygon(screen, (255, 100, 140), [(680, 400), (720, 380), (720, 420)])