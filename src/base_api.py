from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def __init__(self, file_worker):
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self, keyword):
        """абстрактный класс для работы с API сервиса с вакансиями"""
        pass
