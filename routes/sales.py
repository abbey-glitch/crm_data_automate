from flask import Flask, jsonify
from database import get_connection

app = Flask(__name__)

@app.route("/sales", methods=['GET'])
def get_sales():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sales")
    data = cursor.fetchall()

    conn.close()
    return jsonify(data)


@app.route("/add/sales", methods=["GET"])
def get_list():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sales (sales_id, product_id, customer_id, date_id, unit_price, quantity, revenue) VALUE (%s, %s, %s, %s, %s, %s, %s)", (1, 1, 1, 1, 500.00, 4, 2000.00))
    data = conn.commit()

    conn.close()
    return "data saved"