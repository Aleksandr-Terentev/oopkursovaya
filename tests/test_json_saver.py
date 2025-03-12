from src.Json_saver import JsonSaver


def test_json_saver(test_vacancies, test_json):
    json_saver = JsonSaver('../data/[].json')
    json_saver.add_vacancies(test_vacancies.result_list)
    with open('../data/[].json', encoding='utf-8') as file:
        assert test_json == file.read()


def test_json_remove(test_vacancies):
    json_saver = JsonSaver('../data/[].json')
    # json_saver.add_vacancies(test_vacancies.result_list)
    json_saver.remove_vacancies(test_vacancies)
    with open('../data/[].json', encoding='utf-8') as file:
        assert '[]' == file.read()
