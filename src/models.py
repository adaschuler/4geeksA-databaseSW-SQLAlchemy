import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True)
    password = Column(String(250), unique=True)
    planetssave = Column(Integer, ForeignKey('favorites.planets'))
    peoplesave = Column(Integer, ForeignKey('favorites.people'))
    vehiclesave = Column(Integer, ForeignKey('favorites.vehicles'))

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    planets = Column(Integer, ForeignKey('planets.id')) 
    user = relationship(User)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    owner = Column(Integer, ForeignKey('people.id'))
    user = relationship(User)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    people = Column(Integer, ForeignKey('people.id'))
    density = Column(Integer)
    gravity = Column(Integer)
    user = relationship(User)

class Favorites(Base):
    __tablename__ = 'favorites'
    iduser = Column(Integer, ForeignKey('user.id'))
    planets = Column(String(250), nullable=False)
    people = Column(String(250), nullable=False)
    vehicles = Column(String(250), nullable=False)
    userfavorites =  relationship(User)





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')