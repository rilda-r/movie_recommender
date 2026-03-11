A simple Flask web application that recommends movies based on similarity scores, user ratings, and popularity.
Users can select a movie from a dropdown or type with autocomplete, and get personalized movie recommendations.

## Features
Movie recommendations based on cosine similarity of features.
Considers ratings and popularity to calculate a final score.
Dropdown and autocomplete search bar for easy selection of movies.
Displays top 5 recommended movies.

## SET UP
1) clone repo
   -Ensure the models folder contains cosine_sim.pkl, movies.pkl, and indices.pkl.
3) create virtual envi
   `python -m venv venv`
5) activate virtual envi
   `venv\Scripts\activate`
6) install dependencies
   `pip install -r requirements.txt`
7) run flask app
   `cd app`
  `python app.py`
8) open in browser

## future improvements
Implement user ratings to further personalize recommendations.
