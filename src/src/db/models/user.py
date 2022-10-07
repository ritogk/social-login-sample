from datetime import datetime
from db.db import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    
    # #初期化
    # def __init__(title, auther, publisher):
    #     self.name = title.title()
    #     self.auther = auther.title()
    #     self.publisher = publisher.title()