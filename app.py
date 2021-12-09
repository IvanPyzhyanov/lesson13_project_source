from flask import Flask, request, render_template, send_from_directory, json
import os
from pathlib import Path
from functions import read_json, take_tags, looking_tag, add_post

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template("index.html", tags=take_tags())


@app.route("/tag")
def page_tag():
    tag = request.args.get("tag")
    if tag:
        return render_template("post_by_tag.html", posts=looking_tag(tag), tag=tag)



@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    if request.method == "POST":
        text = request.form.get("content")
        pic = request.files.get("picture")
        if text or pic:
            path = f"{UPLOAD_FOLDER}/{pic.filename}"
            pic.save(path)
            post = {"pic": f"/{path}", "content": text}
            add_post(post)
            return render_template("post_uploaded.html", post=post)
    return render_template("post_form.html")



@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run(debug=True)

