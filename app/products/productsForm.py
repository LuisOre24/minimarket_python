from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired

class ProductsForm(FlaskForm):
    product = StringField('Producto', validators=[DataRequired('Campo requerido')])
    category_id = SelectField('Categoria', coerce=int, validators=[DataRequired('Seleccione una Categoria')])
    price = StringField('Precio')
    stock = StringField('Stock')
    submit = SubmitField('Enviar')