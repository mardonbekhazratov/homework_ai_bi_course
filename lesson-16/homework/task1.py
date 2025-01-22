import numpy as np

def C(F):
    return (F-32)*5/9

def main():
    v = np.array([32, 68, 100, 212, 77])
    vfunc = np.vectorize(C)
    print(vfunc(v))

if __name__=="__main__":
    main()