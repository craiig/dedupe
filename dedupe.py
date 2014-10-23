#!/usr/bin/python

#really simple dedup program
import csv

filename = "test.csv"

#open the csv file
csvfile = csv.reader(open(filename), delimiter=',')
header = csvfile.next() #read first line which is the header

for row in csvfile:
	print "---- First record"
	print row
	print row[0]
	print row[1]
	print "----"