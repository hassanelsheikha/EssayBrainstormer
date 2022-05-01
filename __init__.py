from flask import Flask, render_template, request
from uipath.WikiFetcher.start_wikifetcher import get_wikipedia_definition
from sentence_tools import main_get_keywords, get_search_words


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        topic = request.form["topic"]
        if topic == '':  # if the user has not given an input
            return render_template("index.html", empty="True")
        else:
            wikipedia_definition = get_wikipedia_definition(topic)
            if wikipedia_definition is None:  # if the term is undefined
                wikipedia_definition = 'Wikipedia does not have a definition for this phrase.'
            return render_template("index.html", wikipedia=wikipedia_definition)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
