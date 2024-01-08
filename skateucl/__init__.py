import os
import json

from flask import Flask, render_template
from flask_assets import Environment, Bundle


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "skateucl.sqlite"),
    )
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    assets = Environment(app)
    js = Bundle("js/committee profile viewer.js", filters="rjsmin", output="gen/packed.js")
    css = Bundle("css/style.css", "css/home.css", filters="rcssmin", output="gen/packed.css")
    assets.register("js_all", js)
    assets.register("css_all", css)

    committee_member_profiles = get_committee_profiles(app)

    @app.route("/")
    def index():
        return render_template("index.j2", committee_profiles=committee_member_profiles)

    return app


def get_committee_profiles(app):
    path = os.path.join(app.static_folder, "json/committee.json")
    return tuple({"name": obj["Name"], "data": json.dumps(obj)} for obj in json.load(open(path)))
