
# Основы Python часть 9

Разработка web сервисов с помощью Django

## Подготовка окружения

(здесь и далее инструкции для Unix)

```bash
cd ~  
mkdir env  
virtualenv --python=python3 ~/env/rooms
source ~/env/rooms/bin/activate
```

## Установка Django

```bash
pip install django
```

## Клонирование проекта

```bash
cd ~
mkdir pro
cd pro
git clone ...
```

## Подготовка БД

```bash
cd ...
./manage.py check
./manage.py makemigrations room
./manage.py migrate
```

## Создание пользователя

```bash
./manage.py createsuperuser
```

## Запуск отладочного сервера

```bash
./manage.py runserver 127.0.0.1:8000
```

## Работа с сервисом

Домашняя страница - http://127.0.0.1:8000/

Административный доступ - http://127.0.0.1:8000/admin
