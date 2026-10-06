import csv as cs
#file = open("C:/Users/Dagi/Downloads/AD.csv", "r",encoding="utf-8")
#fileread = file.read()
#print(fileread)
#file.close()

with open("C:/Users/Dagi/Downloads/AD.csv", "r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    