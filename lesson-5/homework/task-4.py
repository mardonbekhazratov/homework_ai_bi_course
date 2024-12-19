def enrollment_stats(l) -> list:
    a = [[],[]]
    for i in l:
        a[0].append(i[1])
        a[1].append(i[2])
    return a

def mean(l: list) -> int:
    return None if len(l) == 0 else sum(l) / len(l)

def median(l: list) -> int:
    return None if len(l)==0 else sorted(l)[(len(l)-1)//2]

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

ls = enrollment_stats(universities)

print("******************************")
print(f"Total students: {sum(ls[0])}")
print(f"Total tuition: $ {sum(ls[1])}")
print()
print(f"Student mean: {mean(ls[0]) : .2f}")
print(f"Student median: {median(ls[0])}")
print()
print(f"Tuition mean: $ {mean(ls[1]) : .2f}")
print(f"Tuition median: $ {median(ls[1])}")
print("******************************")
