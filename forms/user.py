from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired, Optional


class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    cult_token = StringField("Cult Token", validators=[Optional()])
    latitude = StringField("Latitude", validators=[Optional()])
    longitude = StringField("Longitude", validators=[Optional()])
    submit = SubmitField("Create User")
