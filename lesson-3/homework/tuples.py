# 1
t = tuple(map(int,input().split()))
x = int(input())
print(t.count(x))

# 2
t = tuple(map(int,input().split()))
print(max(t))

# 3
t = tuple(map(int,input().split()))
print(min(t))

# 4
t = tuple(map(int,input().split()))
x = int(input())
print(x in t)

# 5
t = tuple(map(int,input().split()))
if len(t):
    print(t[0])
else:
    print("tuple is empty")

# 6
t = tuple(map(int,input().split()))
if len(t):
    print(t[-1])
else:
    print("tuple is empty")

# 7
t = tuple(map(int,input().split()))
print(len(t))

# 8
t = tuple(map(int,input().split()))
s = t[:3]
print(s)

# 9
t = tuple(map(int,input().split()))
s = tuple(map(int,input().split()))
print(t+s)

# 10
t = tuple(map(int,input().split()))
print(len(t)==0)

# 11
t = tuple(map(int,input().split()))
x = int(input())
for i in range(len(t)):
    if t[i]==x:
        print(i,end = " ")

# 12
t = tuple(map(int,input().split()))
print(sorted(t)[-2])

# 13
t = tuple(map(int,input().split()))
print(sorted(t)[1])

# 14
t = (5)
print(t)

# 15
a = list(map(int,input().split()))
t = tuple(a)
print(t)

# 16
t = tuple(map(int,input().split()))
print(t == sorted(t))

# 17
t = tuple(map(int,input().split()))
l,r=map(int,input().split())
print(max(t[l:r+1]))

# 18
t = tuple(map(int,input().split()))
l,r = map(int,input().split())
print(min(t[l:r+1]))

# 19
t = tuple(map(int,input().split()))
x = int(input())
t.pop(t.index(x))

# 20
t = tuple(map(int,input().split()))




