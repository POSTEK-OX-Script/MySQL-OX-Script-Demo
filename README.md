# MySQL-OX-Script-Demo

This code is designed to print labels on a printer based on data retrieved from a MySQL database.

## Demo video

A demonstration of what this script can do can be found here

https://youtu.be/QGUP1zCBlzo

## Installation

 To run this code, you will need to have Python 3.8+ installed on your printer(which comes standard on all POSTEK Printers that support OX Script after May 2023). You will not be able to execute this code directly on your computer as it is intended to be executed on the printer

## Usage

Before running the code, you will need to replace the following variables with your own database connection information:

 - host
 - user
 - password
 - database
    
You will also need to replace the following variables with your own table and primary key information:

 - example_table
 - created_at
    
Once you have replaced the variables with your own information, you can run the code through the methods outlined below. The code will conduct a live polling every second to check if the database has new data. If there is new data, the code will print a label based on the data retrieved.

Note that polling the database too frequently may affect the performance of the database in large projects. It is recommended that the terminal device connects to the server, and the server accesses the database. When the data is updated, the server pushes the data to the terminal device.

To execute this demo, simply load the .py file and commands1.txt(file for the label design) into your printer through the POSTEK App. Then to run the program you can initate it from the printer touch screen or the POSTEK App. 

- Initiating the program from printer touch screen
    - On your printer's touch screen, go to settings>Ox Script>[your file name].py. Press it and select run from the bottom right of the pop-up window
 
- Initating the program from the POSTEK App
    - Inside the App, select Ox Script from the left hand side. Connect to the printer that you just moved the files to and select the file from the left hand side drop down, click run on the top right hand corner

## License

This code is released under the MIT License. Please see the LICENSE file for more information.

## Disclaimer

This software is provided "as is" and the author of the software is not liable for any damages or losses that may arise from the use of the software. Use at your own risk.
