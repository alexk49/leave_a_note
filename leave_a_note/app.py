import os

from bottle import route, run, template, static_file, TEMPLATE_PATH, default_app


abs_app_dir_path = os.path.dirname(os.path.realpath(__file__))
abs_views_path = os.path.join(abs_app_dir_path, "views")
TEMPLATE_PATH.insert(0, abs_views_path)

app = default_app()


@route("/")
def index():
    return template("index")


@route("/static/<filename:path>")
def server_static(filename):
    return static_file(filename, root=os.path.join(abs_app_dir_path, "static"))


def main():
    # ensure templates path is still findable when app is run from project root
    app.run(host="localhost", port=8080, debug=True, reloader=True)


if __name__ == "__main__":
    main()
