import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    never_order = customers[~customers['id'].isin(orders['customerId'])]
    return never_order[['name']].rename(columns={'name': 'Customers'})
 
