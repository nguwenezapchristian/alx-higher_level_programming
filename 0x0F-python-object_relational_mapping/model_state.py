#!/usr/bin/python3
"""
Module which creates a table
in mysql
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base
my_metadata = MetaData()
Base = declarative_base(metadata=my_metadata)


class State(Base):
    """
    class State which creat the table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
