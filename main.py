from app import app

from app.menu import menuModel
from app.roles import rolesModel
from app.users import usersModel
from app.categories import categoriesModel
from app.documents import documentsModel
from app.products import productsModel
from app.sales import salesModel

from app.menu import menuRouter
from app.auth import authRouter
from app.home import homeRouter
from app.products import productsRouter
from app.categories import categoriesRouter
from app.sales import salesRouter