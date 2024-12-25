# 1
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"{name}, you are {age} years old")

# 2
txt = "LMaasleitbtui"
print(txt[::2])
print(txt[1::2])

# 3
s = input()
print(len(s))
print(s.lower())
print(s.upper())

# 4
s = input()
print(["not ",""][s==s[::-1]] + "palindrome")

# 5
s = input()
vowel = 0
consonant = 0
for i in s:
    if i in "aeiouy":
        vowel += 1
    else:
        consonant += 1
print(vowel)
print(consonant)

# 6
s = input()
t = input()
if s in t:
    print("first string appears in second")
elif t in s:
    print("second string appears in first")
else:
    print("given strings don't have similarity")

# 7
s = input()
r = input()
w = input()
s = s.replace(r,w)
print(s)

# 8
s = input()
print(s[0], s[-1])

# 9
s = input()
print(s[::-1])

# 10
s = input()
print(s.count(' ') + 1)

# 11
s = input()
ok = False
for i in s:
    if i.isdigit():
        ok = True
if ok:
    print("String has digit in it")
else:
    print("String doesn't have digit in it")

# 12
a = input().split()
print(','.join(a))

# 13
s = input()
s = s.replace(' ','')
print(s)

# 14
s = input()
t = input()
if s==t:
    print("they are same")
else:
    print("they are different")

# 15
s = input()
ans = ""
for i in range(len(s)):
    if i==0 or s[i-1]==' ':
        ans += s[i]
print(ans)

# 16
s = input()
ch = input()
s = s.replace(ch,"")
print(s)

# 17
s = input()
ans = ""
for i in s:
    if i in "aeiouy":
        ans += "*"
    else:
        ans += i
print(ans)

# 18
s = input("Input: ")
print("Starts with:",s.split()[0])
print("Ends with:",s.split()[-1])