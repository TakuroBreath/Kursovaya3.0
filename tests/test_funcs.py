from src.funcs import *


def test_get_data_from_json():
    assert get_data_from_json('src/operations.json') != []
    assert get_data_from_json('src/operations.json') != False
    assert get_data_from_json('src/operations.json') != ""


def test_sort_by_recency():
    assert sort_by_recency([]) == []
    assert sort_by_recency([{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                             'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                             'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                             'to': 'Счет 64686473678894779589'}]) == [
               {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                'to': 'Счет 64686473678894779589'}]
    assert sort_by_recency(get_data_from_json('src/operations.json')) != ""


def test_five_recent_operations():
    assert five_recent_operations(
        [{'state': 'EXECUTED'}, {'state': '(.)(.)'}, {'state': 'EXECUTED'}, {'state': 'EXECUTED'},
         {'state': 'EXECUTED'}, {'state': 'EXECUTED'}]) == [{'state': 'EXECUTED'}, {'state': 'EXECUTED'},
                                                            {'state': 'EXECUTED'}, {'state': 'EXECUTED'},
                                                            {'state': 'EXECUTED'}]
    assert five_recent_operations(sort_by_recency(get_data_from_json('src/operations.json'))) != ""

def test_mask_card():
    assert mask_card('Пипипупу 1234567890123456') == 'Пипипупу 1234 56** **** 3456'
    assert mask_card('Раз Два 1234567890123456') == 'Раз Два 1234 56** **** 3456'

def test_mask_target_card():
    assert mask_target_card('Пипипупу 1234567890123456') == 'Пипипупу **3456'
    assert mask_target_card('Раз Два 1234567890123456') == 'Раз Два **3'

def test_printing():
    assert printing([{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                'to': 'Счет 64686473678894779589'}]) == None

