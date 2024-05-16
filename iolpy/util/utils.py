
def format_stock_data(data):
    formatted_data = {
        "symbol": data.get("Simbolo"),
        "price": data.get("UltimoPrecio"),
        "name": data.get("Nombre")
    }
    return formatted_data
