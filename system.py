import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationSystem:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.df = None
        self.similarity = None
        self.load_data()
        self.compute_similarity()

    def load_data(self):
        """Load and preprocess the dataset."""
        self.df = pd.read_csv(self.dataset_path)
        
        # Check for missing values
        if self.df['tags'].isnull().any():
            self.df['tags'].fillna('', inplace=True)  # Fill missing tags with empty strings

    def compute_similarity(self):
        """Compute TF-IDF and cosine similarity."""
        vectorizer = TfidfVectorizer(stop_words='english')
        tags_vec = vectorizer.fit_transform(self.df['tags']).toarray()
        self.similarity = cosine_similarity(tags_vec)

    def recommend(self, movie_title):
        """Get top 5 recommendations for a given movie."""
        try:
            movie_index = self.df[self.df['title'] == movie_title].index[0]
            distances = self.similarity[movie_index]
            movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
            recommendations = [self.df.iloc[i[0]].title for i in movie_list]
            return recommendations
        except IndexError:
            return []