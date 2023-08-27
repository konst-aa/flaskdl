import asyncio
from flask import Flask, request, render_template, url_for, flash, redirect

# ...

app = Flask(__name__)

@app.route('/', methods=("GET", "POST"))
async def index():
    if request.method == "POST":
        print(request.form)
        return redirect(url_for("index"))
    return render_template('index.html', context={"a": 1})

@app.route("/create", methods=["POST"])
async def create():
    print(request)