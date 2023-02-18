from Complex import Complex
from .base_repository import *


class TextFileRepository(BaseRepository):
    def __init__(self, file_name: str):
        super(TextFileRepository, self).__init__()
        self._file_name = file_name

    def add(self, complex_number):
        complex_number_list = self.get_all()
        complex_number_list.append(complex_number)
        self.write(complex_number_list)

    def remove_by_complex_number(self, complex_number):
        complex_number_list = self.get_all()
        complex_number_list.remove(complex_number)
        self.write(complex_number_list)

    def remove_all(self):
        open(self._file_name, 'w').close()

    def get_all(self):
        output = []
        file = open(self._file_name, 'r')

        lines = file.read()
        lines = lines.splitlines()
        for l in lines:
            values = l.split(',')
            complex_number = Complex(int(values[0]), int(values[1]))
            output.append(complex_number)

        file.close()
        return output

    def write(self, complex_number_list: list):
        file = open(self._file_name, "w")

        lines = self.split_in_lines(complex_number_list)

        for l in lines:
            file.write(l)
            file.write("\n")

        file.close()

    def split_in_lines(self, complex_number_list: list):
        lines = []
        for complex_number in complex_number_list:
            lines.append(f"{complex_number.get_real_part()},{complex_number.get_imaginary_part()}")
        return lines
