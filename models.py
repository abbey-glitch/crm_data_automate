from database import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    # PRODUCTS TABLE
    cursor.execute("""CREATE TABLE IF NOT EXISTS products(
    product_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    category ENUM('Wears', 'Electronics', 'Stationery'),
    brand VARCHAR(100) NOT NULL,
    product_url VARCHAR(150)
    )
    """)

    # CUSTOMERS TABLE
    cursor.execute(""" CREATE TABLE IF NOT EXISTS customers(
    customer_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    full_name VARCHAR(200),
    gender ENUM('Male', 'Female', 'Custom'),
    city VARCHAR(100)
    )
    """)

    # Date Table
    cursor.execute(""" CREATE TABLE IF NOT EXISTS date_dim(
    date_id INT AUTO_INCREMENT PRIMARY KEY,
    full_date DATE,
    day INT,
    month INT, 
    year INT
    )
    """)
    
    # sales Fact table
    cursor.execute(""" CREATE TABLE IF NOT EXISTS sales(
    sales_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    date_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price FLOAT,
    revenue FLOAT
    )
    """)
    

    conn.commit()
    conn.close()
    print("All tables created successfully.")