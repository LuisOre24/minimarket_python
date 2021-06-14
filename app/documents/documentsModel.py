from app import db

class DocumentsModel(db.Model):
    __tablename__ = 'document'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    document = db.Column(db.String(50))
    status = db.Column(db.Integer)

    def __repr__(self):
        return f'Document: {self.document}'