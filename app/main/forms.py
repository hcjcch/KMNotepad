from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(Form):

    """docstring for NameForm"""
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")
