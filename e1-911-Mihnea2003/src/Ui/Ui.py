from src.Domain.board import Board
from src.Service.service import Service


class Ui:
    def __init__(self, player_board: Board, service: Service):
        self.__player_board = player_board
        self._service = service

    def choose_place_piece(self):
        print(self.__player_board)
        while True:
            command = input('(row,column,piece):')
            command = command.split(',')
            try:
                if len(command) != 3:
                    while True:
                        print("Wrong command")
                        command = input("(row,column,piece):")
                        if len(command) == 3:
                            break
                self.__player_board.place_piece_player(int(command[0]), int(command[1]), command[2])
            except ValueError as ve:
                print(ve)
            print(self.__player_board)
            self._service.choose_computer_move()
            print(self.__player_board)
            verification_player = self._service.verification_for_player()
            verification_computer = self._service.verification_for_computer()

            if verification_player:
                print("Player wins!")
                return
            else:
                if verification_computer:
                    print("Computer wins!")
                    return
