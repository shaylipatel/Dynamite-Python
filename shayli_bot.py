import random

class ShayliBot:
    def __init__(self):
        self.dynamite = 100
        self.moves = ['R', 'P' ,'S' ,'D', 'W']
        self.round = -1
        self.opponents_moves = []

    def make_move(self, gamestate):
        if self.round >= 0:
            self.opponents_moves.append(gamestate['rounds'][self.round]['p2'])
        move = self.analyse_last_three_moves()
        if move == 'D':
            self.dynamite -= 1
        if self.dynamite == 0 and 'D' in self.moves:
            self.moves = ['R', 'P' ,'S']
        self.round += 1
        return move
    
    def analyse_last_three_moves(self):
        if self.round >=2:
            if self.opponents_moves[self.round] == self.opponents_moves[self.round -1] and self.opponents_moves[self.round] == self.opponents_moves[self.round -2]:
                match self.opponents_moves[self.round]:
                    case 'D':
                        return 'W'
                    case 'R':
                        return 'P'
                    case 'S':
                        return 'R'
                    case 'P':
                        return 'S'
                    case 'W':
                        return random.choice(['R', 'P' ,'S'])
            else:
                return random.choice(self.moves)
        else:
            return random.choice(self.moves)
        
                    