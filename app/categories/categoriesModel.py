from app import db

class CategoriesModel(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(100), index=True)
    status = db.Column(db.Integer)

    products = db.relationship('ProductsModel', back_populates='category')

    def __repr__(self):
        return f'Category: {self.category}'