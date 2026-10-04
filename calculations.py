

def calculate_average(list_of_numbers):
    summa = 0
    for number in list_of_numbers:
        summa = summa + number
    return summa / len(list_of_numbers)


def find_max(list_of_numbers):
    max_number = -float('inf')
    for number in list_of_numbers:
        max_number = max(max_number, number)
    return max_number


def count_positive(list_of_numbers):
    count = 0
    for number in list_of_numbers:
        if number > 0:
            count = count + 1
    return count
