from bottle import route, run, template, static_file


@route("/")
def index():
    return "Hi!"


@route("/static/<filename:path>")
def server_static(filename):
    return static_file(filename, root="static")


def run_local():
    run(host="localhost", port=8080, debug=True, reloader=True)


if __name__ == "__main__":
    run_local()
