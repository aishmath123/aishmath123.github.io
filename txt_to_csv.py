#Written by Vikram Yabannavar on 5/13/17

# Short script to read files from all four subdirectories 
# and combine their results into one csv called 'emails.csv'
import csv
import itertools
import os.path

#writing categories
with open('email.csv','a') as out_file:
	writer = csv.writer(out_file,delimiter=',')
	fields = ['class','message']
	writer.writerow(fields)

#Writing from the spam-train folder
for filename in os.listdir('spam-train'):
	if filename.endswith(".txt"):
		with open('spam-train/'+str(filename), 'r') as in_file:

		    with open('email.csv', 'a') as out_file:
		        writer = csv.writer(out_file)
		        for line in in_file:
		        	writer.writerow(['spam',line])

#writing from the nonspam-train folders
for filename in os.listdir('nonspam-train'):
	if filename.endswith(".txt"):
		with open('nonspam-train/'+str(filename),'r') as in_file:
			with open('email.csv','a') as out_file:
				writer = csv.writer(out_file,delimiter=',')
				for line in in_file:
					writer.writerow(['ham',line])

#writing from the spam-test folders
for filename in os.listdir('spam-test'):
	if filename.endswith(".txt"):
		with open('spam-test/'+str(filename),'r') as in_file:
			with open('email.csv','a') as out_file:
				writer = csv.writer(out_file,delimiter=',')
				for line in in_file:
					writer.writerow(['spam',line])


#writing from the spam-test folders
for filename in os.listdir('nonspam-test'):
	if filename.endswith(".txt"):
		with open('nonspam-test/'+str(filename),'r') as in_file:
			with open('email.csv','a') as out_file:
				writer = csv.writer(out_file,delimiter=',')
				for line in in_file:
					writer.writerow(['ham',line])