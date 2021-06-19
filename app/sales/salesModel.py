from app import db
from sqlalchemy.sql import func

class SalesModel(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    cantidad = db.Column(db.Integer)
    total = db.Column(db.Float)
    total_total = db.Column(db.Float)
    fecha_venta = db.Column(db.DateTime(timezone=True), server_default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    document_id = db.Column(db.Integer, db.ForeignKey('document.id'))
    client = db.Column(db.String(350))
    status = db.Column(db.Integer)

    product = db.relationship('ProductsModel', back_populates = 'sales')
    seller = db.relationship('UsersModel', back_populates = 'sale')
    document = db.relationship('DocumentsModel', back_populates = 'sale')

    def __repr__(self):
        return f'venta: {self.id}'







