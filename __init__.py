from flask import Flask, render_template, request
from uipath.WikiFetcher.start_wikifetcher import start_wikipedia_fetch
from sentence_tools import extract_first_sentence


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        topic = request.form["topic"]
        if topic == '':  # if the user has not given an input
            return render_template("index.html", empty="True")
        else:
            wikipedia_definition = "Wikipedia: " + extract_first_sentence(start_wikipedia_fetch(topic))
            return render_template("index.html", wikipedia=wikipedia_definition)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
