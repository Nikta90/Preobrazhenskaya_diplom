# Преображенская Катя, 11 когорта, дипломный проект - инженер по тестированию плюс

import data
import configuration
import requests


# Создание нового заказа
def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREAT_ORDERS, json=order_body)


# Сохранение номера заказа
order_track_number = create_order(data.order_body).json()["track"]


#  Получение заказа по треку
def get_order_by_track(order_track_number1):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(order_track_number1))


# Проверка код ответа=200
def test_get_order_by_track():
    data_order = get_order_by_track(order_track_number)
    assert data_order.status_code == 200
