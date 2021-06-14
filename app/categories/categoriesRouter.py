from app import app
from flask import render_template


@app.route('/categories')
def categories():
    return render_template('views/categories/index.html')