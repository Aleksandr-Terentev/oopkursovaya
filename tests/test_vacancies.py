def test_vacancies_(test_vacancies):
    assert test_vacancies.name == "Python Developer"
    assert test_vacancies.salary == "100 000-150 000 руб."
    assert test_vacancies.url == "<https://hh.ru/vacancy/123456>"
    assert test_vacancies.description == "Требования: опыт работы от 3 лет..."


def test_validate_salary(test_validate):
    assert test_validate.salary == '0'


def test_ge(test_vacancies, test_validate):
    assert test_vacancies.__ge__(test_validate) is True


def test_cast_to_object():
    pass
