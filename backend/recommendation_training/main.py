import re
import nltk
import mlflow
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from recommenders.tfidf import build_tfidf_matrix, save_model_artifacts, find_top_k


nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    # Lowercase
    text = text.lower()

    # Remove punctuation and digits
    text = re.sub(r'[^a-z\s]', '', text)
    # Tokenize and remove stopwords
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]

    # Join back to string
    return ' '.join(words)

ngram_range = (1,1)

books_data_df = pd.read_csv("db.csv")
books_data_df = books_data_df[['Title', 'description', 'categories', 'ratingsCount']]

# books_data_df['TitleLower'] = books_data_df['Title'].astype(str).str.lower()
# books_data_df = books_data_df.drop_duplicates(subset='TitleLower')
# books_data_df = books_data_df.drop('TitleLower', axis=1)
books_data_df['categories'] = books_data_df['categories'].astype(str).apply(clean_text)

# books_data_df = books_data_df.dropna()

books_data_df['train'] = books_data_df[['Title', 'description', 'categories']].agg(' '.join, axis=1) 
books_data_df['train'] = books_data_df['train'].apply(clean_text)

description_books = books_data_df['train'].to_numpy()

ratings = books_data_df['ratingsCount'].to_numpy()

tfidf = build_tfidf_matrix(descriptions=description_books, ngram_range=ngram_range, max_df=0.8, min_df=1)

print(tfidf.shape)
save_model_artifacts(tfidf)

# top_k_result, time_used = find_top_k(tfidf, 5)

# num = np.arange(5)
# num = np.arange(256)
# np.random.shuffle(num)
# num = num[:5]
# for i in range(len(top_k_result)):
#     if i in num:
#         name = books_data_df['Title'].iloc[i]
#         print(f"name : {name}")
#         print("top similarity :")
#         for j in top_k_result[i]:
#             print(f" - {books_data_df['Title'].iloc[j[0]]} : {(j[1]*100):.2f}")
#         print()    
