from flask import Flask, render_template, redirect
import os
app = Flask(__name__)

picFolder = os.path.join('static','images')

app.config['UPLOAD_FOLDER'] = picFolder

@app.route("/")
def redirectToProfile():
  return redirect("/profile")

@app.route("/profile")
def index():
  favicon = os.path.join(app.config['UPLOAD_FOLDER'], 'favicon.ico')
  myPhoto = os.path.join(app.config['UPLOAD_FOLDER'], 'MyPhoto.jpg')
  style = os.path.join(app.config['UPLOAD_FOLDER'], '../style.css')
  return render_template("index.html", fav = favicon, myPic = myPhoto, styleCss = style)

if __name__ == "__main__":
  app.run(host="localhost", port=5000)