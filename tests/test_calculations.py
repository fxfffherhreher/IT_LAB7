import pytest

from calculations import analyze, calculate_average, count_positive, find_max


def test_analyze_mixed_numbers():
    assert analyze([3, -2, 7, 0]) == (-2, 7, 2)


def test_analyze_all_positive():
    assert analyze([5, 10, 15]) == (5, 15, 10)


def test_analyze_all_negative():
    assert analyze([-5, -10, -15]) == (-15, -5, -10)


def test_analyze_single_value():
    assert analyze([4]) == (4, 4, 4)


def test_analyze_equal_values():
    assert analyze([2, 2, 2]) == (2, 2, 2)


def test_analyze_float_average():
    assert analyze([1, 2]) == (1, 2, 1.5)


def test_analyze_empty_list():
    assert analyze([]) is None


def test_average_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])


def test_average_positive():
    assert calculate_average([10, 20, 30]) == 20


def test_average_single_value():
    assert calculate_average([5]) == 5


def test_average_negative():
    assert calculate_average([-10, 0, 10]) == 0


def test_zero_count_positive():
    assert count_positive([-4, -10, -34566]) == 0


def test_none_count_positive():
    assert count_positive([]) == 0


def test_count_positive():
    assert count_positive([-4, -10, 3]) == 1


def test_find_max_negative():
    assert find_max([-3, -4, -344]) == -3


def test_find_max_positive():
    assert find_max([1, 4, 6]) == 6


def test_find_max():
    assert find_max([-3, -4, -344, 1, 4, 6]) == 6
