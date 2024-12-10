from database.db import Database
from sqlalchemy import DateTime
from datetime import datetime

db = Database().get_db()


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)
    format = db.Column(db.String(20))
    file_path = db.Column(db.String(255))
    type = db.Column(db.String(255))
    name = db.Column(db.String(255))
    created_at = db.Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f'<Report {self.id}>'
    
    @property
    def formatted_created_at(self):
        return self.created_at.strftime("%d/%m/%Y %H:%M:%S")

class IPAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(15), unique=True, nullable=False)
    status = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<IPAddress {self.ip_address}>'
