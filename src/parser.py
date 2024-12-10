import pandas as pd

def soup_to_dictionary(soup):
    if soup:
        tabela = soup.find("table", {"id": "altas_e_baixas"})
        
        if tabela:
            header_row = tabela.find("tr")
            headers = [th.get_text(strip=True) for th in header_row.find_all("th")]

            data_rows = tabela.find_all("tr")[1:]
            lista_dicts = []
            for row in data_rows:
                cells = [td.get_text(strip=True) for td in row.find_all("td")]
                row_dict = dict(zip(headers, cells))
                lista_dicts.append(row_dict)

            return lista_dicts
        else:
            print("Tabela com id 'altas_e_baixas' não encontrada.")
            return None
    else:
        print("Nenhum dado para parsear.")
        return None

def soup_to_dataframe(soup):
    dados = soup_to_dictionary(soup)
    if dados:
        return pd.DataFrame(dados)
    else:
        return None
    
def parse_values(df):
    if df is not None:
        df[["Volume", "Volume Unid."]] = df["Volume"].str.split(" ", expand=True)
        float_columns = [
            "Último (R$)",
            "Var. Dia (%)",
            "Var. Sem. (%)",
            "Var. Mês (%)",
            "Var. Ano (%)",
            "Var. 12M (%)",
            "Val. Mín",
            "Val. Máx",
            "Volume"
        ]

        for col in float_columns:
            df[col] = df[col].str.replace(",", ".").astype(float)

        return df
    else:
        return None