from .util.const import _ROOT_URL_
import requests

from bs4 import BeautifulSoup
import pandas as pd


def get_stocks():
    print(_ROOT_URL_)
    response = requests.get(_ROOT_URL_)
    # print("Response: ", response.status_code)
    # print(response.text[:200])

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.title)
    # print(soup.prettify())

    html_tables = soup.find_all("table")
    # print("Cantidad de tablas: ", len(html_tables))

    first_table = html_tables[0]

    # Apply find_all() function with `tr` element on first_table
    all_tr = first_table.find("tbody").find_all("tr")
    # print(all_tr[0].prettify())

    cotization_table = []

    for row in all_tr:
        row_data = {}
        columns = row.find_all("td")
        for column in columns:
            try:
                # data-field is the name of the field
                # data-order is the value of the field
                row_data[column["data-field"]] = column["data-order"]
            except Exception as e:
                try:
                    row_data["Simbolo"] = "".join([x for x in column.find("b").text if x not in [" ", "\r", "\n"]])
                    row_data["Nombre"] = column.find("i")["title"]
                except Exception as e:
                    print(f"How exceptional! {e}")
        cotization_table.append(row_data)

    cotization_df = pd.DataFrame(cotization_table)
    return cotization_df
