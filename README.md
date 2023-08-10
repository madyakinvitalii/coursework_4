Project Overview
Authentication

To allow each user the capability to add their favorite movies to bookmarks for later viewing, we will implement registration and authentication pages based on the well-known JWT specification. This will help us differentiate users and manage their access.

User Profiles

Each user will have a profile page where they can select their favorite movie genre, provide their first and last name, and change their password if needed. Additionally, users will have the ability to add and remove movies from their bookmarks, as well as view all saved bookmarked movies.

Movies, Directors, Genres

Of course, the core entities are movies, directors, and genres. We'll focus on implementing read-only functionality (get requests) for these entities. Pagination will be applied to all objects, allowing us to display them on the screen page by page. Moreover, users will be able to explore the latest movies.

This project aims to capture the essence of a platform similar to Kinopoisk, focusing on movie-related content.

- Install dependencies
```shell
pip install -r requirements.txt

pip install -r requirements.dev.txt
```

- Creation of models (will clear the database and create all the models specified in the import)
```shell
python create_tables.py
```

- Loading data into the database
```shell
python load_fixture.py
```
The script reads the fixtures.json file and loads the data into the database. If the data has already been loaded, it displays an appropriate message.

## Launch of the project

### Bash (Linux/MACOS)
```shell
export FLASK_APP=run.py
export FLASK_ENV='development'
flash run
```

###CMD (Windows)
```shell
set FLASK_APP=run.py
set FLASK_ENV=development
flash run
```

### PowerShell (Windows)
```shell
$env:FLASK_APP = "run"
$env:FLASK_ENV = "development"
flash run
```

## Run tests
```shell
pytest.
```
