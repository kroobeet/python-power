import sys
import warnings


def sum_numbers(n: int) -> int:
    """
    Возвращает сумму всех целых чисел от 1 до n включительно

    Args:
        n (int): Верхняя граница диапазона (должно быть положительным целым числом).

    Returns:
        int: Сумма чисел от 1 до n.

    Raises:
        TypeError: Если n НЕ является целым числом
        ValueError: Если n является отрицательным числом

    Examples:
        >>> sum_numbers(5)
        15
        >>> sum_numbers(0)
        0
        >>> sum_numbers(1)
        1
    """

    if not isinstance(n, int):
        raise TypeError(f"Ожидается int, получен {type(n)}")
    elif n < 0:
        raise ValueError("n должно быть положительным")
    elif n > sys.maxsize // 2:
        warnings.warn("Возможно переполнение для других языков", RuntimeWarning)

    return n * (n + 1) // 2
