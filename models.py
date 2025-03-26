from extensions import db

class MyClient(db.Model):
    __tablename__ = "my_client"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    slug = db.Column(db.String(100), nullable=False, unique=True)
    is_project = db.Column(db.String(30), default="0", nullable=False)
    self_capture = db.Column(db.String(1), default="1", nullable=False)
    client_prefix = db.Column(db.String(4), nullable=False)
    client_logo = db.Column(db.String(255), default="no-image.jpg", nullable=False)
    address = db.Column(db.Text, default=None)
    phone_number = db.Column(db.String(50), default=None)
    city = db.Column(db.String(50), default=None)
    created_at = db.Column(db.TIMESTAMP, default=None)
    updated_at = db.Column(db.TIMESTAMP, default=None)
    deleted_at = db.Column(db.TIMESTAMP, default=None)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "is_project": self.is_project,
            "self_capture": self.self_capture,
            "client_prefix": self.client_prefix,
            "client_logo": self.client_logo,
            "address": self.address,
            "phone_number": self.phone_number,
            "city": self.city,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
            "deleted_at": str(self.deleted_at),
        }
