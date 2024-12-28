# 1 - Get Value
d = eval(input())
key = input()
print(d.get(key, None))

# 2 - Check Key
d = eval(input())
key = input()
print(key in d)

# 3 - Count Keys
d = eval(input())
print(len(d))

# 4 - Get All Keys
d = eval(input())
print(list(d.keys()))

# 5 - Get All Values
d = eval(input())
print(list(d.values()))

# 6 - Merge Dictionaries
d1 = eval(input())
d2 = eval(input())
print({**d1, **d2})

# 7 - Remove Key
d = eval(input())
key = input()
d.pop(key, None)
print(d)

# 8 - Clear Dictionary
d = eval(input())
d.clear()
print(d)

# 9 - Check if Dictionary is Empty
d = eval(input())
print(len(d) == 0)

# 10 - Get Key-Value Pair
d = eval(input())
key = input()
print((key, d[key]) if key in d else None)

# 11 - Update Value
d = eval(input())
key = input()
value = input()
d[key] = value
print(d)

# 12 - Count Value Occurrences
d = eval(input())
value = input()
print(list(d.values()).count(value))

# 13 - Invert Dictionary
d = eval(input())
print({v: k for k, v in d.items()})

# 14 - Find Keys with Value
d = eval(input())
value = input()
print([k for k, v in d.items() if v == value])

# 15 - Create a Dictionary from Lists
keys = input().split()
values = input().split()
print(dict(zip(keys, values)))

# 16 - Check for Nested Dictionaries
d = eval(input())
print(any(isinstance(v, dict) for v in d.values()))

# 17 - Get Nested Value
d = eval(input())
outer_key = input()
inner_key = input()
print(d.get(outer_key, {}).get(inner_key, None))

# 18 - Create Default Dictionary
from collections import defaultdict
default_value = input()
d = defaultdict(lambda: default_value)
print(d)

# 19 - Count Unique Values
d = eval(input())
print(len(set(d.values())))

# 20 - Sort Dictionary by Key
d = eval(input())
print(dict(sorted(d.items())))

# 21 - Sort Dictionary by Value
d = eval(input())
print(dict(sorted(d.items(), key=lambda item: item[1])))

# 22 - Filter by Value
d = eval(input())
threshold = int(input())
print({k: v for k, v in d.items() if v > threshold})

# 23 - Check for Common Keys
d1 = eval(input())
d2 = eval(input())
print(not d1.keys().isdisjoint(d2.keys()))

# 24 - Create Dictionary from Tuple
t = eval(input())
print(dict(t))

# 25 - Get the First Key-Value Pair
d = eval(input())
print(next(iter(d.items()), None))
