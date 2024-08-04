---

# ToDo List for Linux Learning

## Project Overview

The **ToDo List** application is a simple web app built using Flask and Python. It allows you to manage tasks by adding, editing, and deleting items from a list. This project serves as a practical introduction to web development with Flask.

## Features

- **Add New Tasks**: Easily add tasks to your ToDo list.
- **Edit Existing Tasks**: Modify tasks that you've already added.
- **Delete Tasks**: Remove tasks from your list when they are completed.
- **View All Tasks**: See all your tasks on the main page.

## Project Structure

The project is organized as follows:

```
todo_list/
│
├── app/
│   ├── __init__.py             # Initializes the Flask app
│   ├── forms.py                # Defines form classes for adding/editing tasks
│   ├── models.py               # Database models (e.g., Task)
│   ├── routes.py               # Application routes and logic
│   ├── static/                 # Static files (CSS, JavaScript, images)
│   │   ├── css/
│   │   │   └── style.css       # Stylesheet
│   │   ├── images/             # Static images
│   │   └── js/                 # JavaScript files (if any)
│   └── templates/              # HTML templates
│       ├── base.html           # Base template for common layout
│       ├── index.html          # Main page template
│       ├── add_task.html       # Template for adding tasks
│       └── edit_task.html      # Template for editing tasks
│
├── migrations/                 # Database migration files
├── .env                        # Environment variables
├── config.py                   # Configuration settings
├── requirements.txt            # Required Python packages
└── run.py                      # Main entry point for running the app
```

### Explanation

- **`app/`**: Contains the main components of the application, including routes, models, forms, static files, and templates.
- **`migrations/`**: Stores database migration history.
- **`.env`**: Optional file for environment variables.
- **`config.py`**: Configures application settings, such as database URI.
- **`requirements.txt`**: Lists all dependencies needed to run the application.
- **`run.py`**: Starts the Flask application.

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/todo_list.git
   cd todo_list
   ```

2. **Create a Virtual Environment**:

   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**:

   ```bash
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

4. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up the Database**:

   ```bash
   flask db init       # Initialize migration repository
   flask db migrate -m "Initial migration"  # Create migration script
   flask db upgrade    # Apply migration
   ```

6. **Run the Application**:

   ```bash
   export FLASK_APP=run.py
   export FLASK_ENV=development  # For development mode
   flask run
   #or
   flask run --host=0.0.0.0 --port=5000
   ```

   Access the app at [http://127.0.0.1:5000](http://127.0.0.1:5000) or your server ip [http://serverIP:5000](http://serverIP:5000)

## Usage

- **Open the Application**: Go to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.
- **Add Tasks**: Use the "Add Task" page to add new items.
- **Edit Tasks**: Click on a task to modify it.
- **Delete Tasks**: Remove completed tasks from the list.

## Contributing

1. **Fork the repository** on GitHub.
2. **Create a new branch** for your feature or bug fix.
3. **Make your changes** and commit them.
4. **Push your changes** to your fork.
5. **Create a pull request** to merge them into the main repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- **Flask**: Web framework for Python.
- **Flask-SQLAlchemy**: Adds SQLAlchemy support to Flask.
- **Flask-Migrate**: Handles database migrations for Flask apps.
- **Flask-WTF**: Simplifies form handling in Flask.

## Contact

For questions or issues, please reach out to [Linkedin](https://www.linkedin.com/in/ajeet-g-456333194/).

---

### `.gitignore`

To ensure that unnecessary files are not tracked by Git, create a `.gitignore` file in the root of your project directory with the following contents:

```plaintext
# Virtual environment
venv/
*.pyc
*.pyo
*.pyd
__pycache__/

# Database
*.sqlite3
*.db

# IDE/editor directories
.vscode/
.idea/

# Operating system files
.DS_Store
Thumbs.db

# Environment variables
.env

# Flask migrations
migrations/

# Logs
*.log

# Misc
*.swp
```

This `.gitignore` file will exclude virtual environment directories, bytecode files, database files, IDE configurations, system files, environment variables, migration files, and other unnecessary files from being tracked in your Git repository.

Feel free to modify the `README.md` and `.gitignore` files as needed for your specific project. Let me know if there's anything else you'd like to add!

