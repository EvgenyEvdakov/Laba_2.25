#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Процессы-демоны. Процессы демоны по своим свойствам похожи на потоки-демоны, их суть заключается в том, что
# они завершают свою работу, если завершился родительский процесс. Указать на то, что процесс является демоном
# можно при создании экземпляра класса через аргумент daemon, либо после создания через свойство daemon.

from multiprocessing import Process
from time import sleep

def func(name):
    counter = 0
    while True:
        print(f"proc {name}, counter = {counter}")
        counter += 1
        sleep(0.1)

if __name__ == "__main__":
    proc1: Process = Process(target=func, args=("proc1",), daemon=True)

    # Указание на то, что процесс демон через свойство daemon
    proc2 = Process(target=func, args=("proc2",))
    proc2.daemon = True

    # Запуск процессов
    proc1.start()
    proc2.start()
    sleep(0.3)