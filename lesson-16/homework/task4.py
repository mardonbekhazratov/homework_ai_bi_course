import numpy as np

def main():
    a = np.array([
        [10,-2,3],
        [-2,8,-1],
        [3,-1,6]
    ])

    b = np.array([12,-5,15])

    res = np.linalg.solve(a,b)
    print(f"I1 = {res[0]}")
    print(f"I2 = {res[1]}")
    print(f"I3 = {res[2]}")

if __name__=="__main__":
    main()