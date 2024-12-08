import pytest

from src.hh_api import HeadHunterAPI


@pytest.fixture
def api_instance():          # type: ignore[no-untyped-def]
    return HeadHunterAPI()


def test_get_vacancies(api_instance):            # type: ignore[no-untyped-def]
    keyword = 'python'
    vacancies = api_instance.load_vacancies(keyword)
    hh_vacancies = api_instance.get_vacancies()
    # print(hh_vacancies, list)
    assert isinstance(hh_vacancies, list)
