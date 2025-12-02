# test_film.py
import pytest
from film import Film

def test_note_validation():
    with pytest.raises(ValueError):
        Film("X", "Y", 2010, 11.0)
    with pytest.raises(ValueError):
        Film("X", "Y", 2010, -0.1)

def test_serialization_and_classique():
    f = Film("Ancien", "R", 1980, 7.5)
    s = f.to_json()
    f2 = Film.from_json(s)
    assert f == f2
    assert f.est_classique() is True

def test_order_by_note():
    low = Film("Low", "R", 2010, 3.0)
    high = Film("High", "R", 2015, 9.0)
    assert low < high
    assert sorted([high, low]) == [low, high]
