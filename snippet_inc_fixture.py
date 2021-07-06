@pytest.fixture(scope='module')
def my_iter():
    gen_id = count(1)
    def foo():
        return next(gen_id)
    return foo


def test_1(my_iter):
    assert my_iter() == 1


def test_2(my_iter):
    assert my_iter() == 2
