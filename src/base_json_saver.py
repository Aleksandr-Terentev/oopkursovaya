from abc import ABC, abstractmethod


class BaseJson(ABC):
    @abstractmethod
    def add_vacancies(self, vacancie):
        pass

    @abstractmethod
    def load_vacancies(self, vacancie):
        pass

    @abstractmethod
    def remove_vacancies(self, vacancie):
        pass
