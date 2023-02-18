from Complex import Complex
from .base_repository import *


class MemoryRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self._complex_numbers_list = []

    def add(self, complex_number):
        self._complex_numbers_list.append(complex_number)

    def remove_by_complex_number(self, complex_number):
        self._complex_numbers_list.remove(complex_number)

    def remove_all(self):
        self._complex_numbers_list.clear()

    def get_all(self):
        return self._complex_numbers_list
