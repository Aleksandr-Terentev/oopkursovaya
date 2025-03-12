from src.base_json_saver import BaseJson
import json
from src.vacancies import Vacansies


class JsonSaver(BaseJson):
    def __init__(self, path_to_file='../data/JsonFile.json'):
        self.path_to_file = path_to_file
        # with open(path_to_file, 'a', encoding='utf-8') as file:
        #     self.data = json.load(file)

    def add_vacancies(self, vacancie):
        """добавление вакансий в файл"""
        with open(self.path_to_file, 'r+', encoding='utf-8') as file:
            json.dump(vacancie, file, ensure_ascii=False, indent=4)

    def load_vacancies(self, vacancie: str):
        """загрузка вакансий"""
        with open(self.path_to_file, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for i in data:
                if i['name'] == vacancie:
                    print(i)

    def remove_vacancies(self, vacancie):
        """удаление вакансии из файла"""
        new_dict = {
            'name': vacancie.name,
            'url': vacancie.url,
            'salary': vacancie.salary,
            'description': vacancie.description
        }

        with open(self.path_to_file, 'r+', encoding='utf-8') as file:
            data = json.load(file)

        for i in data:
            if i == new_dict:
                data.remove(i)
        with open(self.path_to_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    # Пример работы конструктора класса с одной вакансией
    vacancy = Vacansies(
        "Python Developer",
        "<https://hh.ru/vacancy/123456>",
        "100 000-150 000 руб.",
        "Требования: опыт работы от 3 лет...")

    # Сохранение информации о вакансиях в файл
    json_saver = JsonSaver()
    json_saver.add_vacancies(vacancy.result_list)
    json_saver.remove_vacancies(vacancy)
