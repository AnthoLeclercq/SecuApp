import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REPORT_FOLDER = os.environ.get('PATH_REPORT_FOLDER') or 'reports'