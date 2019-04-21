import pytest

from card_validator.validator import card_validator


def test_get_issue():
    assert card_validator("4341 4566 7543 3445") == "Visa"

    with pytest.raises(ValueError):
        card_validator("2345 5656 6644") == "Visa"


def test_get_master_card_issue():
    assert card_validator("5241 4566 7543 3445") == "Master"

    with pytest.raises(ValueError):
        card_validator("2345 5656 6644") == "Master card"

def test_get_american_express():
    assert card_validator("3741 4566 7543 344") == "American Express"

    with pytest.raises(ValueError):
        card_validator("2345 5656 6644") == "American Express"


def test_length_of_visa_card():
    with pytest.raises(ValueError):
        card_validator("4333 1234 5555 66661") == "Visa"
    with pytest.raises(ValueError):
        card_validator("4333 1234 5555 666") == "Visa"
    with pytest.raises(ValueError):
        card_validator("5333 1234 5555 6666 1") == "Master"
    with pytest.raises(ValueError):
        card_validator("5333 1234 5555 666") == "Master"
    with pytest.raises(ValueError):
        card_validator("3733 1234 5555 6665") == "American Express"
    with pytest.raises(ValueError):
        card_validator("3733 1234 5555 66") == "American Express"
