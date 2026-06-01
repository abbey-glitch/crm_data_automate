from flask import Flask, jsonify, request
import os
app = Flask(__name__)  # locate the entry
from database import get_connection

from models import create_table


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT"))