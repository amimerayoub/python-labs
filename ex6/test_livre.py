# test_livre.py
import json
import pytest
from livre import Livre

def test_to_from_json_and_promo():
    l = Livre("1984", "George Orwell", 1949, 9.90)
    s = l.to_json()
    data = json.loads(s)
    assert data["titre"] == "1984"
    l2 = Livre.from_json(s)
    assert l2 == l
    promo = l.promo(5.0)
    assert promo.prix == 5.0
    assert l.prix == 9.90  # immuable

def test_ordering_by_prix():
    a = Livre("A", "X", 2000, 5.0)
    b = Livre("B", "Y", 2001, 7.0)
    assert a < b
    assert sorted([b, a]) == [a, b]

def test_promo_negative():
    l = Livre("T", "A", 2020, 10.0)
    with pytest.raises(ValueError):
        l.promo(-1)
