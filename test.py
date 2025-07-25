from sum_of_two_numbers_in_array import find_two_numbers_for_given_sum


def test(func):
    # тест из условия задачи
    assert func([2, 4, 8, 9, 11, 12, 16, 21], 19) == (8, 11)

    # подходит несколько пар, алгоритм должен вернуть первую подходящую
    assert func([1, 2, 3, 4], 5) == (1, 4)

    # проверка случая, когда два одинаковых числа дают нужную сумму
    assert func([3, 3, 5], 6) == (3, 3)

    # правильной пары числе нет
    assert find_two_numbers_for_given_sum([1, 2], 4) == None

    # первые числа подходят
    assert func([2, 4, 5, 6], 8) == (2, 6)

    # перебор до середины (четное число элементов)
    assert func([1, 1, 4, 5, 6, 7], 9) == (4, 5)

    # перебор до середины (нечетное число элементов)
    assert func([1, 4, 5, 6, 7], 9) == (4, 5)

    # 2 элемента
    assert func([1, 7], 8) == (1, 7)

    # 1 элемент None
    assert func([1], 2) == None

    # 0 элементов None
    assert func([], 1) == None

    # дубликаты
    assert func([2, 2, 3], 5) == (2, 3)

    # отрицательные числа
    assert func([-5, 0, 5], 0) == (-5, 5)


if __name__ == "__main__":
    test(find_two_numbers_for_given_sum)
