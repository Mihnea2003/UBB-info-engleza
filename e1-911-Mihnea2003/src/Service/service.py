import random
from src.Domain.board import Board


class Service:
    def __init__(self, player_board:Board):
        self._player_board = player_board

    def verification_for_computer(self):
        player_board = self._player_board.get_board()
        for row in range(6):
            for column in range(6):
                if player_board[row][column] == ' ':
                    return False
        return True

    def verify_rows(self):
        matrix = self._player_board.get_board()
        for col in range(6):
            check = 0
            for row in range(5):
                if matrix[row][col] != ' ' and matrix[row][col] == matrix[row + 1][col]:
                    check += 1
                    if check == 4:
                        return True
                else:
                    check = 0

    def verify_first_diagonal(self):
        matrix = self._player_board.get_board()
        check = 0
        for col in range(5):

            if matrix[col][col] == matrix[col + 1][col + 1] and matrix[col][col] != ' ':
                check += 1

                if check == 4:
                    return True
            else:
                check = 0

    def verify_upper_diagonal(self):
        matrix = self._player_board.get_board()
        row = 0
        check = 0
        for col in range(1, 5):
            if matrix[row][col] == matrix[row + 1][col + 1] and matrix[row][col] != ' ':
                check += 1
                if check == 4:
                    return True
            else:
                check = 0
            if row <= 3:
                row += 1
            else:
                break

    def verify_lower_diagonal(self):
        matrix = self._player_board.get_board()
        check = 0
        row = 1
        for col in range(4):
            if matrix[row][col] == matrix[row + 1][col + 1] and matrix[row][col] != ' ':
                check += 1
                if check == 4:
                    return True
            else:
                check = 0
            if row <= 4:
                row += 1
            else:
                break

    def verify_columns(self):
        matrix = self._player_board.get_board()
        for row in range(6):
            check = 0
            for col in range(5):
                if matrix[row][col] != ' ' and matrix[row][col] == matrix[row][col + 1]:
                    check += 1
                    if check == 4:
                        return True
                else:
                    check = 0

    def verify_secondary_diagonal(self):
        matrix = self._player_board.get_board()
        row = 0
        check = 0
        for col in range(5, 0, -1):
            if matrix[row][col] == matrix[row + 1][col - 1] and matrix[row][col] != ' ':

                check += 1
                if check == 4:
                    return True
            else:
                check = 0

            if row <= 4:
                row += 1
            else:
                break

    def verify_lower_secondary_diagonal(self):
        matrix = self._player_board.get_board()
        row = 0
        check = 0
        for col in range(4, 0, -1):
            if matrix[row][col] == matrix[row + 1][col - 1] and matrix[row][col] != ' ':

                check += 1
                if check == 4:
                    return True
            else:
                check = 0

            if row <= 3:
                row += 1
            else:
                break

    def verify_upper_secondary_diagonal(self):
        matrix = self._player_board.get_board()
        row = 1
        check = 0
        for col in range(5, 1, -1):
            if matrix[row][col] != ' ':
                if matrix[row][col] == matrix[row + 1][col - 1]:

                    check += 1
                    if check == 4:
                        return True
                else:
                    check = 0
            else:
                check = 0

            if row <= 4:
                row += 1
            else:
                break

    def verification_for_player(self):
        if self.verify_rows() or self.verify_columns() or self.verify_first_diagonal() or self.verify_upper_diagonal():
            return True
        if self.verify_lower_diagonal() or self.verify_secondary_diagonal() or self.verify_lower_secondary_diagonal():
            return True
        if self.verify_upper_secondary_diagonal():
            return True

    def computer_place(self, row, column, piece):
        """
        Places the piece into the player board
        :return: the piece placed
        """
        self._player_board.place_piece_player(row, column, piece)

    def choose_computer_move(self):
        """
        This function choose in a random way where to put a random piece and it verifies if that space is empty
        :return: a list with row,column,piece
        """
        matrix = self._player_board.get_board()
        check = 0
        while check == 0:
            row = random.randint(0, 5)
            column = random.randint(0, 5)
            if matrix[row][column] == ' ':
                check = 1
        piece = random.randint(0, 1)
        if piece == 0:
            piece = 'X'
        else:
            piece = '0'
        self.computer_place(row, column, piece)









