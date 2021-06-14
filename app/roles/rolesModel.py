from app import db

class RolesModel(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    rol = db.Column(db.String(80))
    status = db.Column(db.Integer)

    users = db.relationship('UsersModel', back_populates = 'rol')
    def __repr__(self):
        return f'Rol: {self.rol}'