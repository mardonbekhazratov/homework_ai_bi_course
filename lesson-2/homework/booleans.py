# 1
username = input("Enter username: ")
password = input("Enter password: ")
if len(username.strip())>0 and len(password.strip())>0:
    print(True)
else:
    print(False)

# 2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a==b)

# 3
a = int(input("Enter a number: "))
if a>0 and a%2==0:
    print(True)
else:
    print(False)

# 4
a,b,c = map(int,input("Enter three numbers:\n").split())
print(a!=b and b!=c and a!=c)

# 5
s = input("Enter first string: ")
t = input("Enter second string: ")
print(len(s) == len(t))

# 6
a = int(input("Enter a number: "))
print(a%3==0 and a%5==0)

# 7
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(a+b>50.8)
