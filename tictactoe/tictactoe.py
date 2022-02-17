import random


class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Welcome to TicTacToe!\nPlayer 1 is X and Player 2 is 0\nTake turns placing your pieces - the first to "
              "3 in a row wins!")

    def print_board(self):
        # TODO: Print the board
        print("\t0\t1\t2")
        for row in range(len(self.board)):
            row_string = str(row) + "\t"
            for col in range(len(self.board[0])):
                row_string += self.board[row][col] + "\t"
            print(row_string)

    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        if 0 <= row <= len(self.board) - 1 and 0 <= col <= len(self.board[0]) - 1:
            if self.board[row][col] == "-":
                return True
        return False

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        input_row = int(input("Enter a row: "))
        input_col = int(input("Enter a col: "))

        while not self.is_valid_move(input_row, input_col):
            print("Please enter a valid move.")
            input_row = int(input("Enter a row: "))
            input_col = int(input("Enter a col: "))

        self.place_player(player, input_row, input_col)

    def take_random_turn(self, player):
        rand_row = random.randint(0, 2)
        rand_col = random.randint(0, 2)
        while not self.is_valid_move(rand_row, rand_col):
            rand_row = random.randint(0, 2)
            rand_col = random.randint(0, 2)
        print("Enter a row: " + str(rand_row))
        print("Enter a col: " + str(rand_col))
        self.place_player(player, rand_row, rand_col)

    def take_turn(self, player, depth):
        # TODO: Simply call the take_manual_turn function
        print(str(player) + "'s Turn")
        if player == "X":
            self.take_manual_turn(player)
        else:
            self.take_minimax_turn(player, depth)

    def check_col_win(self, player):
        # TODO: Check col win
        if self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player:
            return True
        if self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player:
            return True
        if self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player:
            return True
        return False

    def check_row_win(self, player):
        # TODO: Check row win
        if self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player:
            return True
        if self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player:
            return True
        if self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player:
            return True
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    def check_win(self, player):
        # TODO: Check win
        return self.check_row_win(player) or self.check_col_win(player) or self.check_diag_win(player)

    def check_tie(self):
        # TODO: Check tie
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == "-":
                    return False
        return True

    def play_game(self):
        # TODO: Play game
        game = True
        depth = 6
        player = "X"
        self.print_instructions()
        self.print_board()
        while game:
            self.take_turn(player, depth)
            self.print_board()
            if self.check_win(player):
                print(str(player) + " wins!")
                game = False
            elif self.check_tie():
                print("Tie game!")
                game = False
            else:
                if player == "X":
                    player = "O"
                else:
                    player = "X"

    def minimax(self, player, depth):
        opt_row = -1
        opt_col = -1
        if self.check_win("O"):
            return 10, None, None
        elif self.check_win("X"):
            return -10, None, None
        elif self.check_tie() or depth == 0:
            return 0, None, None
        if player == "O":
            best = -100
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    if self.board[row][col] == "-":
                        self.place_player(player, row, col)
                        score = self.minimax("X", depth-1)[0]
                        self.place_player("-", row, col)
                        if best < score:
                            opt_row = row
                            opt_col = col
                            best = score
            return best, opt_row, opt_col
        if player == "X":
            worst = 100
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    if self.board[row][col] == "-":
                        self.place_player(player, row, col)
                        score = self.minimax("O", depth-1)[0]
                        self.place_player("-", row, col)
                        if worst > score:
                            opt_row = row
                            opt_col = col
                            worst = score
            return worst, opt_row, opt_col

    def take_minimax_turn(self, player, depth):
        score, row, col = self.minimax(player, depth)
        # print("Score: ", score, "Row: ", row, "Col: ", col)
        print("Enter a row: " + str(row))
        print("Enter a col: " + str(col))
        self.place_player(player, row, col)
