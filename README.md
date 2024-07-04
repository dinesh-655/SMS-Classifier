
# SMS Spam Classifier

Welcome to the SMS Spam Classifier project! This repository contains all the files and resources needed to build and run a machine learning model to classify SMS messages as spam or not spam.

## Project Structure

- `app1.py`: This is the main Python script for running the web application.
- `sms_cluster.ipynb`: A Jupyter notebook containing the code for preprocessing the data, training the model, and evaluating its performance.
- `index.html`: The HTML file for the web application's frontend.
- `spam.csv`: The dataset containing SMS messages labeled as spam or not spam.
- `spam_detection_model.pkl`: The trained machine learning model for spam detection.
- `tfidf_vectorizer.pkl`: The trained TF-IDF vectorizer for transforming text data into numerical features.

## Installation

1. Clone the repository:


git clone https://github.com/dinesheswarreddy/SMS-Spam-Classifier.git
cd SMS-Spam-Classifier


2. Install the required Python packages:


pip install -r requirements.txt


## Usage

1. Run the web application:


python app1.py


2. Open your web browser and go to `http://127.0.0.1:5000/` to access the SMS Spam Classifier web application.

## Dataset

The dataset (`spam.csv`) contains SMS messages labeled as "spam" or "ham" (not spam). It is used for training and evaluating the machine learning model.

## Model

The machine learning model (`spam_detection_model.pkl`) is trained using the data in `spam.csv`. The TF-IDF vectorizer (`tfidf_vectorizer.pkl`) is used to convert the text data into numerical features for model training and prediction.

## Notebooks

- `sms_cluster.ipynb`: Contains the code for data preprocessing, model training, evaluation, and saving the trained model and vectorizer.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
