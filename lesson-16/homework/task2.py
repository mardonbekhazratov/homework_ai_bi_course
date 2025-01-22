import numpy as np

def custom(a,b):
    return a**b

def main():
    v1 = np.array([2, 3, 4, 5])
    v2 = np.array([1, 2, 3, 4])
    func = np.vectorize(custom)
    result = func(v1,v2)
    print(result)


if __name__=="__main__":
    main()