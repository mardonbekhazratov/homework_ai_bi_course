# 1 - Union of Sets
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print(s1 | s2)

# 2 - Intersection of Sets
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print(s1 & s2)

# 3 - Difference of Sets
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print(s1 - s2)

# 4 - Check Subset
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print(s1 <= s2)

# 5 - Check Element
s = set(map(int, input().split()))
x = int(input())
print(x in s)

# 6 - Set Length
s = set(map(int, input().split()))
print(len(s))

# 7 - Convert List to Set
lst = list(map(int, input().split()))
print(set(lst))

# 8 - Remove Element
s = set(map(int, input().split()))
x = int(input())
s.discard(x)
print(s)

# 9 - Clear Set
s = set(map(int, input().split()))
s.clear()
print(s)

# 10 - Check if Set is Empty
s = set(map(int, input().split()))
print(len(s) == 0)

# 11 - Symmetric Difference
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print(s1 ^ s2)

# 12 - Add Element
s = set(map(int, input().split()))
x = int(input())
s.add(x)
print(s)

# 13 - Pop Element
s = set(map(int, input().split()))
print(s.pop() if s else None)

# 14 - Find Maximum
s = set(map(int, input().split()))
print(max(s))

# 15 - Find Minimum
s = set(map(int, input().split()))
print(min(s))

# 16 - Filter Even Numbers
s = set(map(int, input().split()))
print({x for x in s if x % 2 == 0})

# 17 - Filter Odd Numbers
s = set(map(int, input().split()))
print({x for x in s if x % 2 != 0})

# 18 - Create a Set of a Range
start, end = map(int, input().split())
print(set(range(start, end + 1)))

# 19 - Merge and Deduplicate
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
print(set(lst1 + lst2))

# 20 - Check Disjoint Sets
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print(s1.isdisjoint(s2))

# 21 - Remove Duplicates from a List
lst = list(map(int, input().split()))
print(list(set(lst)))

# 22 - Count Unique Elements
lst = list(map(int, input().split()))
print(len(set(lst)))

# 23 - Generate Random Set
import random
n, start, end = map(int, input().split())
print(set(random.randint(start, end) for _ in range(n)))
