import pandas as pd

class Extraction:
    def __init__(self, csv_file: str):
        self.df = csv_file

    def read_csv(self):
        csv_read = pd.read_csv(self.df)
        return csv_read
    
class TransformAndLoad:
    def __init__(self,csv_file: str):
        self.df = pd.read_csv(csv_file)

    def sales_by_state(self):
        self.df['vendas_totais'] = self.df['quantidade'] * self.df['preco_unitario']
        df_grouped_state = self.df.groupby('estado')['vendas_totais'].sum().reset_index()
        return df_grouped_state.to_csv('output/sales_by_state.csv', index=False)

    def best_selling_product(self):
        df_grouped_category = self.df.groupby('categoria')['quantidade'].sum().reset_index()
        return df_grouped_category.to_csv('output/best_selling_product.csv', index=False)
    
    def customers_most_purchases(self):
        df_grouped_customers = self.df.groupby('cliente_id')['quantidade'].sum().reset_index()
        top5_customers = df_grouped_customers.sort_values(by='quantidade', ascending=False).head(5)
        return top5_customers.to_csv('output/customers_most_purchases.csv', index=False)
    
    def monthly_recipe(self):
        self.df['data_compra'] = pd.to_datetime(self.df['data_compra'])
        self.df['mes'] = self.df['data_compra'].dt.to_period('M')
        df_grouped_monthly = self.df.groupby('mes')['preco_unitario'].sum().reset_index()
        return df_grouped_monthly.to_csv('output/monthly_recipe.csv', index=False)

