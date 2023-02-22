import random

class Player:
    def __init__(self, id, name, strength):
        self._id = id
        self._name = name
        self._strength = strength

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_strength(self):
        return self._strength

    def set_strength(self, strength):
        self._strength = strength

    def __str__(self):
        return f"{self._id},{self._name},{self._strength} "


class Pairs:
    def __init__(self, player1, player2):
        self._player1 = player1
        self._player1 = player2

