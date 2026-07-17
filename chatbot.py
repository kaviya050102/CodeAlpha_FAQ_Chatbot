import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Download required NLP data (first time only)
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")


# Load FAQ dataset
faq_data = pd.read_csv("faq.csv")


questions = faq_data["Question"]
answers = faq_data["Answer"]


# Stop words
stop_words = set(stopwords.words("english"))


# Text cleaning function
def clean_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # Tokenization
    words = word_tokenize(text)

    # Remove stop words
    words = [
        word for word in words 
        if word not in stop_words
    ]

    return " ".join(words)



# Clean all FAQ questions
clean_questions = questions.apply(clean_text)


# Convert text into vectors
vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(clean_questions)



# Chatbot response function
def get_answer(user_question):

    # Clean user input
    cleaned_question = clean_text(user_question)


    # Convert user question to vector
    user_vector = vectorizer.transform(
        [cleaned_question]
    )


    # Calculate similarity
    similarity = cosine_similarity(
        user_vector,
        faq_vectors
    )


    # Find best match
    best_match_index = similarity.argmax()


    # Get confidence score
    confidence = similarity[0][best_match_index]


    # Confidence checking
    if confidence < 0.3:
        return "Sorry, I couldn't find a relevant answer. Please ask something related to Artificial Intelligence or Machine Learning."


    return answers.iloc[best_match_index]