import pandas as pd
# import pytest
from iolpy.stocks import get_stocks


# def test_get_stocks(monkeypatch):
#     class MockResponse:
#         @staticmethod
#         def text():
#             return """
#             <html>
#             <body>
#                 <table>
#                     <tbody>
#                         <tr>
#                             <td data-field="UltimoPrecio" data-order="903,000"></td>
#                             <td><b>ALUA</b></td>
#                             <td><i title="Aluar"></i></td>
#                         </tr>
#                     </tbody>
#                 </table>
#             </body>
#             </html>
#             """

#         status_code = 200

#     def mock_get(*args, **kwargs):
#         return MockResponse()

#     monkeypatch.setattr("requests.get", mock_get)
#     data = get_stocks()
#     assert not data.empty
#     assert data.loc[0, "UltimoPrecio"] == "903,000"
#     assert data.loc[0, "Simbolo"] == "ALUA"
#     assert data.loc[0, "Nombre"] == "Aluar"


def test_get_cotizations():
    cotization_df = get_stocks()
    assert isinstance(cotization_df, pd.DataFrame)
    assert cotization_df.shape[1] == 8
    assert cotization_df.shape[0] > 0
    assert cotization_df.columns.to_list() == [
        'Simbolo', 'Nombre', 'UltimoPrecio', 'Variacion', 'Apertura', 'Minimo', 'Maximo', 'UltimoCierre']
    assert cotization_df['Simbolo'].str.len().max() <= 5
    assert cotization_df['Nombre'].str.len().max() > 0
    # assert cotization_df['UltimoPrecio'].astype(float).min() > 0
    # # assert cotization_df['Variacion'].astype(float).min() < 0
    # assert cotization_df['Apertura'].astype(float).min() > 0
    # assert cotization_df['Minimo'].astype(float).min() > 0
    # assert cotization_df['Maximo'].astype(float).min() > 0
    # assert cotization_df['UltimoCierre'].astype(float).min() > 0
    # cotization_df.to_excel('cotization_table.xlsx', index=False)
