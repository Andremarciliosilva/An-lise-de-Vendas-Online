### 📦 Projeto de Engenharia de Dados: Análise de Vendas Online


Este pipeline de Engenharia de Dados foi desenvolvido pra **extrair, transformar
e analisar** dados de vendas utilizando **Python** e **Pandas**. 

---

#### 🎯 Objetivo

Analisar dados de vendas simulados de uma loja online, respondendo perguntas como:

- Qual o total de vendas por estado?
- Quais são os produtos mais vendidos por categoria?
- Quem são os clientes que mais compram?
- Qual é a receita mensal da loja?

---

#### 🛠️ Tecnologias e Ferramentas

- Python 3.10+
- Pandas (para análise e manipulação dos dados)
- Matplotlib / Seaborn (para gráficos)
- VS Code

---

#### 📁 Estrutura do Projeto

```bash
├── data/
│   └── dados_vendas.csv        # Dados simulados
├── src/
│   ├── etl.py                  # Pipeline de leitura, limpeza e transformação
│   └── analise.py              # Cálculos e análises
├── notebooks/
│   └── analise_vendas.ipynb    # Notebook exploratório
├── output/
│   └── relatorios.csv          # Relatórios salvos (exportados)
├── requirements.txt
└── README.md
```

--- 

🧪 **Dataset**

O dataset contém 500 registros com as seguintes colunas:

•	pedido_id
•	data_compra
•	cliente_id
•	produto
•	categoria
•	quantidade
•	preco_unitario
•	cidade
•	estado
•	forma_pagamento

---

📊 **Análises Realizadas**

•	Receita total por estado
•	Produto mais vendido por categoria
•	Top 5 clientes por volume de compras
•	Receita mensal ao longo do ano

---

🧠 **Aprendizados**

•	Manipulação e limpeza de dados com Pandas
•	Agrupamentos e análises estatísticas
•	Visualizações com gráficos
•	Estruturação de um projetos de dados