from flask import Flask, render_template, request, flash, send_file, \
    send_from_directory, abort
import subprocess
from uipath.WikipediaFetcher import start_fetch
import os
import selenium

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    topic = request.form["topic"]
    if request.method == "POST":
        if topic == '':  # if the user has not given an input
            return render_template("index.html", empty="True")
        else:
            start_fetch.start_wikipedia_fetch(topic)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
