#!/usr/bin/python3
"""
Module Name: model_city.py
Description: This module contains a definition of class `City`
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """A definition of `City` class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    states = relationship('State', back_populates='cities')


State.cities = relationship('City', back_populates='states')
