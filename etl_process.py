import pandas as pd
import numpy as np

def clean_sales_data(file_path):
    """
    Simulação de um processo de ETL para limpeza de dados comerciais.
    """
    # 1. Extração (Imagine que aqui estamos lendo um CSV ou base SQL)
    # df = pd.read_csv(file_path)
    
    # Criando dados fictícios para demonstração do script
    data = {
        'Data': ['2025-01-01', '2025-01-02', '2025-01-02', None],
        'Produto': ['Produto A', 'Produto B', 'Produto A', 'Produto C'],
        'Valor_Venda': [1500.50, 2300.00, 1200.00, 500.00],
        'Custo': [900.00, 1500.00, 800.00, 300.00]
    }
    df = pd.DataFrame(data)

    print("--- Iniciando Processamento de Dados ---")

    # 2. Transformação (Lógica de Engenharia)
    # Removendo valores nulos
    df = df.dropna()

    # Criando métricas calculadas no nível de linha (Engenharia de Features)
    df['Margem_Lucro'] = df['Valor_Venda'] - df['Custo']
    df['Percentual_Margem'] = (df['Margem_Lucro'] / df['Valor_Venda']) * 100

    # 3. Carga (O dado limpo pronto para o Power BI ou Data Warehouse)
    print("Dados limpos e processados com sucesso!")
    print(df.head())
    
    # df.to_csv('vendas_processadas.csv', index=False)
    return df

if __name__ == "__main__":
    clean_sales_data('vendas_brutas.csv')
