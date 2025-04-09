import pandas as pd

# Exemplo de dados de receitas (poderia vir de um arquivo JSON/CSV)
receitas = {
    "Segunda": {"prato": "Macarrão com brócolis", "ingredientes": ["macarrão", "brócolis", "alho"]},
    "Terça": {"prato": "Frango assado com batatas", "ingredientes": ["frango", "batatas", "cebola"]},
    # ... adicione mais receitas
}

def gerar_lista_compras(plano_semanal):
    """Gera uma lista de compras a partir de um plano de refeições."""
    lista_compras = {}
    for dia, detalhes in plano_semanal.items():
        for ingrediente in detalhes["ingredientes"]:
            lista_compras[ingrediente] = lista_compras.get(ingrediente, 0) + 1  # Conta ingredientes
    return lista_compras

plano_semanal = {
    "Segunda": receitas["Segunda"],
    "Terça": receitas["Terça"],
    # ... adicione mais dias
}

lista_final = gerar_lista_compras(plano_semanal)
print(lista_final)