import numpy as np

def main():
    a = np.array([
        [4,5,6],
        [3,-1,1],
        [2,1,-2]
    ])

    b = np.array([7,4,5])

    res = np.linalg.solve(a,b)
    print(f"x = {res[0]}")
    print(f"y = {res[1]}")
    print(f"z = {res[2]}")

if __name__=="__main__":
    main()