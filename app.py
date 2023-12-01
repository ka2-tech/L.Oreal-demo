from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', title='Docker Python', name='Tech 2K')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ['PORT'])