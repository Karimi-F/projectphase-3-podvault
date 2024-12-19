#define our tables using OOP + sqlalchemy
from sqlalchemy import Column, Text, Integer, String, ForeignKey, VARCHAR
from sqlalchemy.orm import declarative_base

#create a base model that all our models are going to inherit from 
Base = declarative_base()

#define our first model
# 1. It's a must we provide the table name via the attribute __tablename__
# 2. It's a must we provide at least one table column.
class Episode(Base):
    __tablename__ = "episodes"

    #define columns
    id = Column(Integer(), primary_key = True)
    podcast_name = Column(String(), nullable=False)
    episode_title = Column(String(), nullable=False)
    email = Column(VARCHAR(), nullable=False, unique=True)