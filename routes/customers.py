from flask import Blueprint, jsonify

customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/')
def get_products():
    return jsonify({
        "message": "Customers endpoint"
    })