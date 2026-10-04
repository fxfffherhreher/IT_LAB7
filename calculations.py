def calculate_average(list_of_numbers):
    if not list_of_numbers:
        raise ValueError("Список не должен быть пустым")

    summa = 0
    for number in list_of_numbers:
        summa = summa + number
    return summa / len(list_of_numbers)


def find_max(list_of_numbers):
    max_number = -float("inf")
    for number in list_of_numbers:
        max_number = max(max_number, number)
    return max_number


def count_positive(list_of_numbers):
    count = 0
    for number in list_of_numbers:
        if number > 0:
            count = count + 1
    return count


def analyze(list_of_numbers):
    if len(list_of_numbers) == 0:
        return None
    summa = 0
    max_number = -float("inf")
    min_number = float("inf")
    for number in list_of_numbers:
        summa += number
        max_number = max(max_number, number)
        min_number = min(min_number, number)

    return min_number, max_number, summa / len(list_of_numbers)
