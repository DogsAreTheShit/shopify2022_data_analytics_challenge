import pandas as pd
from datetime import timedelta
from scipy import stats
import numpy as np

# DATE RANGE
date = pd.to_datetime("2017-03-01 00:00:00")
end_date = pd.to_datetime(date) + timedelta(days=30)

# LOAD DATASET
df = pd.read_csv('shop_dataset.csv')
df = df.sort_values(by="created_at")

# FILTER RANGE
df['created_at'] = pd.to_datetime(df['created_at'], format='%Y-%m-%d')
filtered_df = df.loc[(df['created_at'] >= date) & (df['created_at'] <= end_date)]

# FILTER ANOMOLIES
filtered_df = filtered_df[np.abs(filtered_df.order_amount-filtered_df.order_amount.mean()) <= (3*filtered_df.order_amount.std())]

# GET AOV
aov = filtered_df["order_amount"].mean()

# PRINT AOV TO CONSOL
print("Average Order Value (", date, " - ", end_date, "): ", aov)
