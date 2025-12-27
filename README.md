# 📊 Dashboard de Performance Comercial - Star Schema & ETL Python

Este projeto demonstra a construção de um ecossistema de dados completo. A partir de bases transacionais em Excel, utilizei **Python** para o tratamento de dados (ETL) e o **Power BI** para modelagem dimensional e visualização estratégica.

## 🏗️ Arquitetura de Dados (Modelo Dimensional)
O projeto foi estruturado utilizando o conceito de **Star Schema**, garantindo performance e integridade nos cálculos:

- **Tabela Fato:** - `Vendas`: Contém as chaves para dimensões e as métricas de quantidade e descontos.
- **Tabelas Dimensão:**
  - `Produtos`: Detalhes de SKU, Preço Unitário e Custo Unitário.
  - `Clientes`: Dados demográficos (Gênero, Cidade, Estado).
  - `Lojas`: Localização das unidades físicas e online.
  - `Estoque`: Posição de inventário por loja e produto.

## 🛠️ O Toque de Engenharia: ETL com Python
Diferente de uma análise comum, este projeto utiliza o script `etl_process.py` para realizar o processamento pesado antes da carga no BI:
- **Tratamento de Chaves:** Relacionamento entre `VendaID` e `ProdutoID` via Pandas.
- **Cálculos de Negócio:** O lucro e a margem percentual são calculados via código, reduzindo o processamento necessário no Power BI.
- **Limpeza:** Padronização de nomes de colunas e tipos de dados.

## 📊 KPIs Implementados
- **Faturamento Líquido:** (Preço * Quantidade) - Desconto.
- **Margem de Lucro %:** Proporção de lucro sobre o faturamento líquido.
- **Performance por Categoria:** Identificação de produtos com maior giro.
- **Análise Geográfica:** Vendas e lucratividade distribuídas por Estado (SP, RJ, MG).

## 📸 Visualização do Modelo

![Modelo Dimensional](Img%20dash.png)

---
*Desenvolvido por André - Engenheiro de Dados*
