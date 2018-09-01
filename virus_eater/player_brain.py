import random
import math
class PlayerBrain:

    
    def __init__(self, player):
        self.moves = []
        self.step = 0

    def get_move(self):
        self.step += 1
        if self.step - 1 < len(self.moves):
            return self.moves[self.step - 1]
        else:
            next_move = self.random_move()
            self.moves.append(next_move)
            return self.moves[self.step - 1]


    def random_move(self):
        s_const = 4
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

    def mutate(self, mutationrate):
        rand = random.Random()
        for m in self.moves:
            if rand.random() < mutationrate:
                m[0] += rand.randint(-20 * mutationrate, 20 * mutationrate)
            if rand.random() < mutationrate:
                m[1] += rand.randint(-20 * mutationrate, 20 * mutationrate)

    @staticmethod
    def selection(players):
        rand = random.Random()
        size = math.floor(0.1 * len(players))
        fitnesssum = 0

        for p in players:
            if p.score >= 0:
                fitnesssum += p.score
            else:
                players.remove(p)
        fittest = [players[0]]


        #randomly fittest player
        for i in range(size):
            index = rand.randint(0, fitnesssum)
            tmp = 0
            for p in players:
                if tmp <= index and tmp + p.score >= tmp:
                    fittest.append(p)
                    pass
                else:
                    tmp += p.score
            print("random fittest player: " + str(fittest[1].score))

        return fittest