from flask import Flask, render_template, request, flash, send_file, \
    send_from_directory, abort
import subprocess
import os
import selenium

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        if request.form["topic"] == '':  # if the user has not given an input
            return render_template("index.html", empty="True")
        else:
            subprocess.run('wikipedia_fetcher.bat')
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
