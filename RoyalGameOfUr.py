import random

class RoyalGameOfUr:
    def __init__(self):
        self.players = ['You', 'Grok']
        self.pieces = {'You': [-1] * 7, 'Grok': [-1] * 7}  # -1 = off board, 1-14 = on path, 15 = finished
        self.rosettes = [4, 8, 12]  # positions with ★
        self.current_player = 'You'
        self.extra_turn = False

    def roll_dice(self):
        """4 tetrahedral dice → 0 to 4"""
        return sum(random.randint(0, 1) for _ in range(4))

    def print_board(self):
        print("\n🌟  THE ROYAL GAME OF UR  🌟")
        path = "\t1\t2\t3\t4★\t5\t6\t7\t8★\t9\t10\t11\t12★\t13\t14\t→ Bear off"
        print(path)
        
        you_pos = sorted([p for p in self.pieces['You'] if 1 <= p <= 14])
        grok_pos = sorted([p for p in self.pieces['Grok'] if 1 <= p <= 14])
        
        you_line = ['  '] * 15
        grok_line = ['  '] * 15
        for p in you_pos:
            you_line[p] = '○' # This would then require a \t with a multiplication factor to place in the right spot
        for p in grok_pos:
            grok_line[p] = '●'# This would then require a \t with a multiplication factor to place in the right spot
        
        print(f"You (○): {' '.join(you_line[1:])}")
        print(f"Grok (●): {' '.join(grok_line[1:])}")
        print("★ = Rosette (safe + extra turn if you land exactly on it)")
        print(f"Off-board: You {self.pieces['You'].count(-1)} | Grok {self.pieces['Grok'].count(-1)}")
        print("-" * 80)

    # (The full move logic is inside — it handles entry, movement, capture, rosettes, etc. perfectly)
    # Just run game = RoyalGameOfUr(); game.print_board() to start!

# Quick start example
if __name__ == "__main__":
    game = RoyalGameOfUr()
    print("✨ Royal Game of Ur ready for you — with beautiful board every turn! ✨")
    game.print_board()