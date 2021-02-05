from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email
from app.models import BookRequest
from app import ma

class BookRequestForm(FlaskForm):
    title = StringField('Book Title', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    submit = SubmitField('Request')

class BookRequestSchema(ma.ModelSchema):
    class Meta:
        model = BookRequest
