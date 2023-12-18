import sys, os

with open('out_file.csv', 'w') as out_file:
	with open('in_file.txt', 'r') as in_file:
		for line in in_file:
			if 'Serial No: ' in line:
				str1 = line.split('Serial No:',1)[1]
				str2 = str1.strip
				finalstr = str2()[:15]
				out_file.write(finalstr + '\n')