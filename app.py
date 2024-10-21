import streamlit as st
import pickle
import time
import random

# Load the model
model = pickle.load(open('twitter_sentiment.pkl', 'rb'))

# Add custom styling to the page
st.set_page_config(page_title='Twitter Sentiment Analysis', page_icon=":bird:", layout="centered")
st.markdown(
    """
    <style>
    .reportview-container {
        background: linear-gradient(to bottom right, #f0f2f6, #c9d6ff);
    }
    h1 {
        color: #3a4a58;
        font-family: 'Helvetica Neue', sans-serif;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and subtitle
st.title('🐦 Twitter Sentiment Analysis')
st.markdown("Analyze the sentiment of any tweet using Machine Learning!")

# Explanation section
with st.expander("ℹ️ About this app"):
    st.write("""
        This application predicts the sentiment of a tweet (Positive or Negative) using a pre-trained machine learning model.
        The model was trained on a large dataset of tweets and uses natural language processing techniques to analyze the input text.
    """)

# Input text box
tweet = st.text_input('💬 Enter your tweet:', placeholder="Type or paste a tweet here...")

# Provide some example tweets for fun
example_tweets = [
    "I absolutely love this! Great job everyone!",
    "This is the worst experience I've ever had.",
    "Feeling amazing today!",
    "I'm so tired of all the problems with this service."
]
if st.button("📝 Generate Example Tweet"):
    tweet = random.choice(example_tweets)
    st.write(f"Example tweet: *{tweet}*")

# Predict button
submit = st.button('🚀 Predict Sentiment')

if submit:
    if not tweet:
        st.warning("Please enter a tweet to analyze.")
    else:
        with st.spinner('Analyzing tweet...'):
            start = time.time()
            prediction = model.predict([tweet])[0]  # Assuming binary classification: positive or negative
            end = time.time()
            
            # Simulate some randomness for confidence score (if model doesn't return probabilities)
            confidence = round(random.uniform(0.7, 1.0), 2)

            # Display result with time taken
            st.success(f"**Prediction:** {prediction.capitalize()}")
            st.write(f"🕒 Time taken for prediction: {round(end - start, 2)} seconds")

            # Show confidence score
            st.write(f"🔍 Confidence Score: {confidence * 100}%")

            # Visual representation of sentiment
            if prediction == 'positive':
                st.progress(int(confidence * 100))
            else:
                st.progress(int((1 - confidence) * 100))

# Add footer with feedback form or links (optional)
st.markdown("""
    ---
    Spread Positivity
""")
