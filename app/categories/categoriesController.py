from app import db
from app.categories.categoriesModel import CategoriesModel
from flask import redirect, url_for, flash

class CategoriesController:

    def records(self, page):
        return CategoriesModel.query.order_by(CategoriesModel.id).paginate(
            page=page, per_page=5
        )

    def create(self, form):
        try:
            name_category = form.category.data
            category = CategoriesModel(category=name_category, status=1)
            db.session.add(category)
            db.session.commit()
            flash(f'Se genero nueva categoria: {name_category}', category='success')
            return redirect(url_for('categories'))
        except Exception as ex:
            print(str(ex))
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(ex)}', category='danger')
            return redirect(url_for('categories_create'))

    def update(self, form, category_id):
        try:
            name_category = form.category.data
            category = CategoriesModel.query.filter_by(id=category_id).first()
            category.category = name_category
            db.session.commit()
            flash(f'Se actualizo correctamente la categoria', category='success')
            return redirect(url_for('categories'))
        except Exception as ex:
            db.session.rollback()
            flash(f'Error al actualizar categoria , error -> {str(ex)}', category='danger')
            return redirect(url_for('categories_update', id=category_id))

    def delete(self, category_id):
        try:
            category = CategoriesModel.query.filter_by(id = category_id).first()
            status = 0 if category.status == 1 else 1
            category.status = status
            db.session.commit()
            flash(f'Se deshabilito con exito la categoria', category='succes')
            return redirect(url_for('categories'))
        except Exception as ex:
            db.session.rollback() 
            flash(f'Error ocurrido. Error -> {str(ex)}', category='danger')
