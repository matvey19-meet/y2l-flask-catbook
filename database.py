from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_cat(name):
    cat_object = Cat(name=name)
    session.add(cat_object)
    session.commit()

def get_all_cats():
    cats = session.query(Cat).all()
    return cats

def get_cat(cat_id):
    cat= session.query(Cat).filter_by(id=cat_id).one()
    return cat
def search(name):
    cat=session.query(Cat).filter_by(name=name).first()
    return cat
def addVote(cat_id):
    cat= session.query(Cat).filter_by(id=cat_id).one()
    cat.votes=cat.votes+1