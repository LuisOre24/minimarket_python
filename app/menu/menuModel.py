from app import db

class MenuModel(db.Model):
    __tablename__ = 'menu'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    menu = db.Column(db.String(80))
    url = db.Column(db.String(100))
    icon = db.Column(db.String(100))
    status = db.Column(db.Integer)

    def __repr__(self):
        return f'Menu: {self.menu}'