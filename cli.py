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
    podcast" = Podcast(podcast_name=podcast_name, description=description, author=author)
    session.add(podcast)
    session.commit()
    print(f"Podcast {podcast_name} created successfully!")
    print(f"ID: {podcast.id} Description: {description  or "No description provided"}")
    print(f"Author: {author} Created At: {podcast.creation_time}")   

def update_podcast():
    podcast_id = int(input("Enter Podcast ID to update: "))
    podcast = session.get(Podcast, podcast_id)    
    if not podcast:
        print(f"Podcast with ID{podcast_id} does not exist.")
        return
    podcast.podcast_name = input(f"Enter new podcast name (current:{podcast.podcast_name}): ") or podcast.podcast_name
    podcast.description = input(f"Enter new podcast description (current:{podcast.description}): ") or podcast.description
    podcast.author = input(f"Enter new podcast author (current:{podcast.author}): ") or podcast.author
    session.commit()
    print(f"Podcast ID {podcast_id} updated successfully!")

def delete_podcast():
    podcast_id = int(input("Enter Podcast ID to delete: "))
    podcast = session.get(Podcast, podcast_id)
    if not podcast:
        print(f"Podcast with ID {podcast_id} does not exist.")
        return
    session.delete(podcast)
    session.commit()
    print(f"Podcast ID {podcast_id} deleted successfully!")

    
