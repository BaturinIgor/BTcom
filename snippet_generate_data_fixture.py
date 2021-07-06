import pytest

from itertools import count

@pytest.fixture()
def generator():
    def random_int():
        return random.randint(1, 10)
    return random_int


@pytest.fixture
def data(generator):
    data = []
    for _ in range(10):
        data.append(generator())
    return data


def test_one(data):
    assert len(data) == 10
    check_set = set((i for i in range(1, 11)))
    for item in data:
        assert item in check_set
