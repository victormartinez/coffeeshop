from pathlib import Path

import pytest


TESTS_FOLDER = Path(__file__).cwd() / "tests"

@pytest.fixture
def fixtures_path():
    return TESTS_FOLDER / "fixtures/"


@pytest.fixture
def row_reader(fixtures_path):
    def callable(filename: str) -> str:
        filepath = fixtures_path / f"data/{filename}"
        with open(filepath) as f_pointer:
            for row in f_pointer:
                yield row

    return callable


@pytest.fixture
def content_reader(fixtures_path):
    def callable(filename: str) -> str:
        filepath = fixtures_path / f"data/{filename}"
        return Path(filepath).read_text()

    return callable
