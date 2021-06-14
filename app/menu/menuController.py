from app.menu.menuModel import MenuModel
from flask import g

class MenuController:
    def get_all(self):
        records = MenuModel.query.filter_by(status=1).all()
        g.menu = records
        