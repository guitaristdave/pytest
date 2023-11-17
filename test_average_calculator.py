import pytest

from average_calculator import AverageCalculator, compare_averages


@pytest.fixture
def average_calculator():
    return AverageCalculator()

def test_calculate_average_empty_list(average_calculator):
    assert average_calculator.calculate_average([]) == 0

def test_calculate_average(average_calculator):
    assert average_calculator.calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_compare_averages_greater():
    assert compare_averages([1, 2, 3], [1, 2, 3, 4]) == "Второй список имеет большее среднее значение"

def test_compare_averages_lesser():
    assert compare_averages([1, 2, 3, 4], [1, 2, 3]) == "Первый список имеет большее среднее значение"

def test_compare_averages_equal():
    assert compare_averages([1, 2, 3], [3, 2, 1]) == "Средние значения равны"
