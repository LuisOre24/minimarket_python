from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CategoriesForm(FlaskForm):
    category = StringField('Categoria', validators=[DataRequired('Este campo es obligatorio')])
    submit = SubmitField('Enviar')
