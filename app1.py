
from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load('models/spam_detection_model.pkl')
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the SMS text from the form
    sms_text = request.form['sms_text']

    # Vectorize the input text
    sms_vectorized = vectorizer.transform([sms_text])

    # Make prediction using the loaded model
    prediction = model.predict(sms_vectorized)[0]
    if prediction == 0:
        result = 'Not Spam'
    else:
        result = 'Spam'

    return render_template('index.html', prediction_result=result, sms_text=sms_text)

if __name__ == '__main__':
    app.run(debug=True)