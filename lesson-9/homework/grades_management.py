import csv

filename = "grades.csv"

with open(filename, 'r') as file:
    reader = csv.reader(file)

    fields = next(reader)
    
    rows = list()

    d = dict()
    count = dict()

    for row in reader:
        rows.append(row)
        if row[1] in d.keys():
            d[row[1]] += int(row[2])
            count[row[1]] += 1
        else:
            d[row[1]] = int(row[2])
            count[row[1]] = 1
    a = [["Subject","Average Grade"]]
    for key,value in d.items():
        a.append([key,value/count[key]])

    with open("average_grades.csv","w") as f:
        writer = csv.writer(f)
        writer.writerows(a)


