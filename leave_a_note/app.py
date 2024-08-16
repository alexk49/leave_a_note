import os
import logging
import sqlite3

from bottle import route, run, template, static_file, TEMPLATE_PATH, default_app

logging.basicConfig(level=logging.INFO, format=" %(asctime)s -  %(levelname)s -  %(message)s")

abs_app_dir_path = os.path.dirname(os.path.realpath(__file__))
abs_views_path = os.path.join(abs_app_dir_path, "views")
TEMPLATE_PATH.insert(0, abs_views_path)

app = default_app()

DB_DIR_PATH = os.path.join(abs_app_dir_path, "data")
DB_PATH = os.path.join(abs_app_dir_path, "data", "notes.db")


@route("/")
def index():
    return template("index")


@route("/static/<filename:path>")
def server_static(filename: str):
    """
    Required to load all static files
    Absolute dir path is used to handle app
    being loaded from project root
    """
    return static_file(filename, root=os.path.join(abs_app_dir_path, "static"))


def check_database_exists(db_dir_path: str, db_path: str):
    """Check database and folder exists
    and make folder and database if not"""
    if os.path.exists(db_dir_path) is False:
        logging.info("%s does not exist", db_path)
        os.mkdir(db_dir_path)
        create_new_database(db_path)


def create_new_database(db_path: str):
    """Create new database file with standard rows."""
    logging.info("creating new database: %s", db_path)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE notes(id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, note TEXT NOT NULL)"
    )
    connection.commit()
    connection.close()


def main():
    # ensure templates path is still findable when app is run from project root
    app.run(host="localhost", port=8080, debug=True, reloader=True)

    check_database_exists(DB_DIR_PATH, DB_PATH)


if __name__ == "__main__":
    main()
