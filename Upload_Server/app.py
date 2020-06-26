import os
from gevent.pywsgi import WSGIServer
from flask import Flask, render_template, request
from pyngrok import ngrok
from flask_ngrok import run_with_ngrok
__author__ = 'ibininja'

app = Flask(__name__)
#run_with_ngrok(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    try:
        target = os.path.join(APP_ROOT, 'images/')
        print(target)

        if not os.path.isdir(target):
            os.mkdir(target)

        for file in request.files.getlist("file"):
            print(file)
            filename = file.filename
            destination = "/".join([target, filename])
            print(destination)
            file.save(destination)
    
        return render_template("complete.html")
    except:
        return render_template("error.html")
if __name__ == "__main__":
#    app.run()

    http_server = WSGIServer(('0.0.0.0',80), app)

    http_server.serve_forever()
    #ngrok.connect(4555)
