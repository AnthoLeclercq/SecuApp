from flask_sqlalchemy import SQLAlchemy

class Database:
    _instance = None

    def __new__(cls, app=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.db = SQLAlchemy(app)
        return cls._instance

    def init_app(self, app):
        self.db.init_app(app)

    def get_db(self):
        return self.db
