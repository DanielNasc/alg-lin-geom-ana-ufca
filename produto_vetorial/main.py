"""
    Sejam v e w vetores de R^3 e ex um vetor da Base Canônica no R^3 {e1, e2, e3}, com x = 1, 2 ou 3.
    v ∧ w = (det[e1, v, w], det[e2, v, w], det[e3, v, w])
    Outra definição:
    v ∧ w = ((v1*w2) - (v2*w1), (v2*w3) - (v3*w2), (v3*w1) - (v1*w3))
"""

from sys import path
path.insert(1, '../')
from vectors import *

def main():
    pv(1)
    v = get_vector(3)
    pv(2)
    w = get_vector(3)

    cp = cross_product(v, w)
    print("\nv ∧ w: {}".format(cp))

if __name__ == '__main__':
    main()