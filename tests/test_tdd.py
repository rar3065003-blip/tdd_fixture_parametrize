# from main import calculate_tax
from src.taxes import calculate_tax

def test_calculate_tax():
    result = calculate_tax(100.0, 10.0)
    assert result == 110

    result = calculate_tax(-100.0, 10.0)
    assert result == "Неверная цена"

    result = calculate_tax(100.0, -10.0)
    assert result == "Неверный налоговый процент"

    result = calculate_tax(100.0, 100.0)
    assert result == "Неверный налоговый процент"

    result = calculate_tax("100.0", 10.0)
    assert result == "Неверный формат данных цены"

    result = calculate_tax(100.0, "10.0")
    assert result == "Неверный формат данных налогового процента"

    result = calculate_tax(100.0, [10.0])
    assert result == "Неверный формат данных налогового процента"

    result = calculate_tax([100.0], 10.0)
    assert result == "Неверный формат данных цены"
