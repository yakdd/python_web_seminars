import pytest
from user import User


@pytest.fixture
def user():
    return User('Admin', 0, 1)


def test_equal(user):
    assert User('Admin', 0) == user


def test_not_equal(user):
    assert User('Other', 1) != user


def test_bad_name(user):
    with pytest.raises(ValueError):
        User('number16', 10)


def test_bad_id(user):
    with pytest.raises(ValueError, match='идентификатор должен быть целым числом'):
        User('number', 3.14)


def test_bad_level(user):
    with pytest.raises(ValueError, match=f'Уровень доступа должен быть целым числом от {user.min_lvl} до {user.max_lvl}'):
        User('number', 7, 0)


if __name__ == '__main__':
    pytest.main(['-v'])
