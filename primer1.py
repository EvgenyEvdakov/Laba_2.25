#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# создание и ожидание завершения работы процессов. Для запуска процесса используется метод start().

from multiprocessing import Process

def func():
  print("Hello from child Process")
if __name__ == "__main__":
  print("Hello from main Process")
  proc = Process(target=func)
  proc.start()