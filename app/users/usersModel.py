from app import db

class UsersModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(150))
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    rol = db.relationship('RolesModel', uselist=False, back_populates = 'users')
    product = db.relationship('ProductsModel',  back_populates = 'storer')

    def __repr__(self):
        return f'User: {self.user}'