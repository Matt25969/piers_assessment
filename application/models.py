from application import db

class users(db.Model):
    user_ID = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=True)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    children = db.relationship("deck_list") 

class card_list(db.Model):
    card_ID = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(30)), nullable=False, unique=True)
    card_attk = db.Column(db.Integer, nullable=False)
    card_def = db.Column(db.Integer, nullable=False)
    children = db.relationship("deck_list") 

class deck_list(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    deck_name = db.Column(db.String(30)), nullable=False)
    user_ID = db.Column(db.Integer, nullable=False, foreign_key("users.user_ID"))
    card_ID = db.Column(db.Integer, nullable=False, foreign_key("card_list.card_ID"))