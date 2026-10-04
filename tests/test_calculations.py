from calculations import calculate_average, count_positive, find_max

def test_average_positive():
    assert calculate_average([10, 20, 30]) == 30

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