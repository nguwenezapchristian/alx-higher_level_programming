#!/usr/bin/python3
"""
Module which creates a table
in mysql
"""
from sqlalchemy import Column, integer, String, MetaData
from sqlalchemy.orm import Declarative_base
my_metadata = MetaData()
Base = Declarative_base(metadata=my_metadata)


class State(Base):
    """
    class State which creat the table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
