### 📦 Projeto: Análise de Vendas Online


Este pipeline de Engenharia de Dados foi desenvolvido pra **extrair, transformar
e analisar** dados de vendas utilizando **Python**, **Pandas** e **Matplotlib**. 
A ideia foi desenvolver um pipeline que possa ser reutilizado em vários arquivos csv's 
que possuam a mesma estrutura de colunas, por isso optei por construir classes com métodos 
que possam ser utilizados pra analisar vários arquivos, bastando trocar apenas o nome do 
arquivo que é passado quando a classe é invocada.

---

#### 🎯 Objetivo

Analisar dados de vendas simulados de uma loja online, respondendo perguntas como:

- Qual o total de vendas por estado?
- Quais são os produtos mais vendidos por categoria?
- Quem são os clientes que mais compram?
- Qual é a receita mensal da loja?

---

#### 🛠️ Tecnologias e Ferramentas

- Python 3.11.5
- Pandas (para análise e manipulação dos dados)
- Matplotlib (para gráficos)
- VS Code

---

#### 📁 Estrutura do Projeto

```bash
├── data/
│   └── dados_vendas.csv        # Dados simulados
│   └── img                     # Imagens
├── notebooks/
│   └── analise_vendas.ipynb    # Notebook exploratório
├── output/
│   └── relatorios.csv          # Relatórios salvos (exportados)
├── src/
│   ├── analise.py              # Cálculos e análises
│   └── etl.py                  # Pipeline de leitura, limpeza e transformação
├── README.md
└── requirements.txt

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

•	Vendas totais por estado:  
![texto alternativo](img/vendas_totais_por_estado.png)

•	Produto mais vendido por categoria:    
![texto alternativo](img/produtos_mais_vendidos.png)


•	Top 5 clientes por volume de compras:   
![texto alternativo](img/clientes_que_mais_compram.png)

•	Receita mensal ao longo do ano:    


---

🧠 **Aprendizados**

•	Manipulação e limpeza de dados com Pandas  
•	Agrupamentos e análises estatísticas  
•	Visualizações com gráficos  
•	Estruturação de um projetos de dados  
•	Criação de classes com métodos que possam ser reutilizados em outros arquivos 
