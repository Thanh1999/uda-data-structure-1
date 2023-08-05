"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def print_first_text():
    first_record = texts[0]
    print('First record of texts, {} texts {} at time {}'.format(first_record[0], first_record[1], first_record[2]))

def print_first_call():
    first_record = calls[0]
    print('Last record of calls, {} calls {} at time {}, lasting {} seconds'.format(first_record[0], first_record[1], first_record[2], first_record[3]))

print_first_text()
print_first_call()