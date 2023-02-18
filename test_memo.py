from repositories.memory_repository import *
from Complex import *


def test_add():
    repo = MemoryRepository()

    complex_number = Complex(1, 2)
    repo.add(complex_number)

    complex_numbers = repo.get_all()

    assert complex_numbers[0] == complex_number


def test_get_all():
    repo = MemoryRepository()
    complex_number1 = Complex(3, 2)
    complex_number2 = Complex(4, 4)
    numbers_expected = [complex_number1, complex_number2]

    repo.add(complex_number1)
    repo.add(complex_number2)

    numbers_actual = repo.get_all()

    assert numbers_actual[0] == numbers_expected[0] and numbers_actual[1] == numbers_expected[1]


def test_remove_all():
    repo = MemoryRepository()

    complex_number = Complex(1, 2)
    repo.add(complex_number)

    repo.remove_all()

    complex_numbers = repo.get_all()

    assert complex_numbers == []


test_add()
test_get_all()
test_remove_all()

