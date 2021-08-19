from flask import Flask, render_template, request
from difflib import SequenceMatcher
app=Flask(__name__,template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        text1=request.form["text1"]
        text2=request.form["text2"]
        print(text2)
        sim=SequenceMatcher(None,text1, text2).ratio()*100
        return render_template("index.html", sim=sim)
    else:
        return render_template("index.html", sim="")

app.run()
