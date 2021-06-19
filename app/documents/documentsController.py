from app import db
from app.documents.documentsModel import DocumentsModel


class DocumentsController:

    def get_all():
        return DocumentsModel.query.filter_by(status=1).order_by(DocumentsModel.document).all()