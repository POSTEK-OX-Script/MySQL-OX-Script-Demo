from pskfunc import *
import pymysql
import time
import datetime


# The following code is used to initialize the UI on the printer
controller = UIInit(
    UIPage(
        # We can use := to assign a variable to the controller of the UI element which we will use below
        text_on_screen := UIText(value='Initializing...')
    ),
    # Setting require_execute_confirmation to False will allow the script to run without the need to press the execute button on the printer
    require_execute_confirmation=False,
)

# Replace example_table with your table name, replace created_at with the primary key of your table, this demo uses time created as the primary key
query = "SELECT * FROM example_table WHERE created_at > %s ORDER BY created_at DESC"

# Replace the following with your database connection information
host = 'host name'
user = 'user name'
password = 'password'
database = 'database name'
cnx = pymysql.connect(host=host, user=user,
                      password=password, database=database, charset='utf8')
cursor = cnx.cursor()

# Get the latest primary key from the database
cursor.execute("SELECT MAX(created_at) FROM student")
previous_key = cursor.fetchone()
cnx.close()

# Define the label that will be printed
# Replace the following with the label design you would like to use
def drawLabel(value):
    PTK_DrawText(x_coordinate=10,
                 y_coordinate=10,
                 font_size=5,
                 data=str(value))
    PTK_PrintLabel()


# The following conducts a live polling every second to see if the database have new data
# Polling the database will create unnecessary network communication, which may affect the performance of the database in large projects.
# It is recommended that the terminal device connects to the server, and the server accesses the database. When the data is updated, the server pushes the data to the terminal device.
while True:
    text_on_screen.update('Listening for data...')
    cnx = pymysql.connect(host=host, user=user,
                          password=password, database=database, charset='utf8')
    cursor = cnx.cursor()
    # Check if there is data in the database that was created after the 'previous_key' creation time
    cursor.execute(
        "SELECT * FROM student WHERE created_at > %s ORDER BY created_at DESC" % previous_key)
    current_rows = cursor.fetchall()
    cnx.close()
    if current_rows:
        text_on_screen.update('Data received, printing...')
        for row in current_rows:
            # Replace the following with the column name of the data you want to print
            value = row[1]
            # Replace the following with the label design you would like to use
            drawLabel(value)
            for item in row:
                if (type(item) == datetime.datetime):
                    previous_created_at = (item,)
    time.sleep(1)
