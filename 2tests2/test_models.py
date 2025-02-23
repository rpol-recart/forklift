from app.models import Forklift


def test_forklift_initialization():
    fl = Forklift(id=1, name="Test Forklift")
    assert fl.id == 1
    assert fl.name == "Test Forklift"
    assert str(fl) == "<Forklift 1>"


def test_forklift_calculate_method():
    fl = Forklift(...)
    # Проверьте методы класса Forklift, например:
    result = fl.calculate_something()
    assert result == expected_value
