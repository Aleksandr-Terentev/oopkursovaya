def filter_vacancies(api_list: list, api_words: list):
    """фильтр факансий по имени и описанию"""
    new_list = []
    for k in api_words:
        for i in api_list:
            if k in i.get('name', ' ') or i.get('description', ' '):
                if i not in new_list:
                    new_list.append(i)
                else:
                    continue
    return new_list


def get_vacancies_by_salary(filter_list: list, salary_range: str):
    """фильтр вакансий по зарплате"""
    salary_range_split = salary_range.split()
    total_list = []
    for i in filter_list:
        if i['salary'] is not None:
            salary = i['salary'].split()
            if (salary[0] >= salary_range_split[0]
                    and salary[2] <= salary_range_split[2]):
                total_list.append(i)
        else:
            continue
    return total_list


def sort_vacancies(ranged_vacancies: list[dict]):
    """сортировка вакансий по зарплате по убыванию"""
    return sorted(ranged_vacancies,
                  key=lambda to: to["salary"].split()[2], reverse=True)


def get_top_vacancies(sorted_vacancies: list[dict], top: int):
    """получение количества вакансий для вывода в консоль"""
    return sorted_vacancies[0:top]
