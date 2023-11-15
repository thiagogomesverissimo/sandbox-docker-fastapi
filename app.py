from fastapi import FastAPI

from models.person import Person 

app = FastAPI()

@app.get('/')
def index():
    return {'api': 'my api'}

@app.get('/color-check/{color}')
def get_color(color:str):
    if color != 'pink':
        return {'message': 'You are not correct'}
    return {'message': 'You are correct'}

@app.get('/persons')
def persons():
    persons = [
        Person(id=1,name='Maria',description='a girl',age=20),
        Person(id=2,name='Jaun',description='a boy',age=18),
    ]
    return persons
