from solution import Solution


def main():
    """
    Основная функция программы.
    Считывает входные данные, находит пару чисел и выводит результат.
    """
    numbers = list(map(int, input().split()))
    target_sum = int(input())

    solution = Solution()
    result = solution.twoSum(numbers, target_sum)
    print(result[0], result[1])


if __name__ == "__main__":
    main()
