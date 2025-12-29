import pandas as pd
import random

# --- PASSO 1: CRIAR OS DADOS (EXTRAÇÃO SIMULADA) ---
print("Iniciando a criação dos dados...")

# Criando a lista de produtos manualmente para ficar fácil de entender
dados_produtos = {
    'ID': [1, 2, 3, 4],
    'Nome': ['Camiseta Preta', 'Calça Jeans', 'Tênis Esportivo', 'Boné Aba Curva'],
    'Preco': [50.00, 120.00, 250.00, 45.00]
}
df_produtos = pd.DataFrame(dados_produtos)

# Criando as lojas
dados_lojas = {
    'ID': [101, 102],
    'Nome': ['Loja Centro', 'Loja Shopping']
}
df_lojas = pd.DataFrame(dados_lojas)

# --- PASSO 2: GERAR VENDAS (TRANSFORMAÇÃO) ---
print("Gerando 50 vendas aleatórias...")

vendas_lista = []

for i in range(1, 51):  # Vamos criar 50 vendas
    # Sorteia um produto da nossa lista acima
    indice_sorteado = random.randint(0, 3) 
    produto_nome = df_produtos.loc[indice_sorteado, 'Nome']
    preco_unitario = df_produtos.loc[indice_sorteado, 'Preco']
    
    quantidade = random.randint(1, 3)
    valor_total = preco_unitario * quantidade

    # Monta a linha da venda
    venda = {
        'ID_Venda': i,
        'Produto': produto_nome,
        'Qtd': quantidade,
        'Valor_Total': valor_total,
        'Loja_ID': random.choice([101, 102])
    }
    vendas_lista.append(venda)

df_vendas = pd.DataFrame(vendas_lista)

# --- PASSO 3: SALVAR TUDO NO EXCEL (CARGA) ---
print("Salvando o arquivo final...")

with pd.ExcelWriter('loja_roupas_powerbi.xlsx') as writer:
    df_vendas.to_excel(writer, sheet_name='Vendas', index=False)
    df_produtos.to_excel(writer, sheet_name='Produtos', index=False)
    df_lojas.to_excel(writer, sheet_name='Lojas', index=False)

print("Pronto! O arquivo 'loja_roupas_powerbi.xlsx' foi criado.")
