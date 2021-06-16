from app import app
from flask import render_template

@app.route('/products')
def products():
    return render_template('views/products/index.html')