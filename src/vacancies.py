class Vacansies:
    result_list = []
    slots = ("name", "url", "snippet", "salary")

    def __init__(self, name, salary, url, description):
        """инициализатор класса для работы с вакансиями"""
        self.name = name
        self.salary = 0
        self.validate_salary(salary)
        self.url = url
        self.description = description
        vacansies_dict = {
            'name': name,
            'salary': salary,
            'url': url,
            'description': description}
        Vacansies.result_list.append(vacansies_dict)

    def validate_salary(self, salary):
        """"Способ валидации зарплаты"""
        if salary == 'null':
            self.salary = '0'
        else:
            self.salary = salary

    def __ge__(self, other):
        """сравнение зарплаты"""
        return self.salary >= other.salary

    @classmethod
    def cast_to_object_list(cls, hh_vacancies: list):
        """добавление из списка вакансий"""
        for i in hh_vacancies:
            if type(i.get('salary', ' ')) is dict:
                new_str = ''
                new_str += str(i['salary']['from'])
                new_str += ' - '
                new_str += str(i['salary']['to'])
                i['salary'] = new_str
            list_class = cls(
                name=i['name'],
                salary=i.get('salary', '0'),
                url=i['area']['url'],
                description=i['snippet']['requirement']
            )
            dict_class = {'name': list_class.name,
                          'salary': list_class.salary,
                          'url': list_class.url,
                          'description': list_class.description
                          }
            cls.result_list.append(dict_class)
        return cls.result_list


if __name__ == "__main__":
    vacancy = Vacansies("Python Developer",
                        "100 000-150 000 руб.",
                        "<https://hh.ru/vacancy/123456>",
                        "Требования: опыт работы от 3 лет...")
    print(vacancy.name)
