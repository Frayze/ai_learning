import random
class PlayerBrain:
    
    def __init__(self, player):
        self.player = player;
        self.moves = []
        self.step = 0

    def get_move(self):
        if self.step < len(self.moves):
            return self.moves[self.step]
        else:
            next_move = self.random_move()
            self.moves.append(next_move)
            self.step += 1
            return self.moves[self.step - 1]


    def random_move(self):
        rand = random.Random()
        move = [rand.randint(-10, 10), rand.randint(-10, 10)]
        return move