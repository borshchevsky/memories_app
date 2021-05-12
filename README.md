# Places Remember

Сервис позволяет сохранять и просматривать координаты мест с описанием впечатлений
об этих местах. Регистрация на сервисе происходит автоматически через VK или Facebook.


## Используемые технологии:



- Python 3.8.2
- JavaScript (Yandex API)
- Django
- Postgres
- Nginx
- Docker
- Docker-compose
- Bootstrap 5


## Установка

1. Клонировать проект.
2. Создать и запустить контейнер.

```sh
sudo docker-compose up -d
```

3. Запустить миграции и создать суперпользователя.
```sh
sudo docker-compose exec web python manage.py makemigrations
```
```sh
sudo docker-compose exec web python manage.py migrate
```
```sh
sudo docker-compose exec web python manage.py createsuperuser
```

4. Через админку создать соответствующие Social applications (VK, Facebook).
