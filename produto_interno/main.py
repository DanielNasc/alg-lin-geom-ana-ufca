"""
Programa que calcula o produto interno entre dois vetores.
"""
from sys import path
path.insert(1, '../')
from vectors import *

def main():
    print("=== Vetor 1 ===")
    vetor1 = get_vector()
    print("\n=== Vetor 2 ===")
    vetor2 = get_vector(len(vetor1))

    print(f'\nO produto interno entre os vetores é {inner_product(vetor1, vetor2)}')

if __name__ == '__main__':
    main()