from app.sales.salesForm import SalesForms
from flask_login.utils import login_required
from app import app
from flask import render_template, request
from flask_login import login_required
from app.sales.salesForm import SalesForms
from app.sales.salesController import SalesController
from app.products.productsController import ProductsController
from app.documents.documentsController import DocumentsController
from app.middleware import seller, administrator


@app.route('/report')
@login_required
@seller
def sales():
    page = request.args.get('page', type=int, default=1)
    controller = SalesController()
    sales = controller.records(page)
    return render_template('views/report_sales/index.html', title='Reporte Ventas', data=sales)

@app.route('/sell', methods=['GET', 'POST'])
@login_required
@seller
def sell():
    form = SalesForms()
    products = ProductsController.get_all()
    form.product_id.choices = [(p.id, p.product) for p in products]
    documents = DocumentsController.get_all()
    form.document_id.choices = [(d.id, d.document) for d in documents]
    if form.validate_on_submit():
        controller = SalesController()
        return controller.register(form)
    return render_template('views/sales/sale.html', title='Venta', form=form)

@app.route('/report/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@administrator
def sales_delete(id):
    controller = SalesController()
    return controller.delete(id)