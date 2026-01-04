import pytest
from src.taxes import calculate_taxes

@pytest.fixture
def prices():
    return [100, 200, 300]
# def test_func1(test_calculate_taxes):
#     assert calculate_taxes(*test_calculate_taxes) == [183304.095]
@pytest.mark.parametrize("x, y, expected", [
    ([154687.0], 18.5, [183304.095]),
    ([154687.0], -18.5, "Неверный налоговый процент"),
    ([-154687.0], 18.5, 'Неверная цена'),
    ])
def test_calculate_taxes(x, y, expected):
    assert calculate_taxes(x, y) == expected

def test_calcullate_invalid_tax_rate(prices):
    with pytest.raises(ValueError):
        calculate_taxes(prices, tax_rate = -1)


def test_calculate_invalid_prices():
    with pytest.raises(ValueError):
        calculate_taxes([0, -1], tax_rate = 10)
