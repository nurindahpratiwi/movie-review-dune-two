import streamlit as st
import keras
import pickle5 as pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = keras.models.load_model('sentiment_analysis_model.h5')
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


def predict_sentiment(text):
    # Tokenize and pad the input text
    text_sequence = tokenizer.texts_to_sequences([text])
    text_sequence = pad_sequences(text_sequence, maxlen=100)

    # Make a prediction using the trained model
    predicted_rating = model.predict(text_sequence)[0]
    print(predicted_rating[2])
    if np.argmax(predicted_rating) == 0:
        return 'Negative'
    elif np.argmax(predicted_rating) == 1:
        return 'Neutral'
    else:
        return 'Positive'
    

st.title("Sentiment Analysis Web App")
st.caption("Technical Assesment done by Nur Indah Pratiwi")
st.markdown('''
    :red[Movie] :violet[review] :green[for] :blue[Dune] :grey[part]
    :rainbow[Two].''')
st.divider()

# Buat text input dari user
text = st.text_area("Enter your review here", "This movie is great, I loved it!")

if st.button("Predict"):
    predicted_sentiment = predict_sentiment(text)
    st.write(predicted_sentiment)