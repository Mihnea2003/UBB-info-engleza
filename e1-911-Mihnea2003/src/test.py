from Domain.board import Board
from src.Ui.Ui import Ui
from src.Service.service import Service


def test_for_computer_placing():
    board = Board()

    service = Service(board)
    matrix = board.get_board()

    row = 3
    column = 3
    piece = 'X'
    service.computer_place(row, column, piece)
    row1 = 2
    column1 = 2
    piece1 = '0'
    service.computer_place(row1, column1, piece1)
    assert matrix[row][column] == 'X'
    assert matrix[row1][column1] == '0'


test_for_computer_placing()
