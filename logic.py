#!/usr/bin/python3

# Board layout
#0 | 1 | 2
#3 | 4 | 5
#6 | 7 | 8
#


class Board:
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    def __init__(self):
        self.game_end = False
        self.winner = None
        self.tied = False
        self.positions = ['.']*9


    def get_available_moves(self):
        moves = [index for index, position in enumerate(self.positions) if position == '.']
        return moves

    def make_move(self, position, player):
        self.positions[position] = player
        return self.positions

    def game_over(self):
        if self.positions[0] == 'X' and self.positions[1] == 'X' and self.positions[2] == 'X':
            self.game_end = True
            self.winner = 'X'
        elif self.positions[3] == 'X' and self.positions[4] == 'X' and self.positions[5] == 'X':
            self.game_end = True
            self.winner = 'X'
        elif self.positions[6] == 'X' and self.positions[7] == 'X' and self.positions[8] == 'X':
            self.game_end = True
            self.winner = 'X'
        elif self.positions[0] == 'X' and self.positions[3] == 'X' and self.positions[6] == 'X':
            self.game_end = True
            self.winner = 'X'
        elif self.positions[1] == 'X' and self.positions[4] == 'X' and self.positions[7] == 'X':
            self.game_end = True
            self.winner = 'X'
        elif self.positions[2] == 'X' and self.positions[5] == 'X' and self.positions[8] == 'X':
            self.game_end = True
            self.winner = 'X'
        elif self.positions[0] == 'X' and self.positions[4] == 'X' and self.positions[8] == 'X':
            self.game_end = True
            self.winner = 'X'
        elif self.positions[2] == 'X' and self.positions[4] == 'X' and self.positions[6] == 'X':
            self.game_end = True
            self.winner = 'X'
        elif self.positions[0] == '0' and self.positions[1] == '0' and self.positions[2] == '0':
            self.game_end = True
            self.winner = '0'
        elif self.positions[3] == '0' and self.positions[4] == '0' and self.positions[5] == '0':
            self.game_end = True
            self.winner = '0'
        elif self.positions[6] == '0' and self.positions[7] == '0' and self.positions[8] == '0':
            self.game_end = True
            self.winner = '0'
        elif self.positions[0] == '0' and self.positions[3] == '0' and self.positions[6] == '0':
            self.game_end = True
            self.winner = '0'
        elif self.positions[1] == '0' and self.positions[4] == '0' and self.positions[7] == '0':
            self.game_end = True
            self.winner = '0'
        elif self.positions[2] == '0' and self.positions[5] == '0' and self.positions[8] == '0':
            self.game_end = True
            self.winner = '0'
        elif self.positions[0] == '0' and self.positions[4] == '0' and self.positions[8] == '0':
            self.game_end = True
            self.winner = '0'
        elif self.positions[2] == '0' and self.positions[4] == '0' and self.positions[6] == '0':
            self.game_end = True
            self.winner = '0'
        elif self.get_available_moves() == None:
            self.tied = True
            self.winner = None
        else:
            self.game_end = False
            self.winner = None
        return self.game_end, self.winner

    def update_state(self, board, step, player):
        board = list(board)
        board[step] = player
        return board



class Program:
    def __init__(self, board, player):
        self.game = board
        self.choice = None
        self.player = player


    def winning_result(self, player):
        # -10 program looses
        # 10 program wins
        # 0 draw

        if self.player == 'X':
            return 10
        elif self.player == '0':
            return 10
        else:
            return 0


    def minimax(self, board, player):
        state, winner = self.game.game_over()
        moves = []
        scores = []

        if state is True:
            result = self.winning_result(player)
            return result

        for move in board.get_available_moves():
            board.make_move(move, player)
            score = self.minimax(board, self.get_opponent(player))
            scores.append(score)
            moves.append(move)
            board.make_move(move, '.')
            print(score)
            if player == '0':
                max_index = scores.index(max(scores))
                self.choice = moves[max_index]
                return max(scores)
            else:
                min_index = scores.index(min(scores))
                self.choice = moves[min_index]
                return min(scores)

    def get_opponent(self, player):
        # X is always the maximizing player
        # 0 is always the minimizing player
        if player == 'X':
            opponent = '0'
            return opponent
        else:
            opponent = 'X'
            return opponent