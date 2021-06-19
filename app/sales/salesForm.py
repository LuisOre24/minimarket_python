from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.fields.core import FloatField, SelectField
from wtforms.validators import DataRequired


class SalesForms(FlaskForm):
    client = StringField('Cliente')
    product_id = SelectField('Producto', coerce=int)
    quantity = IntegerField('Cantidad')
    subtotal = FloatField('SubTotal')
    """total_total = StringField('Total') """
    document_id = SelectField('Documento')
    submit = SubmitField('Enviar')
    reset = SubmitField('Reset')