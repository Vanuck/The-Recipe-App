# The Recipe App
- Python & Django Recipe App

## Preview

![Screenshot] (media/loginpage.jpg)

<h2>Overview</h2>
<p>
This project is a web application using the Django framework with Python. Django has the advantage of being neatly moduralized and developer friendly, while also being powerful. It is used to run some of the world’s most popular websites today. In this project, working with Python-based Django, a full-stack web application using the Django development server will be developed. t is a fully-fledged application equipped with an admin panel that enables CRUD (Create, Read, Update, Delete) operations on the database. The app provides functionality for user registration, allowing users to create and manage their own content.The main focus of this project will be the backend.
</p>

<br>

## Key Features
* Implement user authentication, login, and logout functionality.
* Enable users to search for recipes by ingredients.
* Automatically assign a difficulty rating to each recipe.
* Handle user input and errors effectively.
* Provide additional details on recipes upon user request.
* Store user-submitted recipes in a database.
* Include a Django Admin dashboard for managing database entries.
* Display statistics and visualizations based on data trends and analysis.

## Tech Used
* Django (5.0.7)
* Pillow (10.4.0)
* Black (formatting: 24.4.2)
* Pandas (2.2.2)
* matplotlib (3.9.1)

## Requirements
- Compatibility: Works on Python 3.6+ installations and Django version 3.
- Error Handling: Manages exceptions and errors during user input, displaying user-friendly error messages.
- Database: Connects to a PostgreSQL database hosted locally (uses SQLite during development).
- User Interface: Provides an easy-to-use interface with simple input forms and clear instructions. Menus for features like login and logout are presented neatly with concise prompts.
- Code Quality: Includes proper documentation and automated tests. Code is uploaded on GitHub.
- Dependencies: A requirements.txt file is provided, listing all necessary modules.
- Instructions: A README file with instructions for downloading and running the app locally is included.

## Setup and Installation

1. **Clone the repository:**

```bash
git clone [repository URL]
cd recipe-app
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Setup Database:**

- Adjust the `DATABASES` configuration in `settings.py` for PostgreSQL and SQLite as per your development and production environments.

4. **Run Migrations:**

```bash
python manage.py migrate
```

5. **Create Superuser for Admin Access:**

```bash
python manage.py createsuperuser
```

6. **Run the Development Server:**

```bash
python manage.py runserver
```

- Visit `http://127.0.0.1:8000` in your browser to view the app.

## Contribution
Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.

# Contributors
- [Andrew Jornitz](https://github.com/Vanuck)


  