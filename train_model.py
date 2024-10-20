import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

data = pd.read_csv('./data/Coffee-2012.csv')

data.columns = data.columns.str.strip()

print("Cleaned column names:", data.columns.tolist())

data['Unnamed: 4'] = pd.to_numeric(data['Unnamed: 4'].str.replace(',', ''), errors='coerce')

data = data.dropna(subset=['Unnamed: 3', 'Unnamed: 4'])

# Ensure the 'Unnamed: 3' column is treated as numeric
data['Unnamed: 3'] = pd.to_numeric(data['Unnamed: 3'], errors='coerce')

# Check unique years in the dataset
unique_years = data['Unnamed: 3'].unique()
print("Unique years in the dataset:", unique_years)

# Filter data for the year 2004
data = data[data['Unnamed: 3'] == 2004]

# Check if any data is left after filtering
if data.empty:
    print("No data found for the year 2004.")
else:
    print(f"Data for the year 2004 found: {len(data)} records.")

X = data.iloc[:, 3].values.reshape(-1, 1)
y = data.iloc[:, 4].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, 'coffee_price_model.pkl')

print("Model trained and saved as 'coffee_price_model.pkl'")
