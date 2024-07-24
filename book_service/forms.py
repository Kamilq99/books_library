from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    cover = FileField(
        'Book Cover', 
        validators=[FileRequired(), FileAllowed(
            ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'],
            'Images only!'
        )]
    )
    submit = SubmitField('Add Book')