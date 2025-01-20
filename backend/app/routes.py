from flask import Blueprint, jsonify, request
from app.services import get_items, create_item, delete_item

items_blueprint = Blueprint('items', __name__)

# route buat ambil semua item
@items_blueprint.route('/items', methods=['GET'])
def fetch_items():
    items = get_items()
    return jsonify([{"id": str(item.id), "name": item.name, "description": item.description} for item in items])

# route buat tambah item baru
@items_blueprint.route('/items', methods=['POST'])
def add_item():
    data = request.json
    new_item = create_item(data['name'], data['description'])
    return jsonify({"id": str(new_item.id), "name": new_item.name, "description": new_item.description}), 201

# route buat hapus item berdasarkan id
@items_blueprint.route('/items/<id>', methods=['DELETE'])
def remove_item(id):
    delete_item(id)
    return jsonify({"message": "Item deleted"})
