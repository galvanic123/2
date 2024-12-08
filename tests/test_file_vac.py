import os

from config import DATA_DIR
from src.file_vac import JSONSaver


def test_init() -> None:
    assert JSONSaver().filename == os.path.join(DATA_DIR, "vacancies.json")
