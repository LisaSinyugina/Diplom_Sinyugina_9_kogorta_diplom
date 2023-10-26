import configuration
import data
import requests


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,)
response = post_new_order(data.order_body)

def get_order_track():
    track = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body).json()['track']

    return track

def get_order():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(get_order_track())).status_code


def test_assert_status():
    actual = get_order()
    expected = 200
    assert actual == expected

# Синюгина Елизавета, 9-я когорта, финальный проект. Инженер по тестированию плюс

