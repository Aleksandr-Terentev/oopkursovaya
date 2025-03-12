import pytest
from src.vacancies import Vacansies


@pytest.fixture
def test_vacansies():
    return Vacansies("Python Developer",
                     "100 000-150 000 руб.",
                     "<https://hh.ru/vacancy/123456>",
                     "Требования: опыт работы от 3 лет...")


@pytest.fixture
def test_validate():
    return Vacansies("Python Developer",
                     "null",
                     "<https://hh.ru/vacancy/123456>",
                     "Требования: опыт работы от 3 лет...")


@pytest.fixture
def test_json():
    return ('[\n    {\n        "name": "Python Developer",'
            '\n        "salary": "100 000-150 000 руб.",'
            '\n        "url": "<https://hh.ru/vacancy/123456>",'
            '\n        "description": "Требования: опыт работы от 3 лет..."'
            '\n    }\n]')
