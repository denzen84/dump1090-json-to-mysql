# -*- coding: utf-8 -*-

# (c) 2018-2019 Denis G Dugushkin

import json
import mysql.connector
import time

# ---------------------Configuration parameters----------------

# Path to file dump1090's "aircraft.json"
json_aircrafts = '/mnt/ramdisk/aircraft.json'

# MySQL config
dbconfig = {	'host': '192.168.xx.xx',
                'user': 'user',
                'password': 'password',
                'database': 'adsb'
                }

sql_table = 'adsb_primary'
tbr = 10 # Time between reads (seconds)
rtr = 5  # Rounds to read (count)
# -------------------------------------------------------------

MAG_GROUND = '0x00B8B1BC'; # Magic value for GROUND as altitude

def process_json(data):
    # JSON processing:
    # Read all available keys and parameters and
    # prepare SQL query
    _SQL = ''
    for aircraft in data['aircraft']:
        sql_cols = ','.join(aircraft.keys())
        str_values = []
        # Now follows shitting code. I have no idea how to make it better
        # It would be great to converse parameters to string list
        # like cool this operation -> ','.join()
        for value in list(aircraft.values()):
            if isinstance(value, list):
                tmp = '"{}"'.format(",".join(value)) # Make array as string with a quotation marks
            elif isinstance(value, str):
                if str(value) == 'ground':
                    tmp = MAG_GROUND
                else:
                    tmp = '"{}"'.format(value) # SQL also wants a quotation marks for string types
            else:
                tmp = str(value) # Other values
            str_values.append(tmp) # Add converted value to array
        sql_values = ','.join(str_values)
        # End of shitting code
        sql_cols = 'time_unix,{}'.format(sql_cols)
        sql_values = '{},{}'.format(data['now'], sql_values)
        _SQL += "INSERT INTO {0} ({1}) VALUES ({2});\n".format(sql_table, sql_cols, sql_values)
    return _SQL
    
if __name__ == '__main__':
    
    # Initialize MySQL
    cnx = mysql.connector.connect(**dbconfig)
    sqlcursor = cnx.cursor()
    
    # Main cycle
    for x in range(0, rtr): # Read n times with 'tbr' pauses
        try:
            with open(json_aircrafts) as json_file:
                data = json.load(json_file)
        except:
            pass
        else:
            _SQL = process_json(data);
            for result in sqlcursor.execute(_SQL, multi=True):
                pass
        cnx.commit()
        time.sleep(tbr)
        
    # Close MySQL
    sqlcursor.close()
    cnx.close()

