import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Podcast, Episode

DATABASE_URL = "sqlite:///podcasts.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    Base.metadata.create_all(engine)
    print("Database Initialized.")

def create_podcast():
    podcast_name = input("Enter Podcast name: ") 
    description = input("Enter podcast description: ")
    author = input ("Enter author's name: ")
    podcast = Podcast(podcast_name=podcast_name, description=description, author=author)
    session.add(podcast)
    session.commit()
    print(f"Podcast {podcast_name} created successfully!")
    print(f"ID: {podcast.id} Description: {description  or "No description provided"}")
    print(f"Author: {author} Created At: {podcast.creation_time}")   

    
