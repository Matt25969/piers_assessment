from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    user_name = StringField('User name: ',
        validators=[DataRequired(message=None), Length(min=2, max=30)
        ]    
    )
    password = PasswordField('Password: ',
        validators=[DataRequired(message=None), Length(min=5, max=30)
        ]    
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

class RegisterForm(FlaskForm):
    user_name = StringField('User name: ',
        validators=[DataRequired(message=None), Length(min=2, max=30)
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
    password = PasswordField('Password: ',
        validators=[DataRequired(message=None), Length(min=5, max=30)
        ]    
    )
    confirm-password = PasswordField('Please confirm your password: ',
        validators=[DataRequired(message=None), Length(min=5, max=30), EqualTo('password')
        ]    
    )
    
    def validate_user_name(self, user_name):
        user = users.query.filter_by(user_name=user_name.data).first()
        
        if user:
            raise ValidationError('User name is already in use!')

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

class CreateDeck(FlaskForm):
    deck_name = StringField('Deck name: ',
    validators=[DataRequired(message=None), Length(min=2, max=30)
        ]    
    )