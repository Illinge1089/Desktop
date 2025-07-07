
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(location, interest):
    df = pd.read_csv("data/jobs.csv")
    df['combined'] = df['location'] + " " + df['industry'] + " " + df['description']

    user_input = location + " " + interest
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['combined'].tolist() + [user_input])
    
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    top_indices = cosine_sim[0].argsort()[-5:][::-1]
    
    return df.iloc[top_indices].to_dict(orient='records')
