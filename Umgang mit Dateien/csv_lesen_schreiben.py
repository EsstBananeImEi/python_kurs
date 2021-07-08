# CSV

# Read ohne Module
with open("../Materialien/test_csv_read.csv", "r") as csvfile:
    for line in csvfile.readlines():
        splitted = line.strip().split(";")
        print(splitted)
        print(splitted[0] + ': ' + splitted[1])

header = ['name', 'age', 'residence']
data = [['Peter', 23, "Köln"], ['Lisa', 22, "Frankfurt"]]

# Write ohne CSV Module
with open("../Materialien/test_csv_write.csv", "w", encoding="UTF8") as csvfile:
    csvfile.write(",".join(header) + "\n")
    for line in data:
        csvfile.write(",".join([str(x) for x in line]) + "\n")


# Read mit CSV Module
import csv

with open("../Materialien/test_csv_read.csv") as csvfile:
    lines = csv.reader(csvfile, delimiter=';')

    for line in lines:
        print(line)
        print(line[0] + ': ' + line[1])

header = ['name', 'age', 'residence']
data = [['Peter', 23, "Köln"], ['Lisa', 22, "Frankfurt"]]

# # Write mit CSV Module
with open('../Materialien/test_csv_write.csv', 'w', newline='', encoding="UTF8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(data)
