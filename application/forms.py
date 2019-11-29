from wtforms import StringField, SubmitField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    user_name = StringField('User name: ',
        validators=[DataRequired(message=None), Length(min=2, max=30)
        ]    
    )
    password = StringField('Password: ',
        validators=[DataRequired(message=None), Length(min=5, max=30)
        ]    
    )

class RegisterForm(FlaskForm):
    user_name = StringField('User name: ',
        validators=[DataRequired(message=None), Length(min=2, max=30)
        ]    
    )
    password = StringField('Password: ',
        validators=[DataRequired(message=None), Length(min=5, max=30)
        ]    
    )
    confirm-password = StringField('please confirm your password: ',
        validators=[DataRequired(message=None), Length(min=5, max=30)
        ]    
    )
    first_name = StringField('First name: ',
        validators=[DataRequired(message=None), Length(min=2, max=30)
        ]    
    )
    last_name = StringField('Last name: ',
        validators=[DataRequired(message=None), Length(min=2, max=30)
        ]    
    )

class CreateCard(FlaskForm):
    card_name = StringField('Card Name: ',
        validators=[DataRequired(message=None), Length(min=2, max=30)
        ]    
    )
    card_attk = IntegerField('Attack: ',
        validators=[DataRequired(message=None))
        ]    
    )
    card_def = IntegerField('Defense: ',
        validators=[DataRequired(message=None))
        ]    
    )

class Createdeck(FlaskForm):
    deck_name = StringField('Deck name: ',
    validators=[DataRequired(message=None), Length(min=2, max=30)
        ]    
    )