### Sentiment Analysis Web App

This repository contains a Streamlit web application for sentiment analysis. The application is built to classify the sentiment of text input into three categories: Negative, Neutral, and Positive. It uses a machine learning model trained on a dataset of reviews.

### Installation

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

### Running the App

After installing the requirements, you can run the app using the following command:

```bash
streamlit run app.py
```

### Notes

- The trained machine learning model is saved as `sentiment_analysis_model.h5` in the root directory of this repository.
- The `tokenizer.pickle` file contains the tokenizer used to preprocess text data for the machine learning model. It allows the app to convert input text into sequences of integers for prediction.

### Additional Documentation

All the detailed notes, explanations, and the process of creating the machine learning model can be found in the `create_model_review.ipynb` Jupyter Notebook file.

### Usage

1. Run the app using the `streamlit run app.py` command.
2. Once the app is running, you can enter text in the provided input field.
3. Click the "Predict" button to see the sentiment classification for the entered text.
4. The app will display the predicted sentiment as either Negative, Neutral, or Positive.

### About

This project was created as a technical assessment for the AI Engineer role at KEcilin. It demonstrates the deployment of a machine learning model for sentiment analysis using Streamlit. For a detailed understanding of the model creation process, please refer to the `create_model_review.ipynb` notebook.
