import psycopg2

# declare the connection string specifying
# the host name database name use name
# and password
conn_string = "host='127.0.0.1' dbname='players' user='admin' password='adminAdmin123!'"

# use connect function to establish the connection
conn = psycopg2.connect(conn_string)
print(conn.info.__dict__)
