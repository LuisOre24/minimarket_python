from app import db
from app.products.productsModel import ProductsModel
from flask import redirect, url_for, flash

class ProductsController:

    def records(self, page):
        return ProductsModel.query.order_by(ProductsModel.id).paginate(
            page=page, per_page=5
        )

    def create(self, form):
        try:
            name_product = form.product.data
            category_product = form.category_id.data
            stock_product = form.stock.data
            price_product = form.price.data
            product = ProductsModel(product=name_product,
                                    category_id = category_product,
                                    stock = stock_product,
                                    price = price_product,
                                    status=1)
            db.session.add(product)
            db.session.commit()
            flash(f'Se genero un nuevo producto: {name_product}', category='success')
            return redirect(url_for('products'))
        except Exception as ex:
            print(str(ex))
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(ex)}', category='danger')
            return redirect(url_for('products_create'))

    def update(self, form, product_id):
        try:
            name_product = form.category.data
            category_product = form.category_id.data
            stock_product = form.stock.data
            price_product = form.price.data
            product = ProductsModel.query.filter_by(id=product_id).first()
            product.product = name_product
            product.category_id = category_product
            product.price = price_product
            product.stock = stock_product
            db.session.commit()
            flash(f'Se actualizo correctamente el producto', category='success')
            return redirect(url_for('products'))
        except Exception as ex:
            db.session.rollback()
            flash(f'Error al actualizar el producto , error -> {str(ex)}', category='danger')
            return redirect(url_for('products_update', id=product_id))

    def delete(self, product_id):
        try:
            product = ProductsModel.query.filter_by(id = product_id).first()
            status = 0 if product.status == 1 else 1
            product.status = status
            db.session.commit()
            flash(f'Se deshabilito con exito el producto', category='success')
            return redirect(url_for('products'))
        except Exception as ex:
            db.session.rollback() 
            flash(f'Error ocurrido. Error -> {str(ex)}', category='danger')
