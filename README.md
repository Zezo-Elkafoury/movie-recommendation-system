# Movie Recommendation System

This project is a simple movie recommendation system that suggests movies based on the similarity of their genres and overviews. The system uses the **TF-IDF Vectorizer** to convert text data into numerical vectors and then calculates the cosine similarity between these vectors to find the most similar movies.

## Dataset

The dataset used in this project contains information about 10,000 movies, including their titles, genres, overviews, popularity, release dates, and more. The dataset is stored in a CSV file named `dataset.csv`.

### Dataset Columns:
- **id**: Unique identifier for each movie.
- **title**: Title of the movie.
- **genre**: Genres associated with the movie.
- **original_language**: Original language of the movie.
- **overview**: Brief description of the movie's plot.
- **popularity**: Popularity score of the movie.
- **release_date**: Release date of the movie.
- **vote_average**: Average rating of the movie.
- **vote_count**: Number of votes the movie received.

## Data Preprocessing

1. **Handling Missing Values**: 
   - The dataset had missing values in the `genre` and `overview` columns. These rows were dropped to ensure data quality.

2. **Creating Tags**:
   - A new column `tags` was created by concatenating the `genre` and `overview` columns. This combined text is used to generate recommendations.

3. **Text Vectorization**:
   - The `tags` column was vectorized using **TF-IDF Vectorizer**, which converts the text data into a matrix of TF-IDF features.

4. **Cosine Similarity**:
   - The cosine similarity between the vectors was calculated to determine how similar the movies are to each other.

## Recommendation Function

The `recommend(movie)` function takes a movie title as input and returns the top 5 most similar movies based on the cosine similarity score.

### Example:
```python
recommend('Interstellar')
```
### Output
```python
Space Pirate Captain Harlock
Prometheus
Star Wars: The Last Jedi
A Trip to the Moon
The Matrix
```
