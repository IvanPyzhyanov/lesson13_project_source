from flask import Flask, request, render_template, send_from_directory, json
import os
from pathlib import Path
from functions import read_json, take_tags

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template("index.html", tags=take_tags())



@app.route("/tag")
def page_tag():
    pass


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run()

