from flask import Flask
from flask import render_template
from flask import request # for Http methods
from flask import jsonify
from flask import redirect
from flask import url_for
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import numpy as np
from sklearn.externals import joblib

app = Flask(__name__) #creating an instance of the class


@app.route('/')
def index():
    return render_template("index.html")



@app.route("/api", methods=["GET","POST"])
def api():
    if request.method == "POST":
        model = joblib.load('model.pkl')
        

        tweet = request.form["tweet"]
        text = [tweet]
        

        

        prediction = model.predict(text)

        if prediction == 'Real':
            msg = "Approximately 80%, your tweet Not Fake (Real tweet)."
            return render_template("index.html", msg=msg, tweet=tweet)
        else:
            error = "Approximately 80%, your tweet Fake"
            return render_template("index.html", error=error, tweet=tweet)
    else:
        return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)

  
