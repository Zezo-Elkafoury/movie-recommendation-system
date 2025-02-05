import streamlit as st
from system import RecommendationSystem

# Initialize the recommendation system
def load_recommendation_system():
    return RecommendationSystem('final_dataset.csv')

def main():
    st.title("🎬 Movie Recommendation System")
    st.write("Enter a movie title to get recommendations!")

    # Load the recommendation system
    recommender = load_recommendation_system()

    # User input
    movie_title = st.selectbox("Select a movie:", recommender.df['title'].values)

    # Get recommendations
    if st.button("Recommend"):
        recommendations = recommender.recommend(movie_title)
        if recommendations:
            st.success("Here are the top 5 recommendations:")
            for i, movie in enumerate(recommendations, 1):
                st.write(f"{i}. {movie}")
        else:
            st.error("Movie not found in the dataset. Please try another title.")

# Run the app
if __name__ == "__main__":
    main()