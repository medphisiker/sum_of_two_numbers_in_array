from solution import Solution


def test():
    # Пример 1 из условия задачи
    # Нужные элементы в самом начале
    #
    # Показываем положение указателей по выходу из метода
    # solution.twoSum(numbers, target)
    #
    #          l
    # numbers: 2 7 11 15
    #            r

    numbers = [2, 7, 11, 15]
    target = 9

    solution = Solution()
    assert solution.twoSum(numbers, target) == [1, 2]

    # Пример 2 из условия задачи
    # Указатели сразу на нужных местах.
    #
    #          l
    # numbers: 2 3 4
    #              r

    numbers = [2, 3, 4]
    target = 6

    solution = Solution()
    assert solution.twoSum(numbers, target) == [1, 3]

    # Пример 3 из условия задачи
    # Массив из 2х элементов (минимально возможный), отрицательные числа.
    #
    #           l
    # numbers: -1 0
    #             r

    numbers = [-1, 0]
    target = -1

    solution = Solution()
    assert solution.twoSum(numbers, target) == [1, 2]

    # Тест из условия задачи
    # Нужные элементы в самом конце
    #
    #                l
    # numbers: 1 2 3 4 5
    #                  r

    numbers = [1, 2, 3, 4, 5]
    target = 9

    solution = Solution()
    assert solution.twoSum(numbers, target) == [4, 5]

    # Тест
    # проверка случая, когда два одинаковых числа дают нужную сумму
    #
    #          l
    # numbers: 3 3 5
    #            r

    numbers = [3, 3, 5]
    target = 6

    solution = Solution()
    assert solution.twoSum(numbers, target) == [1, 2]

    # Тест
    # перебор до середины (четное число элементов)
    #
    #              l
    # numbers: 1 1 4 5 10 12
    #                r

    numbers = [1, 1, 4, 5, 10, 12]
    target = 9

    solution = Solution()
    assert solution.twoSum(numbers, target) == [3, 4]

    # Тест
    # перебор до середины (четное число элементов)
    #
    #              l
    # numbers: 1 1 4 5 10
    #                r

    numbers = [1, 1, 4, 5, 10]
    target = 9

    solution = Solution()
    assert solution.twoSum(numbers, target) == [3, 4]

    # Тест
    # отрицательные числа
    #
    #           l
    # numbers: -5 -1 0 5 10
    #                  r

    numbers = [-5, -1, 0, 5, 10]
    target = 0

    solution = Solution()
    assert solution.twoSum(numbers, target) == [1, 4]

    # Граничные значения
    numbers = [-1000, 999, 1000]
    target = 0  # Проверка минимальных/максимальных значений

    solution = Solution()
    assert solution.twoSum(numbers, target) == [1, 3]

    # Большой массив (проверка эффективности)
    numbers = list(range(1, 30001))
    target = 59999  # 29999 + 30000

    solution = Solution()
    assert solution.twoSum(numbers, target) == [29999, 30000]


if __name__ == "__main__":
    test()
