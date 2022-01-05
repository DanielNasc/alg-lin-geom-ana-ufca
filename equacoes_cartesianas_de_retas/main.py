from sys import path
path.insert(1, '../')
from vectors import *

def main():
    A = get_ponto('A', 2)
    print("\n=== Vetor normal à reta ===")
    v = get_vector(2)

    print("\n> A equação da reta é dada por: r: ax + by + c = 0")
    print("> Com isso, temos: r: {}x + {}y + {} = 0"
            .format(A[0], A[1], -(A[0]*v[0] + A[1]*v[1])))

if __name__ == '__main__':
    main()
