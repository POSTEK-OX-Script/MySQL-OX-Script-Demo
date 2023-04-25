from ox_script import *
import pymysql
import time
import datetime


# The following code is used to initialize the UI on the printer
controller = UIInit(
    UIPage(
        # We can use := to assign a variable to the controller of the UI element which we will use below
        text_on_screen := UIText(value='Listening for data...')
    ),
    # Setting require_execute_confirmation to False will allow the script to run without the need to press the execute button on the printer
    require_execute_confirmation=False,
)

# This is an example of how the query would look like and is not used, the variables used in this query such as
# example_table and created_at are replaced with the actual table name and primary key in the code below
query = "SELECT * FROM example_table WHERE created_at > \'%s\' ORDER BY created_at DESC"

# Replace the following with your database connection information
host = 'host name'
user = 'user name'
password = 'password'
database = 'database name'
table_name = 'example_table'
# Replace the following with the primary key of your table, this demo uses the
# time that the data is created as the primary key to get the latest data
primary_key = 'created_at'

def retrieve_from_database(previous_key=None):
    data_packet = ""
    cnx = pymysql.connect(host=host, user=user,
                          password=password, database=database, charset='utf8')
    cursor = cnx.cursor()
    if (previous_key is None):
        # Get the latest primary key from the database initially
        cursor.execute("SELECT MAX({}) FROM {}".format(primary_key, table_name))
        data_packet = cursor.fetchone()
    else:
        # Check if there is data in the database that was created after the 'previous_key' creation time
        query = "SELECT * FROM {} WHERE {} > \'%s\' ORDER BY {} DESC".format(table_name, primary_key, primary_key)
        cursor.execute(query % previous_key)
        data_packet = cursor.fetchall()
    cnx.close()
    return data_packet

# Get the latest primary key from the database
previous_key = retrieve_from_database()

# Define the label that will be printed
# Replace the following with the label design you would like to use
def drawLabel(value):
    PTK_DrawText(x_coordinate=10,
                 y_coordinate=10,
                 font_size=5,
                 data=str(value))
    PTK_PrintLabel(number_of_label=1)

# The following conducts a live polling every second to see if the database have new data
# Polling the database will create unnecessary network communication, which may affect the performance of the database in large projects.
# It is recommended that the terminal device connects to the server, and the server accesses the database. When the data is updated, the server pushes the data to the terminal device.
if __name__ == '__main__':
    while True:
        current_rows = retrieve_from_database(previous_key)
        if current_rows:
            text_on_screen.update('Data received, printing...')
            for row in current_rows:
                # Replace the following with the column name of the data you want to print
                value = row[1]
                # Replace the following with the label design you would like to use
                drawLabel(value)
                # After printing, replace the previous_key with the latest primary key
                for item in row:
                    if isinstance(item, datetime.datetime):
                        previous_key = (item,)
            time.sleep(2)
            text_on_screen.update('Listening for data...')
        time.sleep(1)
