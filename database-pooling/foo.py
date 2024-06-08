# my_other_module.py
from db_pool import PostgresConnectionPool

# Example usage
connection_params = {
    'host': 'your_host',
    'database': 'your_database',
    'user': 'your_username',
    'password': 'your_password'
}
pool = PostgresConnectionPool(connection_params)

# Now you can use 'pool' object to execute queries or perform database operations
result = pool.execute_query("SELECT * FROM your_table;")
print(result)
