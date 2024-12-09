from abc import ABC, abstractmethod
from typing import List

import requests


class Parser(ABC):
    """Абстрактный класс для работы с API сервисов с вакансиями"""

    @abstractmethod
    def load_vacancies(self, keyword):            # type: ignore[no-untyped-def]
        pass

    @abstractmethod
    def get_vacancies(self) -> None:
        pass


class HeadHunterAPI(Parser, ABC):
    """Класс для получения вакансий"""
    def __init__(self):             # type: ignore[no-untyped-def]
        """Инициируем конструктор класса"""
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 20}
        self.vacancies = []
        super().__init__()

    def load_vacancies(self, keyword: str):             # type: ignore[no-untyped-def]
        """Функция для получения вакансий по заданному слову"""
        self.params['text'] = keyword
        while self.params.get('page') != 2:
            try:
                response = requests.get(self.__url, headers=self.__headers, params=self.params)
            except Exception as e:
                print(f"Произошла ошибка {e}")
            else:
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)
                self.params['page'] += 1

    def get_vacancies(self) -> List:
        """Возвращает список вакансий"""
        return self.vacancies
