from domain import Player


class TextFileRepo(Player):
    def __init__(self, file_name: str):
        super(TextFileRepo, self).__init__()
        self._file_name = file_name

    def get_all(self):
        output = []
        file = open("tennis", 'r')

        lines = file.read()
        lines = lines.splitlines()
        for l in lines:
            values = l.split(',')
            player = Player(int(values[0]), values[1], int(values[2]))
            output.append(player)

        file.close()
        return output

    def write(self, players_list: list):
        file = open("tennis", "w")

        lines = self.split_in_lines(self, players_list)

        for l in lines:
            file.write(l)
            file.write("\n")

        file.close()

    def split_in_lines(self, players_list: list):
        lines = []
        for player in players_list:
            lines.append(f"{player.get_id()},{player.get_name()},{player.get_strength()}")
        return lines
