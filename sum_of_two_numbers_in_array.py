def find_two_numbers_for_given_sum(
    numbers: list[int], target_sum: int
) -> tuple[int, int] | None:
    """
    Находит два числа в отсортированном массиве, сумма которых равна целевому значению.

    Использует алгоритм двух указателей для достижения O(n) по времени и O(1) по памяти.

    Args:
        numbers: Отсортированный массив целых чисел
        target_sum: Целевая сумма

    Returns:
        Кортеж из двух чисел, дающих в сумме target_sum, или None если такая пара не найдена

    Examples:
        >>> find_two_numbers_for_given_sum([2, 4, 8, 9, 11, 12, 16, 21], 19)
        (8, 11)
        >>> find_two_numbers_for_given_sum([1, 2, 3, 4], 5)
        (1, 4)
        >>> find_two_numbers_for_given_sum([1, 2], 4)
        None
    """
    # Проверка крайних случаев
    if len(numbers) < 2:
        return None

    # Инициализация двух указателей
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target_sum:
            return numbers[left], numbers[right]

        elif current_sum < target_sum:
            # Сумма слишком маленькая, нужно увеличить левый элемент
            left += 1
        else:
            # Сумма слишком большая, нужно уменьшить правый элемент
            right -= 1

    return None


def main():
    """
    Основная функция программы.
    Считывает входные данные, находит пару чисел и выводит результат.
    """
    numbers = list(map(int, input().split()))
    target_sum = int(input())
    result = find_two_numbers_for_given_sum(numbers, target_sum)
    if result is not None:
        print(result[0], result[1])
    else:
        print("None")


if __name__ == "__main__":
    main()
