from iolpy.util.utils import format_stock_data


def test_format_stock_data():
    data = {"Simbolo": "AAPL", "UltimoPrecio": "150", "Nombre": "Apple Inc."}
    formatted = format_stock_data(data)
    assert formatted["symbol"] == "AAPL"
    assert formatted["price"] == "150"
    assert formatted["name"] == "Apple Inc."
