import numpy as np
import joblib
import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_tfidf_matrix(descriptions, ngram_range=(1, 1), max_features=None, max_df=1, min_df=1):
    vectorizer = TfidfVectorizer(
        ngram_range=ngram_range,
        max_features=max_features,
        max_df=max_df,
        min_df=min_df
    )

    tfidf = vectorizer.fit_transform(descriptions)

    return tfidf

def save_model_artifacts(vectorizer):
    joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

def find_top_k(vectorizer, k=5):
    batch_size = 256

    epoch = vectorizer.shape[0] // batch_size + 1

    top_k_result = []
    dataset_size = vectorizer.shape[0]
    start = datetime.datetime.now()
    for i in range(epoch):
        start_idx = i * batch_size
        end_idx = min(start_idx + batch_size, dataset_size)

        print(f"batch {i+1} : {start_idx} -> {end_idx}")

        vector = vectorizer[i * batch_size: i * batch_size + batch_size]
        cosine_sim = cosine_similarity(vector, vectorizer)
        # Get top-k for each row in batch
        for j in range(cosine_sim.shape[0]):
            row_sim = cosine_sim[j]
            row_sim[start_idx + j] = -1  # ignore self-similarity
            top_k_idx = row_sim.argsort()[-k:][::-1]
            top_k_scores = row_sim[top_k_idx]
            result = list(zip(top_k_idx, top_k_scores))
            top_k_result.append(result)
            # break
        break        
    
    end = datetime.datetime.now()
    time_used = end - start

    return top_k_result, time_used