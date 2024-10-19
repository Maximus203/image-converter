from flask import render_template, request, redirect, url_for
from app import app
from app.converter import batch_convert
import os

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        input_dir = request.form.get('input_dir')
        output_dir = request.form.get('output_dir')
        if os.path.isdir(input_dir) and os.path.isdir(output_dir):
            batch_convert(input_dir, output_dir)
            message = 'Conversion terminée avec succès.'
        else:
            message = 'Veuillez entrer des répertoires valides.'
        return render_template('index.html', message=message)
    return render_template('index.html', message=message)
