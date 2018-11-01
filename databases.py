from model import Base, Animal

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_animal(name, age, siblings, male, female):
  #TODO: complete the functions (you will need to change the function's inputs)
    animal_object = Animal(
        name=name,
        age=age,
        siblings=siblings,
        male=male,
        female=female)

    session.add(animal_object)
    session.commit()


create_animal("cat", 6, 2, False,True)
create_animal("dog", 4, 5, True,False)

def update_animal():
  #TODO: complete the functions (you will need to change the function's inputs)
  pass

def delete_animal(id):
   session.query(Animal).filter_by(
       name=their_name).delete()
   session.commit()
   delete_animal("cat")

def get_animal(id):
  pass
