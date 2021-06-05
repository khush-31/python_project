import psycopg2
import main

conn = psycopg2.connect(database="employee", password="khush123", port="5432", user="postgres")
cursor = conn.cursor()

# cursor.execute('''create table coustomer.data(
#             id   int primary key not null,
#             randm_number text  not null);''')

try:
    postgres_query = '''insert into coustomer.data(id , randm_number) VALUES(%s , %s);'''
    record = (main.b, main.tyre())
    cursor.execute(postgres_query, record)
except:
    print(" ERROR : please enter unique coustomer id, random no. tagged to this id is visible on webpage.click the link")

conn.commit()
conn.close()
main.app.run()
