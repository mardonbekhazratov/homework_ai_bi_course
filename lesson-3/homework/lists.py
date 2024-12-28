# 1
a = list(map(int,input().split()))
x = int(input())
print(a.count(x))

# 2
a = list(map(int,input().split()))
print(sum(a))

# 3
a = list(map(int,input().split()))
print(max(a))

# 4
a = list(map(int,input().split()))
print(min(a))

# 5
a = list(map(int,input().split()))
x = int(input())
print(x in a)

# 6
a = list(map(int,input().split()))
if len(a)>0:
    print(a[0])
else:
    print("list is empty")

# 7
a = list(map(int,input().split()))
if len(a)>0:
    print(a[-1])
else:
    print("list is empty")

# 8
a = list(map(int,input().split()))
b = a[:3]
print(b)

# 9
a = list(map(int,input().split()))
b = list(reversed(a))
print(b)

# 10
a = list(map(int,input().split()))
b = list(sorted(a))
print(b)

# 11
a = list(map(int,input().split()))
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

# 12
a = list(map(int,input().split()))
x = int(input())
id = int(input())
a.insert(id,x)

# 13
a = list(map(int,input().split()))
x = int(input())
print(a.index(x))

# 14
a = list(map(int,input().split()))
print(len(a)==0)

# 15
a = list(map(int,input().split()))
ans = 0
for i in a:
    ans += i%2==0
print(ans)

# 16
a = list(map(int,input().split()))
ans = 0
for i in a:
    ans += i%2
print(ans)

# 17
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = a + b
print(c)

# 18
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ok = False
for i in range(len(a)-len(b)+1):
    for j in range(i,len(b)+i):
        if a[j] != b[j-i]:
            break
        if j == len(b)+i-1:
            ok = True
print(ok)

# 19
a = list(map(int,input().split()))
x = int(input())
y = int(input())
a[a.index(x)] = y

# 20
a = list(map(int,input().split()))
print(sorted(a)[-2])

# 21
a = list(map(int,input().split()))
print(sorted(a)[1])

# 22
a = list(map(int,input().split()))
b = [i for i in a if i%2==0]
print(b)

# 23
a = list(map(int,input().split()))
b = [i for i in a if i%2==1]
print(b)

# 24
a = list(map(int,input().split()))
print(len(a))

# 25
a = list(map(int,input().split()))
b = a.copy()
print(b)

# 26
a = list(map(int,input().split()))
if len(a)%2==0:
    print(a[len(a)//2-1],a[len(a)//2])
else:
    print(a[len(a)//2])


# 27
a = list(map(int,input().split()))
l, r = map(int,input().split())
print(sorted(a[l:r+1])[-1])

# 28
a = list(map(int,input().split()))
l, r = map(int,input().split())
print(sorted(a[l:r+1])[0])

# 29
a = list(map(int,input().split()))
id = int(input())
if id<len(a):
    a.pop(id)

# 30
a = list(map(int,input().split()))
print(a==sorted(a))

# 31
a = list(map(int,input().split()))
x = int(input())
b = [i for j in range(x) for i in a]

# 32
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = sorted(a+b)
print(c)

# 33
a = list(map(int,input().split()))
x = int(input())
for i in range(len(a)):
    if a[i]==x:
        print(i,end=" ")

# 34
a = list(map(int,input().split()))
x = int(input())
print(a[x:] + a[:x])

# 35
a = [i for i in range(1,10)]

# 36
a = list(map(int,input().split()))
ans = 0
for i in a:
    ans += max(0,i)
print(ans)

# 37
a = list(map(int,input().split()))
ans = 0
for i in a:
    ans += min(0,i)
print(ans)

# 38
a = list(map(int,input().split()))
print(reversed(a)==a)

# 39
a = list(map(int,input().split()))
x = int(input())
b = []
for i in range(0,len(a),x):
    b.append(a[i:min(i+x,len(a))])

# 40
a = list(map(int,input().split()))
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)


