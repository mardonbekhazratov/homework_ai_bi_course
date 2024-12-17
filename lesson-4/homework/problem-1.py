list1 = map(int,input().split())
list2 = map(int,input().split())

ans = list()

for i in list1:
    if i not in list2:
        ans.append(i)

for i in list2:
    if i not in list1:
        ans.append(i)

print(ans)