from pydantic import BaseModel

class Person(BaseModel):
    """
    id, name, description, age
    """
    id:int
    name:str
    description:str
    age:int
