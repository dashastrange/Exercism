import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit("Please enter exactly one argument.")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Please enter a .csv file.")

file_name = sys.argv[1]

try:
    with open(file_name) as f:
        reader = csv.reader(f)
        rows = list(reader)
        if not rows:
            sys.exit("CSV file is empty.")
        headers = rows[0]
        data = rows[1:]
        print(tabulate(data, headers, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist.")











