from flask import redirect, url_for, request, render_template, session
from app import app

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    # Read the values from the form
    original_text = request.form['text']
    target_language = request.form['language']
    return render_template(
        'results.html',
        translated_text=target_language,
        original_text=original_text,
        target_language=target_language
    )