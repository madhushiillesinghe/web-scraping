from textblob import TextBlob
from flask import Flask, request, render_template, jsonify
from textblob.en import polarity

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route("/feedback" ,methods=['GET','POST'])
def feedback():

    polarity = None
    if request.method == "POST":
        input_text = request.form.get("user_input")

        blob = TextBlob(input_text)
        polarity = blob.sentiment.polarity
        print(polarity)
        if polarity > 0:
            polarity = "Positive"
        elif polarity < 0:
            polarity = "Negative"
        else:
            polarity = "Neutral"

    return render_template('index.html', polarity=polarity)

@app.route("/rest",methods=['POST'])
def restEndPoint():
    data=request.get_json()
    print(data.get('text'))

    blob = TextBlob(data.get('text'))
    polarity = blob.sentiment.polarity
    return jsonify({"Value":polarity,"value":data.get("text")})

if __name__ == "__main__":
    app.run(debug=True)