from wtforms.widgets import ListWidget, CheckboxInput
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    IntegerField,
    SubmitField,
    SelectMultipleField
)
from wtforms.validators import DataRequired, Optional
from utils.enums import Class_timing, Class_type, Weekday


class PreferenceForm(FlaskForm):
    user_id = SelectField("User", coerce=int, validators=[DataRequired()])
    center = IntegerField("Center", validators=[DataRequired()])
    timing = SelectField(
        "Class Timing", choices=[(e.name, e.name) for e in Class_timing]
    )
    class_type = SelectField(
        "Class Type", choices=[(e.name, e.name) for e in Class_type]
    )
    days_of_week = SelectMultipleField(
        "Days of the Week",
        choices=[(str(d.value), d.name) for d in Weekday],
        validators=[Optional()],
        option_widget=CheckboxInput(),
        widget=ListWidget(prefix_label=False)
    )
    submit = SubmitField("Create Preference")
