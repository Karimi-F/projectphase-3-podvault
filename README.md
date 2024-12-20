# PodVault - Podcast Episode Manager

PodVault is a command-line interface (CLI) application that allows users to manage podcasts and episodes. The application uses SQLAlchemy for Object-Relational Mapping (ORM) with a SQLite database to store podcast and episode data. The project supports time zone management using `pytz` to handle East Africa Time (EAT) as the default time zone for the podcast's creation time.

## Features

- **Create Podcasts**: Users can create podcasts by providing the podcast name, description, and author.
- **Create Episodes**: Users can create podcast episodes by providing episode title, description, and audio URL.
- **View Podcasts**: Users can view all podcasts with detailed information, including the number of episodes and creation time.
- **View Episodes**: Users can view all episodes associated with a podcast.
- **Timezone Support**: All timestamps are localized to East Africa Time (EAT) using `pytz`.

## Requirements

- Python 3.x
- SQLAlchemy
- pytz
- datetime

### Install Dependencies

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```


This will install both SQLAlchemy and pytz.

### Installation
## Clone the Repository: 
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/podvault.git
cd podvault
```

## Set up the Database: 
Make sure you have SQLite installed, or use any other database supported by SQLAlchemy by adjusting the DATABASE_URL in your config.py.

Run the Application: After setting up, you can run the CLI application:


Project Structure
The project follows a modular structure:

.
├── Pipfile
├── Pipfile.lock
├── README.md
├── cli.py                    # Main CLI file
├── models.py                 # Contains Podcast and Episode models
├── podcast.db                # Contains the database created tables
├── alembic.ini               # Contains the sqlLite url
├── migrations                # Contains the versions and the env.py
│                   
    


- models/podcast.py: Contains the Podcast and Episode classes, which define the database schema.
- cli.py: The command-line interface that allows users to interact with the application, create podcasts, episodes, and view them.
- helpers.py: Contains helper functions for database operations like adding, deleting, and querying podcasts and episodes.
- database.py: Manages the database session and setup.
- config.py: Contains configuration settings such as the database URL.

Example Usage
Create a Podcast:

Enter Podcast name: My Awesome Podcast
Enter podcast description: A podcast about tech and innovation.
Enter author's name: John Doe
Podcast My Awesome Podcast created successfully!
ID: 1 Description: A podcast about tech and innovation. 
Author: John Doe Created At: 2024-12-19 12:30:45+00:00

Create an Episode:

Enter Episode Title: Episode 1 - Introduction
Enter Episode Description: Introduction to the podcast series.
Enter Audio URL: https://example.com/audio/episode1.mp3
Episode "Episode 1 - Introduction" created successfully!
ID: 1 Description: Introduction to the podcast series. 
Audio URL: https://example.com/audio/episode1.mp3
Release Date: 2024-12-19 12:30:45+00:00

### View Podcasts:

Podcasts:
1. My Awesome Podcast
   - Author: John Doe
   - Description: A podcast about tech and innovation.
   - Created At: 2024-12-19 12:30:45+00:00


## Time Zone
All timestamps are set to East Africa Time (EAT) by default. You can modify this by changing the timezone settings in the config.py file or by localizing to any other timezone supported by pytz.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you'd like to contribute to this project.

## Acknowledgements
SQLAlchemy for ORM-based database management.
pytz for time zone handling.
SQLite as the default database engine.

Happy coding and enjoy managing your podcasts with PodVault!