import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = ''
port_id = 5432
conn = None

# Connect to database with psycopg2
try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute('DROP TABLE IF EXISTS User_table')
# Create table 
            create_script = ''' CREATE TABLE IF NOT EXISTS User_table (
                                    User_UID INT NOT NULL PRIMARY KEY,
                                    Username varchar(255), 
                                    role varchar (250),
                                    cash decimal,
                                    start date); '''
            cur.execute(create_script)
# Insert values 
            insert_script  = 'INSERT INTO User_table (User_UID, Username, role, cash, start) VALUES (%s, %s, %s, %s,%s)'
            insert_values = [(9, 'James', 'Stranger Things', '1','01-01-2022'),
                             (10, 'Robin', 'K-Drama', '1','07-06-2022'), 
                             (11, 'Xavier', 'Sci-fi', '2','03-29-2022')]
            for record in insert_values:
                cur.execute(insert_script, record)
# Update values
            update_script = 'UPDATE User_table SET cash = cash + (cash * 0.07)'
            cur.execute(update_script)
# Delete values
            delete_script = 'DELETE FROM User_table WHERE Username = %s'    
            delete_record = ('James',)
            cur.execute(delete_script, delete_record)
# Read values
            cur.execute('SELECT * FROM User_table')
            for record in cur.fetchall():
                print(record['User_UID'], record['role'])
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()