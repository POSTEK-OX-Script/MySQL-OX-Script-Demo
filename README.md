Database Printer

This code is designed to print labels on a printer based on data retrieved from a MySQL database.

Installation

To run this code, you will need to have Python 3.8+ installed on your system. You will not need to install the pskfunc, pymysql, and datetime modules as they come standards on POSTEK printers. You can install them on your device if you would like. You can do this using pip by running the following command:

pip3 install pymysql datetime

Usage

Before running the code, you will need to replace the following variables with your own database connection information:

host
user
password
database
You will also need to replace the following variables with your own table and primary key information:

example_table
created_at
Once you have replaced the variables with your own information, you can run the code. The code will conduct a live polling every second to check if the database has new data. If there is new data, the code will print a label based on the data retrieved.

Note that polling the database too frequently may affect the performance of the database in large projects. It is recommended that the terminal device connects to the server, and the server accesses the database. When the data is updated, the server pushes the data to the terminal device.

License

This code is released under the MIT License. Please see the LICENSE file for more information.