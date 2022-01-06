from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('pages/home.html',page='Home')

@app.route('/analisis-citra')
def analisis_citra():
    return render_template('pages/analisis.html',page='Analisis')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 