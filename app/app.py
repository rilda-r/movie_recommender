from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load models
cosine_sim = pickle.load(open('../models/cosine_sim.pkl', 'rb'))
movies = pickle.load(open('../models/movies.pkl', 'rb'))
indices = pickle.load(open('../models/indices.pkl', 'rb'))

# List of all movie titles for dropdown / autocomplete
all_movies = movies['title'].tolist()

def recommend(title, num_recommendations=5):
    if title not in indices:
        return ["Movie not found"]

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))

    import pandas as pd
    sim_df = pd.DataFrame(sim_scores, columns=['movie_index', 'similarity'])

    sim_df = sim_df.merge(
        movies[['rating_norm', 'count_norm']],
        left_on='movie_index',
        right_index=True
    )

    sim_df['final_score'] = (
        0.6 * sim_df['similarity'] +
        0.2 * sim_df['rating_norm'] +
        0.2 * sim_df['count_norm']
    )

    sim_df = sim_df.sort_values(by='final_score', ascending=False)
    sim_df = sim_df.iloc[1:num_recommendations+1]

    return movies['title'].iloc[sim_df['movie_index']].tolist()

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    selected_movie = None
    if request.method == 'POST':
        selected_movie = request.form['movie']
        recommendations = recommend(selected_movie)

    return render_template(
        'index.html',
        recommendations=recommendations,
        all_movies=all_movies,
        selected_movie=selected_movie
    )

if __name__ == '__main__':
    app.run(debug=True)
