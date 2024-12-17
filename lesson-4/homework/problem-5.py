p = input("Enter password: ")

u = False
for i in p:
    if ord(i)>=ord('A') and ord(i)<=ord('Z'):
        u = True

if len(p)<10:
    print("Password is too short.")
elif not u:
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")