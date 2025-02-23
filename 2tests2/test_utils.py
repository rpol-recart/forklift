from app.utils import validate_data


def test_validate_data():
    valid_data = {"name": "Test", "type": "Forklift"}
    assert validate_data(valid_data) is True

    invalid_data = {"invalid_key": "value"}
    assert validate_data(invalid_data) is False

