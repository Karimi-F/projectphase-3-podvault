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
    print(f"ID: {podcast.id} Description: {description}")
    # print(f"Author: {author}")   
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



def create_episode():
    episode_title = input("Enter Episode title: ") 
    description = input("Enter episode description: ")
    audio_url = input ("Enter audio url: ")
    podcast_id = int(input("Enter Podcast ID:"))
    podcast = session.get(Podcast, podcast_id)
    if not podcast:
        print(f"Podcast with ID {podcast_id} does not exist")
        return
    episode = Episode(episode_title=episode_title, description=description, audio_url=audio_url, podcast_id=podcast_id)
    session.add(episode)
    session.commit()
    print(f"Episode {episode_title} created successfully!")
    print(f"Podcast ID:{podcast_id} Episode ID: {episode.id} Description: {description}")
    # print(f"Audio URL: {audio_url}")   
    print(f"Audio URL: {audio_url} Created At: {episode.release_date}")   

def update_episode():
    episode_id = int(input("Enter Episode ID to update: "))
    episode = session.get(Episode, episode_id)    
    if not episode:
        print(f"Episode with ID{episode_id} does not exist.")
        return
    episode.episode_title = input(f"Enter new episode title (current:{episode.episode_title}): ") or episode.episode_title
    episode.description = input(f"Enter new episode description (current:{episode.description}): ") or episode.description
    episode.audio_url = input(f"Enter new audio url (current:{episode.audio_url}): ") or episode.audio_url
    new_podcast_id = input (f"Enter new Podcast ID for Episode (current: {episode.podcast_id})") or episode.podcast_id
    if new_podcast_id:
        new_podcast = session.get(Podcast, int(new_podcast_id))
        if not new_podcast:
            print(f"Podcast with ID {new_podcast_id} does not exist.")
        else:
            episode.podcast_id = new_podcast_id
    session.commit()
    print(f"Episode ID {episode_id} updated successfully!")

def delete_episode():
    episode_id = int(input("Enter Episode ID to delete: "))
    episode = session.get(Episode, episode_id)
    if not episode:
        print(f"Episode with ID {episode_id} does not exist.")
        return
    session.delete(episode)
    session.commit()
    print(f"Episode ID {episode_id} deleted successfully!")

def assign_episode():
    episode_id = int(input("Enter Episode ID:"))
    podcast_id = int(input("Enter the Podcast ID:"))  
    episode = session.get(Episode, episode_id)
    podcast = session.get(Podcast, podcast_id)

    if not episode or not podcast:
        print("Invalid Episode ID or Podcast ID!")
        return  
    episode.podcast_id = podcast_id
    session.commit()
    print("Episode added to Podcast successsfully!")

def list_podcasts():
    podcasts = session.query(Podcast).all()
    if not podcasts:
        print("No Podcasts found.")
        return
    for podcast in podcasts:
        print(podcast)

def list_episodes():
    episodes = session.query(Episode).all()
    if not episodes:
        print("No Episodes found.")
        return
    for episode in episodes:
        print(episode)

def episodes_by_podcast():
    podcast_id = int(input("Enter Podcast ID to view the episodes: "))
    podcast = session.get(Podcast, podcast_id)
    if not podcast:
        print(f"Podcast with ID {podcast_id} does not exist.")
        return
    episodes = podcast.episodes
    if not episodes:
        print(f"No episodes found for podcast with ID {podcast_id}")
        return
    print(f"Episodes for podcast {podcast.podcast_name} with (ID {podcast_id}):")
    for episode in episodes:
        print(episode)
            


def main_menu():
    while True:
        print("\n Welcome to PodVault. What would you like to do today?")
        print("1. Create Podcast.")
        print("2. Update Podcast.")
        print("3. Delete Podcast.")
        print("4. Create Episode.")
        print("5. Update Episode.")
        print("6. Delete Episode.")
        print("7. Assign Episode to Podcast.")
        print("8. List Podcasts.")
        print("9. List Episodes.")
        print("10. View Episodes per Podcast.")
        print("11. Exit")
        choice = input("Enter your choice:")

        if choice == "1":
            create_podcast()
        elif choice == "2":
            update_podcast()    
        elif choice == "3":
            delete_podcast()    
        elif choice == "4":
            create_episode()    
        elif choice == "5":
            update_episode()    
        elif choice == "6":
            delete_episode()    
        elif choice == "7":
            assign_episode()    
        elif choice == "8":
            list_podcasts()    
        elif choice == "9":
            list_episodes()    
        elif choice == "10":
            episodes_by_podcast()    
        elif choice == "11":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.") 


if __name__ == "__main__":
    init_db()
    main_menu()      

        