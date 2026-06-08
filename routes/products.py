from flask import Blueprint, jsonify, request
from database import get_connection

products_bp = Blueprint('products', __name__)

@products_bp.route('/')
def get_products():
    return jsonify({
        "message": "Products endpoint"
    })

@products_bp.route('/register', methods=['POST'])
def create_products():
    conn = get_connection()
    cursor = conn.cursor()
    data = request.get_json()
    product_name = data.get('product_name')
    product_price = data.get('product_price')
    category = data.get('category')
    brand = data.get('brand')
    product_url = data.get('product_url')

    product_data = (product_name, category, brand, product_url)
    cursor.execute("INSERT INTO products(`product_name`, `category`, `brand`, `product_url`) VALUE(%s, %s, %s, %s)", (product_data))

    conn.commit()
    conn.close()

    return jsonify({
        "message": product_data,
        "success": "product saved"
    })

