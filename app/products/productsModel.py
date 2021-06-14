from app import db

class ProductsModel(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    product = db.Column(db.String(120), index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    stock = db.Column(db.Integer)
    price = db.Column(db.Float)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.Integer)

    category = db.relationship('CategoriesModel', back_populates='products')
    storer = db.relationship('UsersModel', back_populates='product')

    def __repr__(self):
        return f'Producto: {self.product}'
        