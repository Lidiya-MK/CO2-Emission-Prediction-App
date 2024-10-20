import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
from flask import Flask, request, render_template
import matplotlib.pyplot as plt
import os

app = Flask(__name__)


model = joblib.load('co2_model.pkl')


def create_plot(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Volume'], data['Weight'], c=data['CO2'], cmap='viridis', alpha=0.5)
    plt.colorbar(label='CO2 emissions')
    plt.xlabel('Volume')
    plt.ylabel('Weight')
    plt.title('CO2 Emissions by Car Volume and Weight')
    plt.savefig('static/co2_plot.png')
    plt.close()


data = pd.read_csv('./data/DATA.csv')
data.columns = data.columns.str.strip()
data['Volume'] = pd.to_numeric(data['Volume'], errors='coerce')
data['Weight'] = pd.to_numeric(data['Weight'], errors='coerce')
data['CO2'] = pd.to_numeric(data['CO2'], errors='coerce')
data = data.dropna(subset=['Volume', 'Weight', 'CO2'])


create_plot(data)

@app.route('/')
def home():
    return render_template('page.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    volume = float(request.form['volume'])
    weight = float(request.form['weight'])
    prediction = model.predict([[volume, weight]])[0]

    return render_template('page.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
