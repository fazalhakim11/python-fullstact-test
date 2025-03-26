from flask import Flask
from config import Config
from extensions import db
from routes import client_bp

app = Flask(__name__)
app.config.from_object(Config)

# Inisialisasi Database
db.init_app(app)

# Daftarkan Blueprint
app.register_blueprint(client_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Membuat tabel jika belum ada
    app.run(debug=True)
