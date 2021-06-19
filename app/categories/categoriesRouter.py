from app.middleware import administrator
from flask_login.utils import login_required
from app import app
from flask import render_template, request
from flask_login import login_required
from app.categories.categoriesController import CategoriesController
from app.categories.categoriesForm import CategoriesForm
from app.categories.categoriesModel import CategoriesModel
from app.middleware import administrator


@app.route('/categories')
@login_required
@administrator
def categories():
    page = request.args.get('page', type=int, default=1)
    controller = CategoriesController()
    categories = controller.records(page)
    return render_template('views/categories/index.html', title='Categorias', data=categories)

@app.route('/categories/create', methods=['GET', 'POST'])
@login_required
@administrator
def categories_create():
    form = CategoriesForm()
    if form.validate_on_submit():
        controller = CategoriesController()
        return controller.create(form)
    else:
        print("error")
    return render_template('views/categories/forms/create.html', title='Categorias - Crear', form=form)


@app.route('/categories/update/<int:id>', methods=['GET', 'POST'])
@login_required
@administrator
def categories_update(id):
    category = CategoriesModel.query.get_or_404(id)
    form = CategoriesForm(obj=category)
    if form.validate_on_submit():
        controller = CategoriesController()
        return controller.update(form, id)
    else:
        print("error")
    return render_template('views/categories/forms/update.html', 
                        title='Categorias - Actualizar', form=form, category_id=category.id)

@app.route('/categories/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@administrator
def categories_delete(id):
    controller = CategoriesController()
    return controller.delete(id)