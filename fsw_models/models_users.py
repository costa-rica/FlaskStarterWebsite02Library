print("- in models_users.py")
from .base import Base, DatabaseSession
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, Boolean, Table
from itsdangerous.url_safe import URLSafeTimedSerializer
from datetime import datetime
from flask_login import UserMixin
from .config import config
import os
from flask import current_app


def default_username(context):
    return context.get_current_parameters()['email'].split('@')[0]


class Users(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column(String(255), unique = True, nullable = False)
    password = Column(Text, nullable = False)
    username = Column(Text, default=default_username)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def get_reset_token(self):

        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return serializer.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):

        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:

            payload = serializer.loads(token, max_age=1000)
            user_id = payload.get("user_id")
        except:
            return None

        db_session = DatabaseSession()
        try:
            user = db_session.query(Users).get(user_id)
        finally:
            db_session.close()  # Ensure the session is closed after use

        return user

    def __repr__(self):
        return f'Users(id: {self.id}, email: {self.email})'