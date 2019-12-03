from application import db, login_manager
from flask_login import UserMixin

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=True)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    children = db.relationship("deck_list", backref='author', lazy=True)

    def __repr__(self):
        return ''.join(['User ID: ', str(self.id), '\r\n',
            'Name: ', self.first_name, ' ', self.last_name, '\r\n',
            'Admin? ', self.admin
        ])

    @login_manager.user_loader
    def load_user(id):
        return users.query.get(int(id)) 

class card_list(db.Model):
    card_ID = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(30)), nullable=False, unique=True)
    card_attk = db.Column(db.Integer, nullable=False)
    card_def = db.Column(db.Integer, nullable=False)
    children = db.relationship("deck_list", backref='author', lazy=True) 

    def __repr__(self):
        return ''.join(['Card ID: ', self.card_ID, '\r\n',
            'Name: ', self.card_name, '\r\n',
            'Attack: ', self.card_attk, ' ', 'Defense: ', self.card_def
        ])

class deck_list(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    deck_name = db.Column(db.String(30)), nullable=False)
    user_ID = db.Column(db.Integer, nullable=False, foreign_key("users.id"))
    card_ID = db.Column(db.Integer, nullable=False, foreign_key("card_list.card_ID"))

    def __repr__(self):
        return ''.join(['Deck ID: ', self.ID, '\r\n',
            'Name: ', self.deck_name, '\r\n',
            'User: ', self.user_ID, ' ', 'Card: ', self.card_ID
        ])