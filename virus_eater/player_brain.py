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
        s_const = 5
        rand = random.Random()
        move = [0, 0]

        #empty movement list
        if len(self.moves) < 1:
            move[0] = rand.randint(-1 * s_const, s_const)
            move[1] = rand.randint(-1 * s_const, s_const)
            return move

        previous = self.moves[-1]
        #more fluent movement
        #x_direction
        if previous[0] < 0:
            move[0] = rand.randint(-2 * s_const, 0)
        elif previous[0] > 0:
            move[0] = rand.randint(0, 2 * s_const)
        else:
            move[0] = rand.randint(-1 * s_const, s_const)

        #y_direction
        if previous[1] < 0:
            move[1] = rand.randint(-2 * s_const, 0)
        elif previous[1] > 0:
            move[1] = rand.randint(0, 2 * s_const)
        else:
            move[1] = rand.randint(-1 * s_const, s_const)
        return move