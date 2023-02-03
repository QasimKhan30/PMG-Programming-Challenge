import sys

def answer(args):
	
	#This algorithm will run in O(n * m) time where n = number of files and m = number of rows/headers in each file


	#loop over every file passed in 
	for i in range(len(args)):
		file_path = args[i]
		f = open(file_path,'r')
		#get filename without path
		filename = file_path.split('/')[1]

		if i == 0:
			#generate header row for table before parsing data
			row = f.readline().strip()
			headers = row.split(',')
			width_lens = []
			for header in headers:
				print("|" + header[1:-1],end='')
				width_lens.append(len(header[1:-1]))
			print("|filename|")
		
			#this nested for loop is used to add proper length seperators if we have extra columns
			#insert seperator between table header and table data with correct lengths
			#this slows down the algorithm significantly
			#we can avoid this be simply adding constant length seperators
			for table_width in width_lens:
				print("|",end='')
				for j in range(table_width):
					print("-",end='')
			print("|--------|")
			row = f.readline()
		else:
			#we have already generated the headers from the first file
			#skip the subsequent files' headers
			row = f.readline() # this is the empty string that breaks the while loop below
			row = f.readline() #this will be the next files header

		#keep reading lines until we reach the end of file
		while row != "":
			row = row.strip().split(',')

			# place table lines inbetween data
			# This will run in constant time because each row has 2 elements
			
			for data in row:
				
				print("|" + data[1:-1],end='')

			print("|" + filename + "|")

			# get next line
			row = f.readline()

		f.close()
		

		
#for command line arguments
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("incorrect usage: provide the path of a file to parse")
	else:
		answer(sys.argv[1:])