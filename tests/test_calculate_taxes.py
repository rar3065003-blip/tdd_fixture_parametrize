import pytest
from src.taxes import calculate_taxes


# def test_func1(test_calculate_taxes):
#     assert calculate_taxes(*test_calculate_taxes) == [183304.095]
@pytest.mark.parametrize("x, y, expected", [
    ([154687.0], 18.5, [183304.095]),
    ([154687.0], -18.5, "Неверный налоговый процент"),
    ([-154687.0], 18.5, 'Неверная цена'),
    ])
def test_calculate_taxes(x, y, expected):
    assert calculate_taxes(x, y) == expected
