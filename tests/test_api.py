import pytest
import unittest.mock
from src.api import HhAPI
import requests


@pytest.fixture
def hh_api():
    return HhAPI()


@unittest.mock.patch('src.api.requests.get')
def test_get_vacancies_success(mock_get, hh_api):
    mock_get.return_value.json.return_value = {
        'items': [
            {'name': 'Программист', 'employer': {'name': 'Компания'},
             'salary': {'from': 60000, 'to': 80000, 'currency': 'RUR'}}
        ]
    }

    vacancies = hh_api.get_vacancies(text='программист')
    assert len(vacancies) == 1
    assert vacancies[0]['name'] == 'Программист'


@unittest.mock.patch('src.api.requests.get')
def test_get_vacancies_failure(mock_get, hh_api):
    mock_get.side_effect = requests.exceptions.HTTPError('Ошибка HTTP')

    with pytest.raises(requests.exceptions.HTTPError):
        hh_api.get_vacancies(text='программист')


@unittest.mock.patch('src.api.requests.get')
def test_make_request_success(mock_get, hh_api):
    mock_get.return_value.json.return_value = {
        'items': [
            {'name': 'Аналитик', 'employer': {'name': 'Аналитика'},
             'salary': {'from': 50000, 'to': 70000, 'currency': 'RUR'}}
        ]
    }

    response = hh_api._make_request('vacancies', {'text': 'аналитик'})
    assert 'items' in response
    assert len(response['items']) == 1
    assert response['items'][0]['name'] == 'Аналитик'


@unittest.mock.patch('src.api.requests.get')
def test_make_request_failure(mock_get, hh_api):
    mock_get.side_effect = requests.exceptions.RequestException('Ошибка запроса')

    with pytest.raises(requests.exceptions.RequestException):
        hh_api._make_request('vacancies', {'text': 'аналитик'})
