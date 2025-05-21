import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv('data/processed/cleaned_sales.csv', index_col='date', parse_dates=True)
model = ARIMA(df['sales'], order=(5, 1, 0))
model_fit = model.fit()
model_fit.save('models/arima_model.pkl')
