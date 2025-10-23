from mysql.connector import pooling
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, MYSQL_PORT

# Create a connection pool
pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB
)

def get_conn():
    """Get a connection from the pool"""
    return pool.get_connection()

def initialize_db():
    """Create the users table if it doesn't exist"""
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
