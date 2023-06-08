#  Basic python api
Basic python api is microservice api for posts.

## Installation

Download source code.


### Without docker

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```
Run init.py to create and seed database 
```bash
python init.py
```
Run app.py
```bash
python app.py
```

### Docker
```bash
docker build -t customname .
docker run -p 5000:5000 --name customname customname 
 ```

In both ways application will open on localhost:5000. Use [curl](https://curl.se/) or [Insomnia](https://insomnia.rest/) to control app.

## Api Endpoints

### List all Movies 
GET /movies \
Endpoint for listing all movies.
### List one Movie 
GET /movies/{id}\
Endpoint for listing movies with id as {id}.
### Update Movie
PUT /movies/{id} \
Endpoint for updating movie with id as {id} from body request.
### Create Movie 
POST /movies \
Endpoint for creating movie from body of request.

