import repository
from repository import TextFileRepo
import domain


class Services(TextFileRepo):
    def __init__(self):
        super(Services, self).__init__()

    def descending_order_strength(self):
        players_list = self.get_all(self)
        for l in players_list:
            for r in players_list:
                if self.get_strength(players_list[l]) < self.get_strength(players_list[r]):
                    aux = players_list[l]
                    players_list[l] = players_list[r]
                    players_list[r] = players_list[aux]
        return players_list

    def number_of_players_remaining(self):
        players_list = self.get_all(self)
        i = 0
        for player in players_list:
            i += 1
        return i

    def update_the_strength(self):
        players_list = self.get_all()
        for l in players_list:
            self.set_id(players_list[l], self.get_id(players_list[l]+1))
        self.write(self, players_list)

    def delete_player(self,player_lost):
        players_list = self.get_all(self)
        new_players_list= []
        for player in players_list:
            if player!=player_lost:
                new_players_list.append(player)
        self.write(self, new_players_list)











