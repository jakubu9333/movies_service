from flask import Flask , request, jsonify
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




def scrape_body(body):
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
    with app.app_context():
        db.create_all()
    app.run()




