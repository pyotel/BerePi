#!/usr/bin/python
import sys
import getopt
import csv
import string
from influxdb import InfluxDBClient

str_field = ""
time = int(0)
server = "localhost"
port = 8086
measurement = ""
dbname = ""
dbid = "root"
dbpasswd = "root"
insert_query = ""
tags = ""
time_interval = int(0)
tags_arr = {}

try :
    opts, args = getopt.getopt(sys.argv[1:], "hf:t:s:p:m:d:i:w:n:v:a",
            ["help", "field=","time=", "server=", "measurement=","dbname=", "dbid=", "dbpasswd=", "tags=", "input=","interval=", "tags="])
except getopt.GetoptError, err :
    print str(err)
    sys.exit(1)

for o, a in opts:
    if o in ("-h", "--help") :
        print "Help message"
        sys.exit(1)
    elif o in ("-f","--field") :
        str_field = a.split(',')
    elif o in ("-t","--time") :
        time = int(a) * int(1000000000)
    elif o in ("-s","--server") :
        server = a
    elif o in ("-p","--port") :
        port = a
    elif o in ("-m","--measurement") :
        measurement = a
    elif o in ("-d","--dbname") :
        dbname = a
    elif o in ("-i","--dbid") :
        dbid = a
    elif o in ("-w","--dbpasswd") :
        dbpasswd = a
    elif o in ("-a","--tags") :
        tags = a.split(',')
    elif o in ("-n","--input") :
        inputfile = a
    elif o in ("-v","--interval") :
        time_interval = int(a) * int(1000000000)

for tags_elem in tags :
    tags_elem = tags_elem.split('=')
    tags_arr[tags_elem[0]] = tags_elem[1]

client = InfluxDBClient(server, port, dbid, dbpasswd, dbname)

with open(inputfile,'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',',quotechar='|')
    for field_value in spamreader:
        if len(field_value) > 0 :
            for n in range(0,len(str_field)) :
                json_body = [
                                {
                                    "measurement": measurement,
                                    "tags": tags_arr,
                                    "time": time,
                                    "fields": {str_field[n] : field_value[n]}
                                }
                ]
                client.write_points(json_body)
                query = "select %s from %s" % (str_field[n], measurement)
            time = time + time_interval
