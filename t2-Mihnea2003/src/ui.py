from domain import Player
from repository import TextFileRepo
from services import Services
import repository


class UI(Services):
    def show_all(self):
        players_list = repository.TextFileRepo.get_all()
        for player in players_list:
            print(player)

    def show_descending_order(self):
        players_list = self.descending_order_strength(self)
        for player in players_list:
            print(player)

    def choose_who_wins(self):
        players_list = self.get_all(self)
        i = 1
        j = 2
        while j <= len(players_list):
            print("Who should win?")
            print("1.", players_list[i])
            print("2.", players_list[j])
            option = input("Write your option > ")
            if option == "1":
                self.delete_player(self,players_list[j])
            else:
                self.delete_player(self,(players_list[i]))
            i += 1
            j += 1

    def start_game(self):
        while self.number_of_players_remaining(self) > 1:
            print("Last", self.number_of_players_remaining(self))
            self.choose_who_wins(self)
            self.update_the_strength(self)

    def start(self):
        print("1.Display tha players")
        print("2.Start the game")
        option = input("Write your option > ")
        if option == "1":
            players_list = self.repository.get_all()
            for player in players_list:
                print(player)
        else:
            self.start_game(self)


ui = UI()
ui.start(ui)




