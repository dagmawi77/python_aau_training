import csv
#file = open("C:/Users/Dagi/Downloads/AD.csv", "r",encoding="utf-8")
#fileread = file.read()
#print(fileread)
#file.close()

with open("C:/Users/Dagi/Downloads/AD.csv", "r",encoding="utf-8") as file:

    reader = csv.reader(file)
    for row in reader:
        print(row)


