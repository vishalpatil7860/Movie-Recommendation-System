# Movie Recommendation System

This project implements a content-based movie recommendation system using movie metadata from TMDB. The system uses the cosine similarity between movies based on various features like genres, keywords, cast, and crew to recommend similar movies.

## Steps

1. **Import Libraries**
    - Import necessary libraries like `numpy`, `pandas`, `os`, `ast`, `CountVectorizer`, `cosine_similarity`, and `pickle`.

2. **List Input Files**
    - List all files available in the input directory to ensure the datasets are loaded correctly.

3. **Read Datasets**
    - Read the `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` files into pandas dataframes.

4. **Explore Data**
    - Display the first few rows and shape of the datasets to understand their structure.

5. **Merge Datasets**
    - Merge the movies and credits dataframes on the 'title' column to create a single dataframe containing all necessary information.

6. **Select Relevant Columns**
    - Select columns relevant for the recommendation system: 'movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', and 'crew'.

7. **Data Preprocessing**
    - Convert JSON formatted columns ('genres', 'keywords', 'cast', 'crew') to lists using a custom function.
    - Drop rows with missing values.
    - Limit the 'cast' column to the top 3 actors.
    - Extract the director's name from the 'crew' column.
    - Remove spaces from elements in the lists to create unified tags.

8. **Create Tags**
    - Combine 'overview', 'genres', 'keywords', 'cast', and 'crew' columns into a single 'tags' column.

9. **Vectorize Tags**
    - Use `CountVectorizer` to convert the 'tags' column into a matrix of token counts.
    - Compute the cosine similarity matrix for the tags.

10. **Recommendation Function**
    - Define a function to recommend movies based on the cosine similarity of the tags.
    - Test the function with a sample movie.

11. **Save Model**
    - Save the processed data and similarity matrix using `pickle` for future use.

## Usage

1. **Run the Code**
    - Execute the code in a Python environment to process the data and create the recommendation system.

2. **Get Recommendations**
    - Use the `recommend(movie)` function to get movie recommendations. Replace `movie` with the title of the movie you want recommendations for.

3. **Load Saved Model**
    - Load the saved model and data using `pickle` to reuse the recommendation system without reprocessing the data.

## Example

To get recommendations for the movie "Gandhi":

```python
recommend('Gandhi')
```
This will output a list of movies similar to "Gandhi".

Dependencies
- numpy
- pandas
- scikit-learn
- ast
- pickle
