from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from models import MyClient
from extensions import db, redis_client
import json

client_bp = Blueprint("client", __name__)
api = Api(client_bp)

class ClientResource(Resource):
    def get(self, slug):
        """Ambil data dari Redis atau Database"""
        data = redis_client.get(slug)
        if data:
            return jsonify(json.loads(data))  # Ambil dari Redis jika ada

        client = MyClient.query.filter_by(slug=slug).first()
        if client:
            client_dict = client.to_dict()
            redis_client.set(slug, json.dumps(client_dict))  # Simpan ke Redis
            return jsonify(client_dict)

        return {"message": "Client not found"}, 404

    def post(self):
        """Simpan data ke PostgreSQL dan Redis"""
        data = request.json
        if MyClient.query.filter_by(slug=data["slug"]).first():
            return {"message": "Slug already exists"}, 400

        client = MyClient(
            name=data["name"],
            slug=data["slug"],
            client_prefix=data["client_prefix"],
            is_project=data.get("is_project", "0"),
            self_capture=data.get("self_capture", "1"),
            client_logo=data.get("client_logo", "no-image.jpg"),
            address=data.get("address"),
            phone_number=data.get("phone_number"),
            city=data.get("city"),
        )

        db.session.add(client)
        db.session.commit()

        client_dict = client.to_dict()
        redis_client.set(data["slug"], json.dumps(client_dict))  # Simpan ke Redis
        return jsonify(client_dict)

    def put(self, slug):
        """Update data dalam PostgreSQL & Redis"""
        data = request.json
        client = MyClient.query.filter_by(slug=slug).first()
        if not client:
            return {"message": "Client not found"}, 404

        client.name = data.get("name", client.name)
        client.is_project = data.get("is_project", client.is_project)
        client.self_capture = data.get("self_capture", client.self_capture)
        client.client_prefix = data.get("client_prefix", client.client_prefix)
        client.client_logo = data.get("client_logo", client.client_logo)
        client.address = data.get("address", client.address)
        client.phone_number = data.get("phone_number", client.phone_number)
        client.city = data.get("city", client.city)

        db.session.commit()

        client_dict = client.to_dict()
        redis_client.set(slug, json.dumps(client_dict))  # Perbarui di Redis
        return jsonify(client_dict)

    def delete(self, slug):
        """Hapus data dari PostgreSQL & Redis"""
        client = MyClient.query.filter_by(slug=slug).first()
        if not client:
            return {"message": "Client not found"}, 404

        db.session.delete(client)
        db.session.commit()
        redis_client.delete(slug)  # Hapus dari Redis

        return {"message": "Client deleted successfully"}, 200


api.add_resource(ClientResource, "/client", "/client/<string:slug>")
