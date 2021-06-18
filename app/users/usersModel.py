from app import db, login
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin

class UsersModel(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(150))
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    rol = db.relationship('RolesModel', uselist=False, back_populates = 'users')
    product = db.relationship('ProductsModel',  back_populates = 'storer')
    sale = db.relationship('SalesModel', back_populates = 'seller')

    def __repr__(self):
        return f'User: {self.user}'

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


# Obtiene los datos del usuario cuando se conecte
@login.user_loader
def load_user(user_id):
    return UsersModel.query.get(int(user_id))