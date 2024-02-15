import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Функция для угадывания числа методом бинарного поиска.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1
    predict = 50  # Начинаем угадывать с середины диапазона возможных чисел
    step = 25  # Шаг, на который будем уменьшать диапазон поиска

    while number != predict:
        count += 1
        if number > predict:
            predict += step
        else:
            predict -= step
        step = max(step // 2, 1)  # Уменьшаем шаг вдвое на каждой итерации

    return count

def score_game(game_core):
    """Функция для запуска игры и вычисления среднего количества попыток"""
    np.random.seed(1)  # Фиксируем RANDOM SEED
    random_array = np.random.randint(1, 101, size=(1000))
    count_ls = [game_core(number) for number in random_array]
    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за {score} попыток")

# Запускаем бенчмарк для game_core_v3
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)


