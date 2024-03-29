#!/usr/bin/env python3

# This file was provided by Udacity
import sys
import time
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# declare mapper
Base = declarative_base()


# restaurant table
class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    # JSON export
    @property
    def serialize(self):

        return {
           'name': self.name,
           'description': self.description,
           'id': self.id,
           'price': self.price,
           'course': self.course,
        }


# connect to psql db, avoid duplicate error with checkfirst
engine = create_engine('postgresql:///catalog')
Base.metadata.create_all(engine, checkfirst=True)
