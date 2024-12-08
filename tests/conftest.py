import pytest

from src.vacancy import Vacancy


@pytest.fixture
def serialized():             # type: ignore[no-untyped-def]
    return [
        {
            "name": "Junior Python",
            "link": "https://hh.ru/vacancy/105338726",
            "salary": 10,
            "description": "Создание скриптов",
            "area": "Могилев",
        }
    ]


@pytest.fixture
def serialized_for_json():            # type: ignore[no-untyped-def]
    return [
        {
            "name": "Junior Python developer",
            "link": "https://hh.ru/vacancy/105338726",
            "salary": 0,
            "description": "Создание скриптов на <highlighttext>Python</highlighttext> для "
                           "автоматизации тестирования блокчейн и инфраструктурных проектов. "
                           "Разработка сценариев, имитирующих взаимодействие пользователя с веб-приложением, "
                           "включая...",
            "area": "Могилев",
        }
    ]


@pytest.fixture
def serialized_for_user():             # type: ignore[no-untyped-def]
    return (
        "Вакансия: Junior Python developer"
        "Ссылка: https://hh.ru/vacancy/105338726)"
        "Зарплата от: 0"
        "Описание: Создание скриптов на <highlighttext>Python</highlighttext> для автоматизации тестирования "
        "блокчейн и инфраструктурных проектов. Разработка сценариев, имитирующих взаимодействие пользователя с "
        "веб-приложением, включая..."
        "Город: Могилев"
    )


@pytest.fixture
def hh_vacs_list():             # type: ignore[no-untyped-def]
    return [
        {
            "name": "Junior Python developer",
            "alternate_url": "https://hh.ru/vacancy/105338726",
            "salary": 0,
            "snippet": {
                "responsibility": "Создание скриптов на <highlighttext>Python</highlighttext> для автоматизации "
                                  "тестирования блокчейн и инфраструктурных проектов. Разработка сценариев, "
                                  "имитирующих взаимодействие пользователя с веб-приложением, включая..."
            },
            "area": {"name": "Могилев"},
        }
    ]


@pytest.fixture
def vacancy_1():           # type: ignore[no-untyped-def]
    return {
        "name": "Junior Python",
        "alternate_url": "https://hh.ru/vacancy/105338726",
        "salary": {"from": 0},
        "snippet": {"responsibility": "Создание скриптов"},
        "area": {
            "name": "Могилев",
        },
    }


@pytest.fixture
def vacancy_2():         # type: ignore[no-untyped-def]
    return {
        "name": "Junior Python",
        "alternate_url": "https://hh.ru/vacancy/105338726",
        "salary": {"from": 10000},
        "snippet": {"responsibility": "Приглашаем Инженера"},
        "area": {
            "name": "Москва",
        },
    }


@pytest.fixture
def vac_list_1(vacancy_1, vacancy_2):         # type: ignore[no-untyped-def]
    return [Vacancy(vacancy_1), Vacancy(vacancy_2)]
