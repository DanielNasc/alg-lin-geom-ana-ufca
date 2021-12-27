"""
Programa que calcula o ângulo entre dois vetores.
cos(a) = produto interno dos vetores / (norma do vetor1 * norma do vetor2)
"""

from sys import path
path.insert(1, '../')
from vectors import *

from math import acos, degrees
from fractions import Fraction

def main():
    pv(1)
    vetor1 = get_vector()
    pv(2)
    vetor2 = get_vector(len(vetor1))

    # Calcula o produto interno dos vetores.
    produto_interno = inner_product(vetor1, vetor2)

    # Calcula a norma dos vetores.
    norma_vetor1 = calculate_norm(vetor1)[0]
    norma_vetor2 = calculate_norm(vetor2)[0]

    # Calcula o ângulo entre os vetores.
    cos_angulo = produto_interno / (norma_vetor1 * norma_vetor2)
    # Fix IEEE 754
    angulo = degrees(acos(round(cos_angulo, 10)))

    print("\nO ângulo entre os vetores é: {:.2f}°".format(angulo))
    if (angulo):
        frac = Fraction(angulo/180).limit_denominator(180)
        print("O ângulo entre os vetores (em radianos) é: {}π{}"
                .format(frac.numerator if frac.numerator != 1 else '',
                        f"/{frac.denominator}" if frac.denominator != 1 else ''))
    else:
        print("O ângulo entre os vetores (em radianos) é: 0")

if __name__ == '__main__':
    main()