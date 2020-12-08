from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))

    def __init__(self, **kwargs):
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")

    def serialize(self):
        return {
            "User id": self.id,
            "Username": self.username 
        }

class Channel(db.Model):
    __tablename__ = 'channels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    fr = db.Column(db.Integer, db.ForeignKey('users.id'))
    to = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.fr = kwargs.get("fr")
        self.to = kwargs.get("to")
        
    def serialize(self):
        return {
            "Channel id": self.id,
            "Channel name": self.name,
            "From": self.fr,
            "To": self.to
        }

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    fr = db.Column(db.Integer, db.ForeignKey('users.id'))
    to = db.Column(db.Integer, db.ForeignKey('users.id'))
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'))

    def __init__(self, **kwargs):
        self.message = kwargs.get("message")
        self.channel_id = kwargs.get("channel_id")
        self.fr = kwargs.get("fr")
        self.to = kwargs.get("to")
        
    def serialize(self):
        return {
            "Message id": self.id,
            "Message contents": self.contents,
            "From": self.fr,
            "To": self.to,
            "Sent in channel": self.channel_id 
        }