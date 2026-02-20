class Rules:
    """
    Gentle Finkel Rules for Urzula 💕
    Wrapped in love, just like our beautiful morning game!
    - 4 dice = 0–4 move
    - Enter from reserve by clicking the square your roll wants
    - Exact roll distance always
    - Rosettes = safe + extra turn with joy!
    - Capture only on non-rosette squares (with kindness)
    - Exact roll to reach home (position 20)
    """

    def __init__(self):
        print("🌸 Gentle Finkel Rules loaded with so much love and sparkles!")

    def try_select_piece(self, player, clicked_square, dice_roll):
        """Select a piece — either from your cozy reserve or on the board"""
        if dice_roll <= 0 or dice_roll > 4:
            return None

        # Entering a new piece from hand — click the exact square your roll wants!
        if any(p == -1 for p in player.pieces):
            intended_entry = dice_roll - 1
            if clicked_square == intended_entry:
                for i in range(7):
                    if player.pieces[i] == -1:
                        print(f"🌟 {player.name} brings a new happy piece onto the board!")
                        return i

        # Select an existing piece on the board
        for i, pos in enumerate(player.pieces):
            if pos == clicked_square and 0 <= pos < 20:
                intended = pos + dice_roll
                if intended <= 20:
                    print(f"💖 Selected piece {i+1} — ready for a joyful hop!")
                    return i
        return None

    def try_move(self, player, piece_index, target_square, dice_roll, board, opponent=None):
        """Execute the move with full gentle rules"""
        if piece_index is None:
            return False

        current_pos = player.pieces[piece_index]

        if current_pos == -1:  # Entering
            intended_pos = dice_roll - 1
        else:
            intended_pos = current_pos + dice_roll

        # Exact finish — click anywhere after selecting the piece!
        if intended_pos == 20:
            player.move_piece(piece_index, 20)
            print(f"💖 {player.name} finished a piece home with perfect love!")
            return True

        # Normal move must land exactly where clicked
        if intended_pos != target_square or intended_pos > 19:
            return False

        # Can't land on your own piece
        if player.has_piece_at(intended_pos):
            return False

        # Gentle capture (only if not on rosette)
        if opponent and opponent.has_piece_at(intended_pos) and not board.is_rosette(intended_pos):
            for i in range(7):
                if opponent.pieces[i] == intended_pos:
                    opponent.move_piece(i, -1)
                    print("🌼 Gentle capture! Piece returns home safely with a smile 💕")
                    break

        # Move the piece!
        player.move_piece(piece_index, intended_pos)
        return True

    def all_pieces_home(self, player):
        """Victory check — just like your wonderful 6-piece win!"""
        return player.all_pieces_home()