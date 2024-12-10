from src.utils import FilterSortVacancies
from src.vacancy import Vacancy


def test_filter_init():         # type: ignore[no-untyped-def]
    test = FilterSortVacancies(filter_word="python", filter_area="москва", filter_salary=0, top_n=5)
    assert test.filter_word == "python"
    assert test.filter_area == "москва"
    assert test.filter_salary == 0
    assert test.top_n == 5


def test_filter_by_description(vac_list_1, vacancy_1):           # type: ignore[no-untyped-def]
    test = FilterSortVacancies(filter_word="Создание", filter_area="Могилев", filter_salary=0, top_n=5)
    assert test.filter_by_description(vac_list_1) == [Vacancy(vacancy_1)]


def test_filter_by_area(vac_list_1, vacancy_2):                # type: ignore[no-untyped-def]
    test = FilterSortVacancies(filter_word="Создание", filter_area="Москва", filter_salary=0, top_n=5)
    assert test.filter_by_area(vac_list_1) == [Vacancy(vacancy_2)]


#
#
def test_filter_by_salary(vac_list_1, vacancy_2):              # type: ignore[no-untyped-def]
    test = FilterSortVacancies(filter_word="Создание", filter_area="Москва", filter_salary=10, top_n=5)
    assert test.filter_by_area(vac_list_1) == [Vacancy(vacancy_2)]


def test_sort_vacancies_by_salary(vac_list_1, vacancy_1, vacancy_2):            # type: ignore[no-untyped-def]
    test = FilterSortVacancies(filter_word="Создание", filter_area="Москва", filter_salary=10, top_n=5)
    assert test.sort_vacancies_by_salary(vac_list_1) == [Vacancy(vacancy_2), Vacancy(vacancy_1)]

# def test_get_top_vacancies(vac_list_1):            # type: ignore[no-untyped-def]
#     test = FilterSortVacancies(filter_word="Создание", filter_area="Москва", filter_salary=10, top_n=5)
#     print(test.get_top_vacancies(vac_list_1))
#     assert (test.get_top_vacancies(vac_list_1)) == ("Вакансия номер 1:\nВакансия: Junior Python\n Ссылка: https://hh.ru/vacancy/105338726\n Зарплата от: 0\n Описание: Создание скриптов\n Город: Могилев",
#                                                      "Вакансия номер 2:\n Вакансия: Junior Python\nСсылка: https: // hh.ru / vacancy / 105338726\nЗарплата от: 10000\nОписание: Приглашаем Инженера\nГород: Москва")


    #         (
    #     "Вакансия номер 1:\nВакансия: Junior Python\nСсылка: https://hh.ru/vacancy/105338726\nЗарплата от: "
    #     "0\nОписание: Создание скриптов\nГород: Могилев\n\nВакансия номер 2:\nВакансия: Junior Python\nСсылка: "
    #     "https://hh.ru/vacancy/105338726\nЗарплата от: 10000\nОписание: Приглашаем Инженера\nГород: Москва\n\n"
    # ))
