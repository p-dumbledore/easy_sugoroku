import random

class Actor:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.position = 1

    def plus_pos(self, pos):
        self.position += pos

    def minus_pos(self, pos):
        self.position -= pos

    def get_pos(self):
        return self.position

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name


player = Actor('player', 'P')
computer = Actor('computer', 'C')

REST = '*'
ALL = 30

def board():
    print(REST*(player.get_pos()-1) + player.get_symbol() + REST*(ALL-player.get_pos()) + 'Goal')
    print(REST*(computer.get_pos()-1) + computer.get_symbol() + REST*(ALL-computer.get_pos()) + 'Goal')

def main_process(actor):
    pos_minus = 0
    print("Turn: " + actor.get_name())
    pos_plus = random.randint(1, 6)
    if actor.get_pos() + pos_plus > 30:
        pos_minus = abs(30 - (actor.get_pos() + pos_plus))
    else:
        actor.plus_pos(pos_plus)
        if actor.get_pos() == 30:
            return [1, actor]
    actor.minus_pos(pos_minus)
    board()
    return [0, actor]

def check_result(n, actor):
    if n:
        print(actor.get_name() + " Won!")
        exit()

print("Sugoroku, Start!")
board()
while True:
    rand = random.randint(0, 1)
    if not rand:
        actor1 = player
        actor2 = computer
    else:
        actor1 = computer
        actor2 = player

    # actor1 turn
    check_result(main_process(actor1)[0], main_process(actor1)[1])
    check_result(main_process(actor2)[0], main_process(actor2)[1])
