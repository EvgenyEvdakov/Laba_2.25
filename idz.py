#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Для своего индивидуального задания лабораторной работы 2.23 необходимо реализовать вычисление значений в двух
# функций в отдельных процессах.
# Условие 2.23 - С использованием многопоточности для заданного значения x найти сумму ряда S с точностью члена ряда
# по абсолютному значению ε=10-7 и произвести сравнение полученной суммы с контрольным значением функции для
# двух бесконечных рядов.

import multiprocessing
import math


# Функция для вычисления суммы ряда
def compute_series_sum(x, epsilon, result, series_type):
    n = 0  # Начальное значение степени
    term = (x ** (2 * n)) / math.factorial(2 * n)  # Вычисление первого члена ряда
    series_sum = 0  # Инициализация переменной для хранения суммы ряда

    # Выбор типа ряда для вычислений
    if series_type == 1:
        # Цикл для вычисления суммы ряда до достижения точности epsilon
        while abs(term) > epsilon:
            series_sum += term
            n += 1
            term = (x ** (2 * n)) / math.factorial(2 * n)

    elif series_type == 2:
        # Цикл для вычисления суммы ряда с чередующимися знаками до достижения точности epsilon
        while abs(term) > epsilon:
            series_sum += term
            n += 1
            term = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)

    result.value = series_sum  # Запись результата в общую память


def main():
    x = 1 / 2  # Заданное значение x
    epsilon = 1e-7  # Точность вычислений

    # Контрольные значения для сравнения
    control_value_1 = (math.exp(x) + math.exp(-x)) / 2
    control_value_2 = math.cos(x)

    # Общая память для хранения результатов
    result_1 = multiprocessing.Value('d', 0.0)
    result_2 = multiprocessing.Value('d', 0.0)

    # Создание процессов для вычисления суммы ряда
    process_1 = multiprocessing.Process(target=compute_series_sum, args=(x, epsilon, result_1, 1))
    process_2 = multiprocessing.Process(target=compute_series_sum, args=(x, epsilon, result_2, 2))

    # Запуск процессов
    process_1.start()
    process_2.start()

    # Ожидание завершения процессов
    process_1.join()
    process_2.join()

    # Получение результатов
    series_sum_1 = result_1.value
    series_sum_2 = result_2.value

    # Сравнение результатов с контрольными значениями
    print(f"Сумма ряда 1: {series_sum_1}, Контрольное значение: {control_value_1}")
    if abs(series_sum_1 - control_value_1) < epsilon:
        print("Результат ряда 1 совпадает с контрольным значением.")
    else:
        print("Результат ряда 1 не совпадает с контрольным значением.")

    print(f"Сумма ряда 2: {series_sum_2}, Контрольное значение: {control_value_2}")
    if abs(series_sum_2 - control_value_2) < epsilon:
        print("Результат ряда 2 совпадает с контрольным значением.")
    else:
        print("Результат ряда 2 не совпадает с контрольным значением.")


if __name__ == "__main__":
    main()
