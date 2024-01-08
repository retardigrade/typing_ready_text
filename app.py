from flask import Flask, request, render_template
from logic.rules import fix_text

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return render_template('index_empty.html')
    elif request.method == 'POST':
        original_text = request.form['text']
        return render_template('index_filled.html',
                               original_text=original_text,
                               formatted_text=fix_text(original_text))
