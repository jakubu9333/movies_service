#  Basic python api
Movie service is microservice api for movies.

## Installation

Download source code.


### Without docker

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```
Run init.py to create database
```bash
python init.py
```
Run with flask
```bash
flask run```

### Docker
```bash
docker build -t customname .
docker run -p 5000:5000 --name customname customname 
 ```

In both ways application will open on localhost:5000

