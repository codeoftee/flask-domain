from app import db
from datetime import datetime

class Domains(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain_name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    registration_date = db.Column(db.DateTime, default=datetime.now)
    expiry_date = db.Column(db.DateTime)
    status = db.Column(db.String(10))

    def __repr__(self):
        return f"<Domain {self.domain_name}>"
