# 3 - Min Element
t = tuple(map(int, input().split()))
print(min(t))

# 4 - Check Element
t = tuple(map(int, input().split()))
x = int(input())
print(x in t)

# 5 - First Element
t = tuple(map(int, input().split()))
print(t[0] if t else None)

# 6 - Last Element
t = tuple(map(int, input().split()))
print(t[-1] if t else None)

# 7 - Tuple Length
t = tuple(map(int, input().split()))
print(len(t))

# 8 - Slice Tuple
t = tuple(map(int, input().split()))
print(t[:3])

# 9 - Concatenate Tuples
t1 = tuple(map(int, input().split()))
t2 = tuple(map(int, input().split()))
print(t1 + t2)

# 10 - Check if Tuple is Empty
t = tuple(map(int, input().split()))
print(len(t) == 0)

# 11 - Get All Indices of Element
t = tuple(map(int, input().split()))
x = int(input())
print([i for i, v in enumerate(t) if v == x])

# 12 - Find Second Largest
t = tuple(map(int, input().split()))
print(sorted(set(t))[-2] if len(set(t)) > 1 else None)

# 13 - Find Second Smallest
t = tuple(map(int, input().split()))
print(sorted(set(t))[1] if len(set(t)) > 1 else None)

# 14 - Create a Single Element Tuple
x = int(input())
print((x,))

# 15 - Convert List to Tuple
lst = list(map(int, input().split()))
print(tuple(lst))

# 16 - Check if Tuple is Sorted
t = tuple(map(int, input().split()))
print(t == tuple(sorted(t)))

# 17 - Find Maximum of Subtuple
t = tuple(map(int, input().split()))
start, end = map(int, input().split())
print(max(t[start:end+1]))

# 18 - Find Minimum of Subtuple
t = tuple(map(int, input().split()))
start, end = map(int, input().split())
print(min(t[start:end+1]))

# 19 - Remove Element by Value
t = tuple(map(int, input().split()))
x = int(input())
print(tuple(v for i, v in enumerate(t) if i != t.index(x)) if x in t else t)

# 20 - Create Nested Tuple
t = tuple(map(int, input().split()))
indices = list(map(int, input().split()))
print(tuple(t[i] for i in indices))

# 21 - Repeat Elements
t = tuple(map(int, input().split()))
n = int(input())
print(tuple(v for v in t for _ in range(n)))

# 22 - Create Range Tuple
start, end = map(int, input().split())
print(tuple(range(start, end + 1)))

# 23 - Reverse Tuple
t = tuple(map(int, input().split()))
print(t[::-1])

# 24 - Check Palindrome
t = tuple(map(int, input().split()))
print(t == t[::-1])

# 25 - Get Unique Elements
t = tuple(map(int, input().split()))
seen = set()
print(tuple(v for v in t if v not in seen and not seen.add(v)))
