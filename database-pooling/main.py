import psycopg2
from concurrent.futures import ThreadPoolExecutor

class PostgresConnectionPool:
    def __init__(self, connection_params, pool_size=5):
        self.connection_params = connection_params
        self.pool = ThreadPoolExecutor(max_workers=pool_size)
        self.connections = []

    def get_connection(self):
        connection = psycopg2.connect(**self.connection_params)
        self.connections.append(connection)
        return connection

    def execute_query(self, query, *args):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, args)
        result = cursor.fetchall()
        cursor.close()
        connection.commit()
        return result

    def close_connections(self):
        for connection in self.connections:
            connection.close()

# Example usage:
if __name__ == "__main__":
    connection_params = {
        'host': 'your_host',
        'database': 'your_database',
        'user': 'your_username',
        'password': 'your_password'
    }
    pool = PostgresConnectionPool(connection_params)

    try:
        # Execute queries using the pool
        result = pool.execute_query("SELECT * FROM your_table;")
        print(result)
    finally:
        pool.close_connections()

