from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)


model = joblib.load('coffee_price_model.pkl')


@app.route('/')
def index():
    return render_template('page.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
       
        production_year = int(request.form['year'])
        
 
        prediction = model.predict([[production_year]])[0]


        return jsonify({'predicted_price': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
