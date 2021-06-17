from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ProductsForm(FlaskForm):
    product = StringField('Producto')
    category_id = StringField('Categoria')
    price = StringField('Precio')
    stock = StringField('Stock')
    submit = SubmitField('Enviar')