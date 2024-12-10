import streamlit as st
from src.scraper import get_infomoney_data
from src.parser import soup_to_dictionary
from src.parser import soup_to_dataframe
from src.parser import parse_values
import plotly.express as px

def encontrar_outliers_iqr(serie):
    Q1 = serie.quantile(0.25)
    Q3 = serie.quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    outliers = serie[(serie < limite_inferior) | (serie > limite_superior)]
    return outliers


st.title("Dashboard de Análise - InfoMoney")
st.write("""
Este dashboard apresenta uma tabela completa obtida via web scraping do site InfoMoney dos dados analisados e um gráfico interativo 
para explorar outliers em diferentes métricas.
A captura dos dados seguiu as [política de privacidade](https://www.infomoney.com.br/politica-de-privacidade/) do site InfoMoney e respeitou o arquivo [`robots.txt`](https://www.infomoney.com.br/robots.txt/).
""")
st.subheader("Tabela de Dados Completos")

soup = get_infomoney_data()
if soup:
    lista_dicts = soup_to_dictionary(soup)
    df = soup_to_dataframe(soup)
    df = parse_values(df)
    st.dataframe(df)

opcao_coluna = st.selectbox(
    "Selecione a coluna para análise de outliers:",
    ["Var. Dia (%)","Var. Sem. (%)"," Var. Mês (%)", "Var. Ano (%)", "Var. 12M (%)"]
)

outliers = encontrar_outliers_iqr(df[opcao_coluna])

if outliers.empty:
    st.write("Nenhum outlier encontrado para esta coluna.")
else:
    st.write("Ativos Outliers:")
    df_outliers = df[df[opcao_coluna].isin(outliers)]
    st.dataframe(df_outliers)

    fig = px.box(
        df,
        y=opcao_coluna,
        points="all",
        hover_data=["Ativo"],
        title=f"Boxplot Interativo - {opcao_coluna}"
    )

    st.plotly_chart(fig, use_container_width=True)