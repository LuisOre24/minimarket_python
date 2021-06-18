from flask_login.utils import login_required
from app import app
from flask import render_template, request
from flask_login import login_required
from app.sales.salesModel import SalesModel
from app.sales.salesController import SalesController


@app.route('/products')
@login_required
def sales():
    return render_template('views/products/index.html', title='Venta')

@app.route('/products/create', methods=['GET', 'POST'])
@login_required
def sales_create():
    pass


@app.route('/products/update/<int:id>', methods=['GET', 'POST'])
@login_required
def sales_update(id):
    pass

@app.route('/products/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def sales_delete(id):
    pass