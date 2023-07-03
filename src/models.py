import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    url_image = Column(String(250), nullable=False)

class PlanetUserFav(Base):
    __tablename__ = 'planetUserFav'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    url_image = Column(String(250), nullable=False)

class CharacterUserFav(Base):
    __tablename__ = 'characterUserFav'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    url_image = Column(String(250), nullable=False)

class VehicleUserFav(Base):
    __tablename__ = 'vehicleUserFav'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(Vehicle)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
