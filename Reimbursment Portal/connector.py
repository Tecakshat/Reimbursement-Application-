import mysql.connector


conn = mysql.connector.connect(
        host="localhost",
        database="reimbustment_database",
        username="root",
        password="@bhi2672"
    )

conn.commit()
conn.close()
print("Connection established")

