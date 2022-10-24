from flask import redirect, url_for, request, render_template, session
from app import app
from app.model.translate import Translate

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    # Read the values from the form
    original_text = request.form['text']
    target_language = request.form['language']

    model = Translate()
    model.transform(
        text=original_text,
        target_language=target_language,
    )

    return render_template(
        'results.html',
        translated_text=model.translated_text,
        original_text=model.original_text,
        target_language=model.target_language,
        original_language = model.original_language
    )