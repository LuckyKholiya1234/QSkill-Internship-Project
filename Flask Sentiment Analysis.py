from flask import Flask, request, render_template_string
from textblob import TextBlob

app = Flask(__name__)


# HTML page
html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Sentiment Analysis</title>

    <style>
        body {
            font-family: Arial;
            background-color: #f2f2f2;
            text-align: center;
            padding: 50px;
        }

        .container {
            background-color: white;
            width: 500px;
            margin: auto;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px gray;
        }

        h1 {
            color: #333;
        }

        textarea {
            width: 90%;
            height: 120px;
            padding: 10px;
            font-size: 16px;
            margin-bottom: 15px;
        }

        button {
            background-color: #333;
            color: white;
            padding: 10px 25px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background-color: #555;
        }

        .result {
            margin-top: 25px;
            padding: 15px;
            background-color: #eeeeee;
            border-radius: 5px;
        }
    </style>
</head>

<body>

    <div class="container">

        <h1>Sentiment Analysis</h1>

        <p>Enter a sentence and check its sentiment.</p>

        <form method="POST">

            <textarea
                name="text"
                placeholder="Enter your text here..."
                required
            >{{ text }}</textarea>

            <br>

            <button type="submit">Analyze Sentiment</button>

        </form>


        {% if sentiment %}

        <div class="result">

            <h2>Result</h2>

            <p>
                <b>Sentiment:</b> {{ sentiment }}
            </p>

            <p>
                <b>Polarity:</b> {{ polarity }}
            </p>

            <p>
                <b>Subjectivity:</b> {{ subjectivity }}
            </p>

        </div>

        {% endif %}

    </div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    sentiment = ""
    polarity = ""
    subjectivity = ""
    text = ""

    if request.method == "POST":

        # Get text entered by the user
        text = request.form["text"]

        # Create TextBlob object
        blob = TextBlob(text)

        # Get polarity and subjectivity
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Decide the sentiment
        if polarity > 0:
            sentiment = "Positive"

        elif polarity < 0:
            sentiment = "Negative"

        else:
            sentiment = "Neutral"

    return render_template_string(
        html_page,
        sentiment=sentiment,
        polarity=round(polarity, 2) if polarity != "" else "",
        subjectivity=round(subjectivity, 2) if subjectivity != "" else "",
        text=text
    )


if __name__ == "__main__":
    app.run(debug=True)