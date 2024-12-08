import re
from typing import List


class FilterSortVacancies:
    """Класс для фильтрации, сортировки и вывода топ вакансий."""
    def __init__(self, filter_word, filter_area, filter_salary, top_n):           # type: ignore[no-untyped-def]
        self.filter_word = filter_word
        self.filter_area = filter_area
        self.filter_salary = filter_salary
        self.top_n = top_n

    def filter_by_description(self, vacancies_list: List) -> List:
        """Функция для фильтрации вакансий по заданному слову"""
        filtered_vacancies_list = []
        for vac in vacancies_list:
            if re.findall(self.filter_word, vac.description, re.IGNORECASE):
                filtered_vacancies_list.append(vac)
        return filtered_vacancies_list

    def filter_by_area(self, vacancies_list: List) -> List:
        """Функция для фильтрации вакансий по заданному городу"""
        filtered_vacancies_list = []
        for vac in vacancies_list:
            if re.findall(self.filter_area, vac.area, re.IGNORECASE):
                filtered_vacancies_list.append(vac)
        return filtered_vacancies_list

    def filter_by_salary(self, vacancies_list: List) -> List:
        """Функция для фильтрации вакансий по заданной зарплате"""
        filtered_vacancies_list = []
        for vac in vacancies_list:
            if vac.salary >= self.filter_salary:
                filtered_vacancies_list.append(vac)
        return filtered_vacancies_list

    @staticmethod
    def sort_vacancies_by_salary(vacancies_list: List) -> List:
        """Функция для сортировки вакансий по зарплате(по убыванию)."""
        vacancies_list.sort(key=lambda x: x.salary, reverse=True)
        return vacancies_list

    def get_top_vacancies(self, vacancies_list: List) -> List:
        """Функция для получения топ Н вакансий, Н указывает пользователь."""
        top_vacancies = ""
        if self.top_n < len(vacancies_list):
            for i in range(self.top_n):
                top_vacancies += f"Вакансия номер {i + 1}:\n{str(vacancies_list[i])}\n\n"
        else:
            for i in range(len(vacancies_list)):
                top_vacancies += f"Вакансия номер {i + 1}:\n{str(vacancies_list[i])}\n\n"


    # def write_to_file_top_n_vac(self, for_write_top_n_vac_list: List) -> List:
    #     """Записываем список топ N вакансий"""
    #     root_path_src_dir = os.path.split(os.path.abspath(__file__))
    #     root_path_main_dir = os.path.split(os.path.split(root_path_src_dir[0])[0])[0]
    #     file_with_data = str(os.path.join(root_path_main_dir, 'data', self._file_name)) + '.json'
    #     list_top_n_vac_for_write = []
    #     for vac in for_write_top_n_vac_list:
    #         list_top_n_vac_for_write.append({'name': vac.name, 'link': vac.url, 'city': vac.area,
    #                                          'salary_from': vac.salary_min, 'salary_to': vac.salary_max,
    #                                          'currency': vac.currency, 'requirements': vac.requirements,
    #                                          'duties': vac.responsibility})
    #
    #     try:
    #         with open(file_with_data, "w", encoding="UTF-8",) as file_vac_for_update:
    #             json.dump(list_top_n_vac_for_write, file_vac_for_update, indent=2, ensure_ascii=False)
    #     except FileNotFoundError:
    #         with open(file_with_data, "w",encoding='UTF-8') as file_vac_new:
    #             json.dump(list_top_n_vac_for_write, file_vac_new, indent=2, ensure_ascii=False)
    #     except json.JSONDecodeError:
    #         with open(file_with_data, "w", encoding='UTF-8') as file_vac_for_update:
    #             json.dump(list_top_n_vac_for_write, file_vac_for_update, indent=2, ensure_ascii=False)
    #     return list_top_n_vac_for_write
