from .. import db


class UploadFile(db.Model):
    __tablename__ = "upload_file"

    id = db.Column("id", db.Integer, primary_key=True)
    file_name = db.Column("file_name", db.String(500))
    file_url = db.Column("file_url", db.String(500))
    upload_time = db.Column("upload_time", db.DateTime)
    upload_people = db.Column("upload_people", db.Integer)
    is_delete = db.Column("is_delete", db.Integer, default=0)
