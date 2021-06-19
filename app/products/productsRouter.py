from flask_login.utils import login_required
from app.categories.categoriesController import CategoriesController
from app import app
from flask import render_template, request
from flask_login import login_required
from app.products.productsController import ProductsController
from app.products.productsForm import ProductsForm
from app.products.productsModel import ProductsModel
from app.middleware import storer


@app.route('/products')
@login_required
@storer
def products():
    page = request.args.get('page', type=int, default=1)
    controller = ProductsController()
    products = controller.records(page)
    return render_template('views/products/index.html', title='Productos', data=products)

@app.route('/products/create', methods=['GET', 'POST'])
@login_required
@storer
def products_create():
    form = ProductsForm()
    categories = CategoriesController.get_all()
    form.category_id.choices = [(c.id, c.category) for c in categories]
    if form.validate_on_submit():
        controller = ProductsController()
        return controller.create(form)
    return render_template('views/products/forms/create.html', title='Productos - Crear', form=form)


@app.route('/products/update/<int:id>', methods=['GET', 'POST'])
@login_required
@storer
def products_update(id):
    product = ProductsModel.query.get_or_404(id)
    form = ProductsForm(obj=product)
    categories = CategoriesController.get_all()
    form.category_id.choices = [(c.id, c.category) for c in categories]
    if form.validate_on_submit():
        controller = ProductsController()
        return controller.update(form, id)
    else:
        print("error")
    return render_template('views/products/forms/update.html', 
                        title='Productos - Actualizar', form=form, product_id=product.id)

@app.route('/products/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@storer
def products_delete(id):
    controller = ProductsController()
    return controller.delete(id)