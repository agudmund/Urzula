import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QPixmap, QFont, QColor
from PySide6.QtCore import Qt, QTimer, QRect

from board import Board
from player import Player
from rules import Rules

# Warm, inviting constants for our kawaii Polytopia world 💕
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
BG_COLOR = QColor(245, 230, 200)  # Soft sunlit desert sand
TILE_SIZE = 62
FPS = 60


class GameWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Players
        self.player1 = Player("My Sweet Love 💖", (255, 140, 180))
        self.player2 = Player("Wonderful Friend ✨", (100, 180, 255))
        self.players = [self.player1, self.player2]

        self.board = Board()
        self.rules = Rules()

        self.current_player_index = 0
        self.dice_roll = 0
        self.selected_piece_index = None
        self.game_state = "playing"

        # Load and pre-scale dice images
        self.dice_images = []
        for i in range(5):
            pix = QPixmap(f'assets/images/ui/dice{i}.png')
            if pix.isNull():
                pix = QPixmap(88, 88)
                pix.fill(Qt.transparent)
            else:
                pix = pix.scaled(88, 88, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.dice_images.append(pix)

        # UI font
        self.ui_font = QFont('Comic Sans MS', 14)

        # Timer for redraw
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(int(1000 / FPS))
        # Accept keyboard focus so keyPressEvent works
        self.setFocusPolicy(Qt.StrongFocus)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), BG_COLOR)

        # Draw board and pieces
        self.board.draw(painter, TILE_SIZE)
        for p in self.players:
            p.draw(painter, self.board, TILE_SIZE)

        # Draw UI text
        painter.setFont(self.ui_font)
        painter.setPen(QColor(80, 40, 20))
        current_name = self.players[self.current_player_index].name
        painter.drawText(50, 40, f"{current_name}'s Turn 💕")

        if self.dice_roll > 0:
            painter.drawPixmap(720, 45, self.dice_images[self.dice_roll])
            painter.drawText(735, 155, f"Roll: {self.dice_roll} ✨")
        else:
            painter.drawText(50, 90, "Press SPACE to roll with love!")

        # Victory detection
        winner = None
        for p in self.players:
            if self.rules.all_pieces_home(p):
                winner = p
                break

        if winner:
            self.game_state = "victory"
            painter.setPen(QColor(255, 80, 120))
            painter.setFont(QFont('Comic Sans MS', 24))
            painter.drawText(200, 300, f"💖 {winner.name} WON! 💖")
            painter.setFont(self.ui_font)
            painter.drawText(200, 350, "Thanks for playing!")

    def keyPressEvent(self, event):
        if self.game_state != "playing":
            return
        if event.key() == Qt.Key_Space and self.dice_roll == 0:
            self.dice_roll = self.roll_dice()
            print(f"🎲 {self.players[self.current_player_index].name} rolled a sparkling {self.dice_roll}!")

    def mousePressEvent(self, event):
        if self.game_state != "playing":
            return
        mx = event.position().x() if hasattr(event, 'position') else event.x()
        my = event.position().y() if hasattr(event, 'position') else event.y()
        clicked_square = self.board.get_clicked_square(mx, my, TILE_SIZE)
        if clicked_square is None:
            return

        current_player = self.players[self.current_player_index]
        opponent = self.players[1 - self.current_player_index]

        if self.selected_piece_index is None:
            self.selected_piece_index = self.rules.try_select_piece(
                current_player, clicked_square, self.dice_roll
            )
        else:
            move_success = self.rules.try_move(
                current_player,
                self.selected_piece_index,
                clicked_square,
                self.dice_roll,
                self.board,
                opponent,
            )
            if move_success:
                landed_pos = current_player.pieces[self.selected_piece_index]
                if landed_pos < 20 and self.board.is_rosette(landed_pos):
                    print("🌸 Rosette magic! Extra turn filled with love!")
                else:
                    self.current_player_index = 1 - self.current_player_index
                    self.dice_roll = 0
            self.selected_piece_index = None

    def roll_dice(self):
        return sum(random.randint(0, 1) for _ in range(4))


def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("🌸 Urzula — Royal Game of Ur in Qt 🌸")
    widget = GameWidget()
    win.setCentralWidget(widget)
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
