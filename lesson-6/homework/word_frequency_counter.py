try:
    with open("sample.txt", "r") as f:
        pass
except:
    with open("sample.txt", "w") as f:
        print("sample.txt does not exist! Write your text here. You can write many lines and once you have done write -1 in a new line")
        while True:
            s = input()
            if s=="-1":
                break
            f.write(s + "\n")

f = open("sample.txt", "r")

d = dict()

for line in f.readlines():
    st = ""
    for ch in line:
        if ch.isalpha():
            st += ch.lower()
        else:
            if st=="":
                continue
            if st in d.keys():
                d[st] += 1
            else:
                d[st] = 1
            st = ""
    if st != "":
        if st in d.keys():
            d[st] += 1
        else:
            d[st] = 1

f.close()

ar = list()

for key, value in d.items():
    ar.append([value,key])

ar = list(reversed(sorted(ar)))
# print(ar)

with open("word_count_report.txt","w") as f:
    f.write("Word Count Report\n")

    count_of_words = 0
    for ij in ar:
        count_of_words += ij[0]

    f.write(f"Total words: {count_of_words}\n")
    f.write(f"Top {min(5,len(ar))} most common words:\n")

    for i in range(min(5,len(ar))):
        f.write(f"{ar[i][1]} - {ar[i][0]} times\n")

# bonus task

while True:
    print(f"if you want to get top words count write a number between 1 and {len(ar)}, else write 0")
    try:
        x = int(input())
        assert(x<len(ar))
        assert(x>=0)
    except:
        print("You picked wrong number. Try again!")
        continue
    if x==0:
        break
    for i in range(x):
        print(f"{i+1}. {ar[i][1]} - {ar[i][0]} times")