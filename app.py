from flask import Flask, render_template, request, send_from_directory, send_file
from pytube import YouTube
from json import dumps as json_dumps
import sqlite3
from random import randint, choice as random_choice
from os import remove as os_remove
from io import BytesIO

servername = "http://127.0.0.1/"
conn = sqlite3.connect("data.yttomp3", check_same_thread=False)

app = Flask(__name__)

def randomString(start, end):
    randomInt = randint(start, end)
    chars = "0123456789-_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    token = ""
    for i in range(randomInt):
        token += random_choice(chars)
    return token

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-options", methods=['GET', 'POST'])
def get_link():
    if "youtube-url" not in request.form:
        res = {
            "status": "failure",
            "message": "method not allowed",
        }
        responseMain = app.response_class(
            response=json_dumps(res),
            status=405,
            mimetype="application/json"
        )
        return responseMain
    youtubeLink = request.form.get("youtube-url")
    yt = YouTube(youtubeLink)
    data = {
        "status": "success",
        "thumbnail_url": yt.thumbnail_url,
        "title": yt.title,
        "data": [],
    }

    for item in yt.streams:
        itag = item.itag
        mime_type = item.mime_type
        res = item.resolution
        if res == None:
            res = item.abr
        filesize = yt.streams.get_by_itag(itag).filesize
        dataObj = {
            "itag": itag,
            "mime_type": mime_type,
            "resolution": res,
            "filesize": filesize,
        }
        data["data"].append(dataObj)

    response = app.response_class(
        response=json_dumps(data),
        status=200,
        mimetype="application/json"
    )

    return response


@app.route("/get-download-link", methods=['GET', 'POST'])
def get_download_link():
    # return request.form
    if "youtube_url" in request.form and "itag" in request.form:
        ytlink = request.form.get("youtube_url")
        itag = request.form.get("itag")
        fileId = randomString(20, 36)
        query = conn.execute(f'''
        INSERT INTO `data` (`file_id`, `youtube_itag`, `youtube_url`) VALUES ('{fileId}', '{itag}', '{ytlink}')
        ''')
        conn.commit()
        if query:
            dataToSend = {
                "status": "success",
                "url": servername + "download/" + fileId,
            }
        response = app.response_class(
            response=json_dumps(dataToSend),
            status=200,
            mimetype="application/json",
        )

        return response
    else:
        return '''{"status": "failure"}'''

# @app.route("/get-file/<path:path>")
# def get_file(path):
#     return send_file("files/" + path, mimetype="application/octet-stream", download_name=path, as_attachment=True)

@app.route("/download/<string:file_id>")
def download(file_id):
    query = conn.execute(f'''
    SELECT * FROM `data` WHERE `file_id` = '{file_id}'
    ''')
    data = query.fetchone()
    if data == None:
        req = request.path
        return render_template("error404.html", path=req), 404
    else:        
        yt = YouTube(data[3])
        itag = data[2]
        exactName = yt.streams.get_by_itag(itag).default_filename
        yt.streams.get_by_itag(itag).download("files")
        file_path = "files/" + exactName
        return_data = BytesIO()
        with open(file_path, "rb") as f:
            return_data.write(f.read())

        return_data.seek(0)

        os_remove(file_path)
        # conn.execute(f'''
        # DELETE FROM `data` WHERE `file_id` = '{file_id}'
        # ''')
        conn.commit()
        return send_file(return_data, mimetype="application/octet-stream", download_name=exactName, as_attachment=True)



@app.route("/favicon.ico")
def favicon_ico():
    return send_from_directory("static", "youtube-logo.ico")        

@app.errorhandler(404)
def errorHandler(error):
    req = request.path
    return render_template("error404.html", path=req), 404


app.run()

