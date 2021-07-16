import shutil
from flask import Flask

shutil.make_archive("static/py", 'zip', "static/py")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run(debug=True)