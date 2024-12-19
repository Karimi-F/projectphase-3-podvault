#define our tables using OOP + sqlalchemy
from sqlalchemy import create_engine, Column, Text, Integer, String, ForeignKey, VARCHAR, DateTime
#   from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
import pytz

eat = pytz.timezone("Africa/Nairobi")
# from zoneinfo import ZoneInfo

#create a base model that all our models are going to inherit from 
Base = declarative_base()

#define our first model
# 1. It's a must we provide the table name via the attribute __tablename__
# 2. It's a must we provide at least one table column.
class Podcast(Base):
    __tablename__ = "podcasts"

    #define columns
    id = Column(Integer, primary_key = True)
    podcast_name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    author = Column(String, nullable=False)
    creation_time = Column(DateTime, default=lambda: datetime.now(eat), nullable=False)

    episodes = relationship("Episode", back_populates="podcast")

    def __repr__(self):
        return (
            f"Podcast(id:{self.id}, Podcast Name:{self.podcast_name}, Description: {self.description}, Author: {self.author}, Creation Time: {self.creation_time})" 
        )


class Episode(Base):
    __tablename__= "episodes"

    id = Column(Integer, primary_key=True)
    episode_title = Column(String, nullable=False)
    description = Column(String, nullable = True)
    audio_url = Column(String, nullable=False)
    release_date = Column(DateTime, default=lambda: datetime.now(eat), nullable=False)
    podcast_id = Column(Integer, ForeignKey("podcasts.id"), nullable=False)
    update_time = Column(DateTime, default=lambda: datetime.now(eat), nullable=False)

    podcast = relationship("Podcast", back_populates="episodes")

    def __repr__(self):
        return(
            f"Episode(id : {self.id}, Episode Title : {self.episode_title}, Description : {self.description}, "
            f"Audio Url : {self.audio_url}, Release Date : {self.release_date}, Podcast ID : {self.podcast_id}, "
            f"Updated Time : {self.update_time})"
        )

