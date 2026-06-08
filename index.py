from flask import Flask, jsonify, request
import os

app = Flask(__name__)  # locate the entry

from database import get_connection

from models import create_table

# import routes
# from routes.home import app
# from routes.sales import app
from routes.products import products_bp
from routes.customers import customers_bp

# from routes.sales import app
app.register_blueprint(
    products_bp,
    url_prefix='/products'
)

app.register_blueprint(
    customers_bp,
    url_prefix='/customers'
)





if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT"))