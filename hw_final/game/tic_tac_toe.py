import os

class Cell():
    def __init__(self, num: int):
        self.filled = 0
        self.num = num

class Board():
    def __init__(self):
        self.board = [Cell(i) for i in range(9)]

    def update(self, player: "Player"):
        num = player.play(self)
        self.board[num - 1].filled = player.turn
        self.print_board()

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(3):
            for j in range(3):
                if self.board[i * 3 + j].filled == 0:
                    print("__", end=" ")
                elif self.board[i * 3 + j].filled == 1:
                    print("XX", end=" ")
                elif self.board[i * 3 + j].filled == 2:
                    print("OO", end=" ")
            print("\n\n")

    def check_win(self, player: "Player"):
        vars = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        if any([self.board[i[0]].filled == self.board[i[1]].filled == self.board[i[2]].filled and self.board[i[0]].filled != 0 for i in vars]):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Побеждает игрок {player.name}!")
            return False
        elif all(self.board[i].filled != 0 for i in range(9)):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Ничья!")
            return False
        return True
                
class Player():
    def __init__(self, name: str, turn: int):
        self.name = name
        self.turn = turn

    def play(self, board):
        while True:
            temp = int(input(f"Ход игрока '{self.name}': "))
            if 0 < temp < 10 and board.board[temp - 1].filled == 0:
                break
            else:
                print("Некорректный ход, попробуйте ещё раз: ")
        return temp
    
def game():
    board = Board()
    player1 = Player(input("Введите имя первого игрока: "), 1)
    player2 = Player(input("Введите имя второго игрока: "), 2)
    board.print_board()
    while True:
        if board.check_win(player2):
            board.update(player1)
            if board.check_win(player1):
                board.update(player2)
            else:
                break
        else:
            break