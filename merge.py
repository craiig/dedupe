import sys

overwrite_columns = dict()
tag_column = dict()
def merge_record(a, b, header=None):
	#set up dictionary to remember the columns to overwrite
	#if not hasattr(merge_record, 'overwrite_columns'):
	#	merge_record.overwrite_columns = dict()

	#assuming a and b are lists
	if len(a) != len(b):
		raise Exception("record length does not match")

	print "---- Merging record"
	new = list(a)
	for i in range(len(b)):
		if b[i] != "":
			if new[i] == "":
				new[i] = b[i]
			elif new[i] == b[i]:
				pass #nothing to do because they already match!
			elif i not in overwrite_columns and i not in tag_column:
				if header != None:
					print "Both records have a value in column \"%s\", which one do you want to keep?" % (header[i])
				else: 
					print "Both records have a value in column %d, which one do you want to keep?" % (i)
				print "[A]: " + new[i]
				print "[B]: " + b[i]
				print "[F]: Always keep first seen value (never will ask you about this column again)"
				print "[T]: Merge this column as the tag column"

				done = False
				while not done:
					choice = sys.stdin.readline().strip().upper()
					if choice == "A":
						print "Using value from A: %s" % new[i]
						done = True
					if choice =="T":
						tag_column[i] = 1
						done = True
					if choice == "B":
						new[i] = b[i]
						print "Using value from B: %s" % b[i]
						done = True
					if choice == "F":
						#remember this column should never be asked again
						overwrite_columns[i] = 1
						print overwrite_columns
						print "Ok, always keeping first value for column %d" % i
						done = True

			if i in tag_column:
				#parse column as tag
				new[i] = map(lambda x: x.strip(), new[i].split(","))
				print "Tag column parsed:"
				print "A was parsed as " + str(new[i])
				print "B was parsed as " + str(  map(lambda x: x.strip(), b[i].split(",")))
				new[i] = ", ".join(set(new[i] + map( lambda x: x.strip(), b[i].split(",")))) #sorry sorry sorry

	return new

#testing code
#header = ["one", "two", "three", "four", "five", "tags"]
#a = ['x','y', '', '10', "666", "12, 34,67,11"]
#b = ['x','y', '20', '', "44", "89, 10, 11, 12"]
#print merge_record(a, b, header)
#print merge_record(a, b)