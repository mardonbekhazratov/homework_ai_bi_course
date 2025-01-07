import json
import csv

with open("tasks.json",'r') as file:
    data = json.load(file)
    for row in data:
        for key,value in row.items():
            print(f"{key}: {value}")
        print()
    
with open("tasks.json",'w') as file:
    json.dump(data,file,indent=4)

with open("tasks.json",'r') as file:
    data = json.load(file)
    f = open("tasks.csv",'w')
    writer = csv.writer(f)
    writer.writerow(data[0].keys())
    for i in data:
        writer.writerow(i.values())
    f.close()