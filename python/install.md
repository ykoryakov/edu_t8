# Установка Python

Инструкция по установке интерпретатора Python и библиотек.

## Windows

Для Windows проще всего будет скачать и установить готовый пакет, состоящий из интерпретатора Python и библиотек.
https://www.anaconda.com/download/#windows (выбираем версию Python 3.x)

## Unix

Под Unix есть два основных варианта:

1. Настроить виртуальное окружение и установить туда необходимые библиотеки.
2. Скачать и установить пакет Anaconda.

### Вариант 1

$ sudo apt-get install python-virtualenv
$ mkdir ~/env && cd ~/env
$ virtualenv --python=python3 edu
$ source edu/bin/activate
$ pip install numpy
$ pip install scipy
$ pip install jupyter

### Вариант 2

Скачать и установить пакет Anaconda - https://www.anaconda.com/download/#linux (выбираем версию Python 3.x)
