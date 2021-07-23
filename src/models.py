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
    username = Column(String(120), unique=True)
    password = Column(String(120), unique=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id_fav = Column(Integer, primary_key=True)
    planet_fav = Column(String(255), nullable=False)
    people_fav = Column(String(255), nullable=False)
    vehicles_fav = Column(String(255), nullable=False)
    iduser = Column(Integer, ForeignKey('user.id'))
    userfavorites =  relationship(User)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    homeworld = Column(Integer, ForeignKey('planet.id'))
    favorites = Column(Integer, ForeignKey('favorites.people_fav'))
    user = relationship(User)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    model = Column(String(120), nullable=False)
    manufacturer = Column(String(120), nullable=False)
    pilots = Column(Integer, ForeignKey('people.id'))
    favorites = Column(Integer, ForeignKey('favorites.vehicles_fav'))
    user = relationship(User)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    people = Column(Integer, ForeignKey('people.id'))
    density = Column(Integer)
    gravity = Column(Integer)
    favorites = Column(Integer, ForeignKey('favorites.planet_fav'))
    user = relationship(User)







    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')