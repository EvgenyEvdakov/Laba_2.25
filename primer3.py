#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Принудительное завершение работы процессов. В отличии от потоков, работу процессов можно принудительно завершить,
# для этого класс Process предоставляет набор методов

from multiprocessing import Process
from time import sleep


def func():
    counter = 0
    while True:
        print(f"counter = {counter}")
        counter += 1
        sleep(0.1)


if __name__ == "__main__":
    proc = Process(target=func)
    proc.start()
    sleep(0.7)
    proc.terminate()