import json
from flask import Flask , request, abort
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(200))
    release_year=db.Column(db.Integer)

    def set_atributes(self,title,description,release_year):
        self.title = title
        self.description = description
        self.release_year = release_year

    def __init__(self,title,description,release_year):
        self.title = title
        self.description = description
        self.release_year = release_year

    def to_json(self):
       return {"id":self.id,"title":self.title,"description":self.description,"release_year":self.release_year}

def seed(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    for item in data:
        db.session.add(Movie(*scrape_body(item)))
    db.session.commit()


def scrape_body(body):
    if (body.get("title",None)==None or  body.get("description",None)==None or body.get("release_year",None)==None):
        abort(400)
    return body["title"],body["description"],body["release_year"]


@app.get("/movies")
def get_movies():
    return list(map(lambda movie: movie.to_json() ,Movie.query.all()))

@app.get("/movies/<int:id>")
def get_one_movie(id):
    return Movie.query.get_or_404(id).to_json()

@app.post("/movies")
def add_movie():
    data = request.get_json()
    movie=Movie(*scrape_body(data))
    db.session.add(movie)
    db.session.commit()
    return movie.to_json()

@app.put("/movies/<int:id>")
def edit_movie(id):
    movie =  request.get_json()
    db_movie = Movie.query.get_or_404(id)
    db_movie.set_atributes(*scrape_body(movie))
    db.session.commit()
    return db_movie.to_json()


if __name__=="__main__":
    app.run(host="0.0.0.0")




