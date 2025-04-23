from classes import Extraction, TransformAndLoad

# Extract

read_csv = Extraction('data/dados_vendas.csv')
read_csv.read_csv()

# Transform

transform_csv = TransformAndLoad('data/dados_vendas.csv')
transform_csv.sales_by_state()
transform_csv.best_selling_product()
transform_csv.customers_most_purchases()
transform_csv.monthly_recipe()

