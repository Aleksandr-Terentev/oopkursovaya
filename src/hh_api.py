import requests
from src.base_api import Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser
    является родительским классом,
    который вам необходимо реализовать
    """

    def __init__(self, file_worker='Data/JsonFile.json'):
        """инициализатор"""
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        """функция для загрузки вакансий"""
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = (requests.get
                        (self.__url, headers=self.__headers,
                         params=self.__params))
            vacancies = response.json()['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1
        return self.__vacancies

    @property
    def vacancies(self):
        """декоратор для работы с приватным атрибутом"""
        return self.__vacancies


if __name__ == "__main__":
    hh = HH(' ')
    hh.load_vacancies('python')
    print(hh.vacancies)
