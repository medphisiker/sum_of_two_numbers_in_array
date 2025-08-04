from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Находит два элемента в отсортированном массиве, сумма которых равна целевому значению.
        Возвращает их индексы увеличенные на единицу, так как будто нумерация массива начинается с 1-цы.

        Использует паттерн two pointers.
        
        Временная сложность:O(n).
        Пространственная сложность: O(1).

        Args:
            numbers: Отсортированный массив целых чисел.
            target: Целевая сумма.

        Returns:
            Кортеж из двух чисел, соответствующих индексам элементов, увеличенных на единицу,
            так как будто нумерация массива начинается с 1-го.

        Examples:
            >>> twoSum([2, 7, 11, 15], 9)
            [1, 2]
            >>> twoSum([2, 3, 4], 6)
            [1, 3]
            >>> twoSum([-1, 0], -1)
            [1, 2]
        """
        # Инициализация двух указателей
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]

            elif current_sum < target:
                # Сумма слишком маленькая, нужно увеличить левый элемент
                left += 1
            else:
                # Сумма слишком большая, нужно уменьшить правый элемент
                right -= 1

        return None