import uuid
import shutil
import os
import io
from yt_dlp import YoutubeDL
import asyncio
from flask import Flask, request, render_template, url_for, flash, redirect, send_file

# ...

app = Flask(__name__)

@app.route('/', methods=("GET", "POST"))
async def index():
    if request.method == "POST":
        outfile = str(uuid.uuid1())
        opts = {"outtmpl": outfile}
        with YoutubeDL(opts) as ydl:
            ydl.download([request.form["link"]])
        print(request.form)
        cache = io.BytesIO()
        with open(outfile, 'rb') as fp:
            shutil.copyfileobj(fp, cache)
            cache.flush()
        cache.seek(0)
        os.remove(outfile)
        return send_file(cache, as_attachment=True, download_name=outfile)
    return render_template('index.html', context={"file": False})

@app.route("/create", methods=["POST"])
async def create():
    print(request)