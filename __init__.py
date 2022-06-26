from flask import Flask, render_template, request
from uipath.WikiFetcher.start_wikifetcher import get_wikipedia_definition


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        topic = request.form["topic"]
        if topic == '':  # if the user has not given an input
            return render_template("index.html", empty="True", site="")
        else:
            t = get_wikipedia_definition(topic)
            url = f'https://en.wikipedia.org/wiki/{topic}'
            if t is None:  # if the term is undefined
                wikipedia_definition = 'Wikipedia does not have a definition for this phrase.' \
                                       ' If your phrase is broad (there is one name corresponding to equally ranked people), please be more specific.'
                url = ""
                news = ""
            else:
                wikipedia_definition = t[0]
                news = t[1]

            return render_template("index.html", wikipedia=wikipedia_definition, site=url, news=news)
    else:
        return render_template("index.html", site='')


if __name__ == "__main__":
    app.run(debug=True)
