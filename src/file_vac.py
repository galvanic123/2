import json
import os
from abc import ABC, abstractmethod

from config import DATA_DIR
from src.vacancy import Vacancy


class Employee(ABC):
    """Абстрактный родительский класс для обработки файла"""
    @abstractmethod
    def read_file(self):               # type: ignore[no-untyped-def]
        pass

    @abstractmethod
    def write_file(self, ser_vacs):             # type: ignore[no-untyped-def]
        pass

    @abstractmethod
    def del_vacancy(self):       # type: ignore[no-untyped-def]
        pass


class JSONSaver(Employee):
    """Класс для работы с файлом со списком вакансий"""
    filename_value = "vacancies.json"

    def __init__(self, filename=filename_value):         # type: ignore[no-untyped-def]
        self.vacs_list = []

        self.__filename = os.path.join(DATA_DIR, filename)

    @property
    def filename(self):           # type: ignore[no-untyped-def]
        return self.__filename

    def read_file(self):               # type: ignore[no-untyped-def]
        """Функция чтения файла. Проверяет, есть ли файл и при наличии сохраняет список объектов."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as f:
                vacs = json.load(f)
            self.vacs_list = [Vacancy(i) for i in vacs]
        return self.vacs_list

    def write_file(self, vacs_obj: list):          # type: ignore[no-untyped-def]
        """Функция для записи списка вакансий в файл. Принимает список объектов класса Vacancy."""
        vacs_list = []
        for i in vacs_obj:
            vacs_list.append(
                {
                    "name": Vacancy(i).name,
                    "alternate_url": Vacancy(i).link,
                    "salary": {"from": Vacancy(i).salary},
                    "snippet": {"responsibility": Vacancy(i).description},
                    "area": {"name": Vacancy(i).area},
                }
            )
        with open(self.filename, 'w', encoding='UTF-8') as f:
            json.dump(vacs_list, f, ensure_ascii=False, indent=4)

    def del_vacancy(self):         # type: ignore[no-untyped-def]
        with open(self.filename, 'w') as f:
            json.dump([], f, ensure_ascii=False, indent=4)
