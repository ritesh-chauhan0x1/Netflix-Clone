from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Dummy movie data
movies = [
    {"id": 1, "title": "Stranger Things", "image": "/static/stranger_things.jpg", "desc": "A thrilling Netflix original series."},
    {"id": 2, "title": "Money Heist", "image": "/static/money_heist.jpg", "desc": "A Spanish heist crime drama television series."},
    {"id": 3, "title": "The Witcher", "image": "/static/witcher.jpg", "desc": "A fantasy drama series based on the book series."}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/movies')
def get_movies():
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True)
