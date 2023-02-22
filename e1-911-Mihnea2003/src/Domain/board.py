from texttable import Texttable


class Board:

    def __init__(self):
        self._columns = 6
        self._rows = 6
        self._player_board = [[' ' for col in range(self._columns)] for row in range(self._rows)]

    @property
    def player_board(self):
        return self._player_board

    @property
    def columns(self):
        return self._columns

    @property
    def rows(self):
        return self._rows

    def get_board(self):
        return self._player_board

    def place_piece_player(self, row, column, piece):
        """
        Place X or 0 on the board
        :param row:
        :param column:
        :param piece:
        :return:Placing the piece on board or error
        """
        self.verify_placing_on_board(row, column, piece)
        self._player_board[row][column] = piece

    def verify_placing_on_board(self, row, column, piece):
        """
        Raise error if you put a letter and not a number
        or the rows or the columns is larger than 5 or if in the space that you want to put a symbol
        already is occupied
        :param row:
        :param column:
        :param piece:
        :return:
        """
        if not int(row) and row != 0:
            raise ValueError("Wrong row!")
        if not int(column) and column != 0:
            raise ValueError("Wrong column!")
        if row < 0 or row > 5:
            raise ValueError("Wrong row,the rows are between 0-5!")
        if column < 0 or column > 5:
            raise ValueError("Wrong column,the columns are between 0-5!")
        if piece != "X" and piece != "0":
            raise ValueError("You need to put X or 0!")
        if self._player_board[row][column] != ' ':
            raise ValueError("This space already has a symbol!")

    def __str__(self):
        t = Texttable()

        header = ['X']
        for r in range(self._columns):
            header.append(r)

        t.header(header)
        for r in range(self._rows):
            t.add_row([r]+self._player_board[r])

        return t.draw()

    def is_free(self, row, column):
        return self._player_board[row][column] == ' '
