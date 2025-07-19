import sys
import csv

if len(sys.argv) != 3:
    print("Wrong number of arguments")
    sys.exit(1)

try:
    with open(sys.argv[1]) as file:
        pass
except FileNotFoundError:
    print(f"Could not read file")
    sys.exit(1)

else:
    with open(sys.argv[1]) as file:
        reader = []
        reader = csv.DictReader(file)

        with open(sys.argv[2], 'w') as after_file:
            writer = csv.DictWriter(after_file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            
            for row in reader:
                name = row["name"]
                house = row["house"]
                fname = name.replace('"', '').split(",")[1].strip()
                lname = name.replace('"', '').split(",")[0].strip()

                writer.writerow({
                    "first": fname, 
                    "last": lname, 
                    "house": house})
