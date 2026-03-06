from PySide6.QtGui import QPixmap, QFont, QColor
from PySide6.QtCore import QRect, QPoint
from PySide6.QtGui import QPolygon


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

        # Load tiles as QPixmap; scaling happens during draw
        self.normal_tile = QPixmap('assets/images/board/normal_tile.png')
        self.rosette_tile = QPixmap('assets/images/board/rosette_tile.png')

    def is_rosette(self, square):
        return square in self.rosettes

    def get_clicked_square(self, mx, my, tile_size):
        mx_i = int(mx)
        my_i = int(my)
        for i, (x, y) in enumerate(self.positions):
            rect = QRect(x, y, tile_size, tile_size)
            if rect.contains(mx_i, my_i):
                return i
        return None

    def draw(self, painter, tile_size):
        for i, (x, y) in enumerate(self.positions):
            tile_img = self.rosette_tile if self.is_rosette(i) else self.normal_tile
            if tile_img.isNull():
                # simple placeholder rectangle
                painter.setBrush(QColor(220, 200, 180))
                painter.setPen(QColor(150, 120, 100))
                painter.drawRect(x, y, tile_size, tile_size)
            else:
                scaled = tile_img.scaled(tile_size, tile_size)
                painter.drawPixmap(x, y, scaled)

        # Sweet labels & exit arrows
        font = QFont("Comic Sans MS", 10)
        painter.setFont(font)
        painter.setPen(QColor(80, 40, 20))
        painter.drawText(50, 420, "Your Home Path 💖")
        painter.drawText(50, 150, "Friend's Path ✨")

        # Draw simple arrows
        painter.setBrush(QColor(255, 100, 140))
        poly1 = QPolygon([QPoint(680, 190), QPoint(720, 170), QPoint(720, 210)])
        poly2 = QPolygon([QPoint(680, 400), QPoint(720, 380), QPoint(720, 420)])
        painter.drawPolygon(poly1)
        painter.drawPolygon(poly2)
