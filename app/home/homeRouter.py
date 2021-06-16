from app import app
from flask import render_template
from app.menu.menuController import MenuController


@app.route('/')
def index():
    return render_template('views/home/index.html')

@app.before_request
def before_request():   
    controller = MenuController()
    controller.get_all()
