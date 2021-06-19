from app import db
from app.sales.salesModel import SalesModel
from flask import redirect,url_for,flash
from flask_login import current_user
from sqlalchemy.sql import func
from app.products.productsController import ProductsController
from app.products.productsModel import ProductsModel

class SalesController:
    
    def records(self, page):
        return SalesModel.query.order_by(SalesModel.id).paginate(
            page=page, per_page=5
        )

    def register(self, form):
        try:
            name_client = form.client.data
            name_product = form.product_id.data
            quantity_product = form.quantity.data
            subtotal = form.subtotal.data
            name_document = form.document_id.data
            sale = SalesModel(product_id = name_product,
                            cantidad = quantity_product,
                            total = subtotal,
                            total_total = subtotal,
                            fecha_venta = func.now(),
                            user_id = current_user.id,
                            document_id = name_document,
                            client = name_client,
                            status = 1)
            print(name_product, quantity_product,"register")
            product = ProductsModel.query.filter_by(id = name_product).first()
            product.stock = product.stock - quantity_product
            #ProductsController.update_stock_sold(name_product, quantity_product)
            db.session.add(sale)
            db.session.commit()
            flash('se registro correctamante la venta', category='success')
            return redirect(url_for('sales'))
        except Exception as ex:
            db.session.rollback()
            flash('Ocurrio un error al registrar venta', category='danger')
            return redirect(url_for('sell'))
        

    def delete(self, id_sale):
        try:
            sale = SalesModel.query.filter_by(id = id_sale).first()
            if (sale.status == 1):
                status = 0 
                sale.status = status
                product = ProductsModel.query.filter_by(id = sale.product_id).first()
                product.stock = product.stock + sale.cantidad
                #ProductsController.update_stock_cancel(id_sale, sale.cantidad)
                db.session.commit()
                flash(f'Venta Anulada', category='success')
                return redirect(url_for('sales'))
            else:
                flash(f'La venta ya fue anulada', category='warning')
                return redirect(url_for('sales'))
        except Exception as ex:
            db.session.rollback() 
            flash(f'Error ocurrido. Error -> {str(ex)}', category='danger')
            return redirect(url_for('sales_delete'))
