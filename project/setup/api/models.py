from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режисёр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Леонид Гайдай'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='КАК НАЧАТЬ МЕТКО СТРЕЛЯТЬ БЕЗ ЧИТОВ. МОЙ СПОСОБ '
                                                                  'ТРЕНИРОВКИ АИМА'),
    'description': fields.String(required=True, max_length=255, example='Всем привет, меня зовут Игорь. Мне 30 лет. '
                                                                        'Очень приятно видеть тебя на моем канале. '
                                                                        'Хорошего  тебе настроения! Неси к монитору '
                                                                        'чай и бутеры - будет интересно! '),
    'trailer': fields.String(required=True, max_length=255, example='https://www.youtube.com/watch?v=ofsX1MVEJ3k'),
    'year': fields.Integer(required=True, max_length=20, example='2005'),
    'rating': fields.Float(required=True, max_length=10, example='5.0'),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=150, example='mail@mail.com'),
    'password': fields.String(required=True, max_length=100, example='password'),
    'name': fields.String(required=True, max_length=100, example='Иван'),
    'surname': fields.String(required=True, max_length=100, example='Иванов'),
    'favorite_genre': fields.Integer(required=True, example=1),
})
