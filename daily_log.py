import os
from datetime import date
today = date.today()
f = open('daily_log.txt', 'r')
contents = f.read()
f.close()
f = open('daily_log.txt', 'w')
tasks = ["Cracking the coding interview",
		"1 Chapter CLRS",
		"1 Slide Deck, EECS 281",
		"Anki Chinese",
		"App status",
		"1 problem, leetcode"]
		
new_info = "Date: " + str(today.month)+ "-" + str(today.day) + "-" + str(today.year) + \
			"\n"
new_info += '{0: <50}'.format('Task')
new_info += 'Completed\n'
for item in tasks:
	print("Did you complete " + item + "?")
	resp = input()
	new_info += '{0: <50}'.format(item)
	new_info += resp + '\n'
new_info += '\n\n'
contents = new_info + contents;
f.write(contents)
