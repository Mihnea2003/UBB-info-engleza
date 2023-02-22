from Domain.board import Board
from src.Ui.Ui import Ui
from src.Service.service import Service


def start_game():
    board = Board()

    service = Service(board)

    ui = Ui(board, service)

    ui.choose_place_piece()


start_game()
