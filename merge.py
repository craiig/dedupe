import sys

overwrite_columns = dict()
def merge_record(a, b):
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
			elif i not in overwrite_columns:
				print "Both records have a value in column %d, which one do you want to keep?" % (i)
				print "[A]: " + new[i]
				print "[B]: " + b[i]
				print "[F] Always keep first seen value (never will ask you about this column again)"

				done = False
				while not done:
					choice = sys.stdin.readline().strip().upper()
					if choice == "A":
						print "Using value from A: %s" % new[i]
						done = True
					if choice == "B":
						new[i] = b[i]
						print "Using value from B: %s" % b[i]
						done = True
					elif choice == "F":
						#remember this column should never be asked again
						overwrite_columns[i] = 1;
						print overwrite_columns
						print "Ok, always keeping first value for column %d" % i
						done = True
	return new

a = ['x','y', '', '10', "33"]
b = ['x','y', '20', '', "44"]
print merge_record(a, b)
print merge_record(a, b)