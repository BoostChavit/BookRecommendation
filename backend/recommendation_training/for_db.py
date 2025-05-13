import re
import pandas as pd
import nltk
import csv
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

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

books_data_df = pd.read_csv("dataset/books_data.csv")
books_data_df = books_data_df[['Title', 'description', 'authors', 'image', 'categories', 'ratingsCount']]

books_data_df = books_data_df.applymap(lambda x: x.replace('"', "'") if isinstance(x, str) else x)
import ast

def clean_author(author_str):
    try:
        # Safely convert string to list
        authors = ast.literal_eval(author_str)
        if isinstance(authors, list):
            return ', '.join(authors)
    except Exception:
        pass
    return author_str
books_data_df['authors'] = books_data_df['authors'].apply(clean_author)
books_data_df['categories'] = books_data_df['categories'].apply(clean_author)
# books_data_df['TitleLower'] = books_data_df['Title'].astype(str).str.lower()
# books_data_df = books_data_df.drop_duplicates(subset='TitleLower')
# books_data_df = books_data_df.drop('TitleLower', axis=1)
# books_data_df['categories'] = books_data_df['categories'].astype(str).apply(clean_text)

books_data_df.dropna(inplace=True)
books_data_df.to_csv('db.csv', index=False, quotechar='"', quoting=csv.QUOTE_ALL)

# df = pd.read_csv('db.csv')
# for row in df['ratingsCount']:
#     print(row)
# print(df['ratingsCount'].astype(float))