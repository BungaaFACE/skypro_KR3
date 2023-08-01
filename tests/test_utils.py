import src.utils as utils
import json
import pytest

OPERATIONS_FILE = Path(__file__).parent.joinpath("operations.json")


@pytest.fixture
def get_list_from_json():
    with open(json_path, encoding='utf8') as json_data:
        return json.load(json_data)


@pytest.fixture
def get_unsorted_list():
    return [
        {'date': "2018-08-19T04:27:37.904916"},
        {'date': "2019-12-08T22:46:21.935582"},
        {'not_date': "random_data"},
        {'date': "2018-01-26T15:40:13.413061"}
    ]


operation1 = {
    "id": 518707726,
    "state": "EXECUTED",
    "date": "2018-11-29T07:18:23.941293",
    "operationAmount": {
            "amount": "3348.98",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
    },
    "description": "Перевод с карты на карту",
    "from": "MasterCard 3152479541115065",
    "to": "Visa Gold 9447344650495960"
}
operation2 = {
    "id": 649467725,
    "state": "EXECUTED",
    "date": "2018-04-14T19:35:28.978265",
    "operationAmount": {
            "amount": "96995.73",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
    },
    "description": "Перевод организации",
    "from": "Счет 27248529432547658655",
    "to": "Счет 97584898735659638967"
}
operation3 = {
    "id": 172864002,
    "state": "EXECUTED",
    "date": "2018-12-28T23:10:35.459698",
    "operationAmount": {
            "amount": "49192.52",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
    },
    "description": "Открытие вклада",
    "to": "Счет 96231448929365202391"
}

state_check_operations = [{
    "id": 172864002,
    "state": "EXECUTED",
    "date": "2018-12-28T23:10:35.459698",
    "operationAmount": {
        "amount": "49192.52",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Открытие вклада",
    "to": "Счет 96231448929365202391"
},
    {
    "id": 476991061,
    "state": "CANCELED",
    "date": "2018-11-23T17:47:33.127140",
    "operationAmount": {
        "amount": "26971.25",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Gold 7305799447374042",
    "to": "Maestro 3364923093037194"
},
    {
    "id": 633268359,
    "state": "EXECUTED",
    "date": "2019-07-12T08:11:47.735774",
    "operationAmount": {
        "amount": "2631.44",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Visa Gold 3589276410671603",
    "to": "Счет 96292138399386853355"
}]


def test_get_json_data(get_list_from_json):
    assert utils.get_json_data(json_path) == get_list_from_json


def test_sort_operations_by_date(get_unsorted_list):
    assert utils.sort_operations_by_date(get_unsorted_list) == [{'date': "2019-12-08T22:46:21.935582"},
                                                                {'date': "2018-08-19T04:27:37.904916"},
                                                                {'date': "2018-01-26T15:40:13.413061"},
                                                                {'not_date': "random_data"}]


def test_parse_operation_data():
    assert utils.parse_operation_data(operation1) == '''29.11.2018 Перевод с карты на карту
MasterCard 3152 47** **** 5065 -> Visa Gold **5960
3348.98 USD
'''

    assert utils.parse_operation_data(operation2) == '''14.04.2018 Перевод организации
Счет 2724 85** **** 8655 -> Счет **8967
96995.73 руб.
'''

    assert utils.parse_operation_data(operation3) == '''28.12.2018 Открытие вклада
Пополнение вклада -> Счет **2391
49192.52 USD
'''


def test_filter_operations_by_executed():
    assert utils.filter_operations_by_executed(state_check_operations) == [{
        "id": 172864002,
        "state": "EXECUTED",
        "date": "2018-12-28T23:10:35.459698",
        "operationAmount": {
            "amount": "49192.52",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 96231448929365202391"
    },
        {
        "id": 633268359,
        "state": "EXECUTED",
        "date": "2019-07-12T08:11:47.735774",
        "operationAmount": {
            "amount": "2631.44",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Gold 3589276410671603",
        "to": "Счет 96292138399386853355"
    }]

    assert utils.filter_operations_by_executed(state_check_operations, 1) == [{
        "id": 172864002,
        "state": "EXECUTED",
        "date": "2018-12-28T23:10:35.459698",
        "operationAmount": {
            "amount": "49192.52",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 96231448929365202391"
    }]
