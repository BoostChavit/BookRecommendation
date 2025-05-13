import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class BookRecommender:
    def __init__(self, tfidf_vectorizer):
        self.tfidf_vectorizer = tfidf_vectorizer
    
    def recommend(self, id, top_k=5):
        id = id -1
        query_vec = self.tfidf_vectorizer[id]
        similarities = cosine_similarity(query_vec, self.tfidf_vectorizer).flatten()
        similarities[id] = -1
        top_indices = similarities.argsort()[::-1][:top_k]
        result = []
        for i in top_indices:
            result.append(int(i))
        return result