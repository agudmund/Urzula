from PySide6.QtGui import QPixmap, QFont, QColor, QPen
from PySide6.QtCore import QRect, Qt, QPoint
from PySide6.QtGui import QPolygon

class Board:
    def __init__(self):
        self.board_image = QPixmap('assets/images/board/british_museum_board.jpg')

        if self.board_image.isNull():
            print("⚠️ Could not load british_museum_board.jpg — double-check the path!")

        self.rosettes = {3, 7, 11, 15, 4, 8, 12, 16}

        # === EXACT ORIGINAL POSITIONS FROM OUR REPO (tuned for TILE_SIZE=62) ===
        # We will tweak these together based on what you see
        self.positions = [
            (180, 120), (250, 120), (320, 120), (390, 120), (460, 120),
            (180, 190), (460, 190),
            (180, 260), (250, 260), (320, 260), (390, 260), (460, 260),
            (530, 190),
            (180, 330), (250, 330), (320, 330), (390, 330), (460, 330),
            (180, 400), (460, 400),
            (180, 470), (250, 470), (320, 470), (390, 470), (460, 470),
        ]

        self.debug = True   # ← Set to False when we're perfectly calibrated

    def is_rosette(self, square):
        return square in self.rosettes

    def get_clicked_square(self, mx, my, tile_size):
        # print(f"🖱️  Click detected at pixel ({int(mx)}, {int(my)})")

        for i, (x, y) in enumerate(self.positions):
            if i >= 20:          # only the first 20 squares are playable
                continue
            rect = QRect(int(x), int(y), int(tile_size), int(tile_size))
            if rect.contains(int(mx), int(my)):
                # print(f"✅ PERFECT HIT! Square {i} selected!")
                return i
            # elif abs(x - mx) < 100 and abs(y - my) < 100:
            #     print(f"   (near square {i} at {x},{y})")
        
        # print("❌ No square detected — hitbox not aligned yet")
        return None

    def draw(self, painter, tile_size):
        # Draw the majestic British Museum photograph first
        if not self.board_image.isNull():
            scaled = self.board_image.scaled(620, 480, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            painter.drawPixmap(85, 95, scaled)
        else:
            painter.fillRect(85, 95, 620, 480, QColor(210, 180, 140))

        # === DEBUG OVERLAY — you will see bright red boxes + numbers! ===
        if self.debug:
            pen = QPen(QColor(255, 50, 50, 200))  # semi-transparent red
            pen.setWidth(4)
            painter.setPen(pen)
            font = QFont("Arial", 16, QFont.Bold)
            painter.setFont(font)
            painter.setBrush(QColor(255, 255, 255, 180))

            for i, (x, y) in enumerate(self.positions):
                if i >= 20:
                    break
                rect = QRect(int(x)-4, int(y)-4, int(tile_size)+8, int(tile_size)+8)
                painter.drawRect(rect)
                painter.drawText(int(x) + 18, int(y) + 45, str(i))

        # Your lovely labels & arrows (kept exactly as you loved them)
        font = QFont("Comic Sans MS", 10)
        painter.setFont(font)
        painter.setPen(QColor(80, 40, 20))
        painter.drawText(50, 420, "Your Home Path heart")
        painter.drawText(50, 150, "Friend's Path sparkles")

        painter.setBrush(QColor(255, 100, 140))
        poly1 = QPolygon([QPoint(680, 190), QPoint(720, 170), QPoint(720, 210)])
        poly2 = QPolygon([QPoint(680, 400), QPoint(720, 380), QPoint(720, 420)])
        painter.drawPolygon(poly1)
        painter.drawPolygon(poly2)