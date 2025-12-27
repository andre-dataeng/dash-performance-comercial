import pandas as pd

def processar_etl_comercial():
    """
    ETL fiel à estrutura do projeto de André:
    Tabelas: Produtos, Clientes, Lojas, Estoque e Vendas.
    """
    
    # 1. SIMULAÇÃO DE CARGA (Conforme suas imagens)
    # Tabela Produtos (image_58044c.png)
    produtos_data = {
        'ProdutoID': [1, 2, 3],
        'Produto': ['Camiseta Básica', 'Camiseta Estampada', 'Blusa Social'],
        'Preco_Unitario': [59.9, 69.9, 129.9],
        'Custo_Unitario': [25.0, 28.0, 60.0]
    }
    
    # Tabela Vendas (image_580521.png)
    vendas_data = {
        'VendaID': [1, 2, 3, 4],
        'Data_Venda': ['2025-01-03', '2025-01-10', '2025-01-05', '2025-01-30'],
        'ProdutoID': [6, 10, 4, 13],
        'Quantidade': [1, 4, 4, 2],
        'Desconto': [15, 5, 0, 15]
    }

    df_produtos = pd.DataFrame(produtos_data)
    df_vendas = pd.DataFrame(vendas_data)

    print("--- Iniciando Processamento de Dados (Fiel ao Schema) ---")

    # 2. TRANSFORMAÇÃO (Lógica de Engenharia)
    # Cruzando Vendas com Produtos para ter os preços e custos
    df_final = pd.merge(df_vendas, df_produtos, on='ProdutoID', how='left')

    # Cálculo de Faturamento Líquido (Preço * Qtd - Desconto)
    df_final['Faturamento_Liquido'] = (df_final['Preco_Unitario'] * df_final['Quantidade']) - df_final['Desconto']

    # Cálculo de Custo Total
    df_final['Custo_Total'] = df_final['Custo_Unitario'] * df_final['Quantidade']

    # Cálculo de Lucro e Margem %
    df_final['Lucro'] = df_final['Faturamento_Liquido'] - df_final['Custo_Total']
    df_final['Margem_Percentual'] = (df_final['Lucro'] / df_final['Faturamento_Liquido']) * 100

    # 3. CARGA (Visualização do Resultado)
    print("ETL Concluído! KPIs calculados com sucesso.")
    print(df_final[['VendaID', 'Data_Venda', 'Faturamento_Liquido', 'Lucro', 'Margem_Percentual']].head())

    return df_final

if __name__ == "__main__":
    processar_etl_comercial()
