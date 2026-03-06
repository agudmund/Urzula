from PySide6.QtGui import QPixmap, QColor


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color  # kept for future fun
        self.pieces = [-1] * 7

        player_key = "player1" if "Love" in name or "Sweet" in name else "player2"
        self.piece_image = QPixmap(f'assets/images/pieces/{player_key}_piece.png')

    def all_pieces_home(self):
        return all(pos >= 20 for pos in self.pieces)

    def count_finished(self):
        return sum(1 for pos in self.pieces if pos >= 20)

    def get_pieces_on_board(self):
        return [i for i, pos in enumerate(self.pieces) if 0 <= pos < 20]

    def has_piece_at(self, square):
        return any(pos == square for pos in self.pieces)

    def move_piece(self, piece_index, new_pos):
        if 0 <= piece_index < 7:
            self.pieces[piece_index] = new_pos

    def draw(self, painter, board, tile_size):
        # On-board pieces — use QPixmap if available
        for idx, pos in enumerate(self.pieces):
            if 0 <= pos < 20:
                base_x, base_y = board.positions[pos]
                off_x = (idx % 3 - 1) * 6
                off_y = (idx % 2) * -5
                piece_size = tile_size - 24
                if not self.piece_image.isNull():
                    scaled = self.piece_image.scaled(piece_size, piece_size)
                    painter.drawPixmap(base_x + 12 + off_x, base_y + 12 + off_y, scaled)
                else:
                    painter.setBrush(QColor(*self.color))
                    painter.drawEllipse(base_x + 12 + off_x, base_y + 12 + off_y, piece_size, piece_size)

        # Reserve pieces — cute stacked sprites
        base_x = 55
        base_y = 510 if "Sweet" in self.name or "Love" in self.name else 95
        remaining = sum(1 for p in self.pieces if p == -1)
        for i in range(remaining):
            x = base_x + (i % 3) * 22
            y = base_y + (i // 3) * 22
            if not self.piece_image.isNull():
                small = self.piece_image.scaled(38, 38)
                painter.drawPixmap(x, y, small)
            else:
                painter.setBrush(QColor(*self.color))
                painter.drawEllipse(x, y, 38, 38)
