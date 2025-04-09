import pandas as pd
from openpyxl import Workbook

def gerar_relatorio_vendas(dados, arquivo_excel):
    """Gera um relatório de vendas em Excel."""
    df = pd.DataFrame(dados)
    workbook = Workbook()
    sheet = workbook.active
    for r in dataframe_to_rows(df, index=False, header=True):
        sheet.append(r)
    workbook.save(arquivo_excel)

# Dados de exemplo (substitua pelos seus dados reais)
dados_vendas = {
    "Produto": ["A", "B", "C"],
    "Vendas": [100, 150, 120],
    "Data": ["2023-10-26", "2023-10-26", "2023-10-26"]
}

gerar_relatorio_vendas(dados_vendas, "relatorio_vendas.xlsx")