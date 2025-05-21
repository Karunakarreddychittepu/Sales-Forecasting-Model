import pandas as pd

def clean_sales_data(input_path, output_path):
    df = pd.read_csv(input_path, parse_dates=['date'])
    df = df.dropna()
    df.set_index('date', inplace=True)
    df.to_csv(output_path)

# Usage
# clean_sales_data('data/raw/sales.csv', 'data/processed/cleaned_sales.csv')
