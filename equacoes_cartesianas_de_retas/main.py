from sys import path
path.insert(1, '../')
from vectors import *
from beauty_prints import equacao_reta

from simple_term_menu import TerminalMenu

def main():
    A = get_ponto('A', 2)

    print("\nQue informações você tem?")
    menu = TerminalMenu(['Com A e n', 'Com A e B', 'Sair'])
    opcao = menu.show()

    if opcao == 0:
        com_A_e_n(A)
    elif opcao == 1:
        com_A_e_B(A)
    else:
        print("\nSaindo...")

    return 0
    

def com_A_e_n(A):
    print("\n=== Vetor normal à reta ===")
    n = get_vector(2)

    print("\n> A equação da reta é dada por: r: ax + by + c = 0")
    print("> Com isso, temos: {}".format(equacao_reta(n[0], n[1], A)))

def com_A_e_B(A):
    B = get_ponto('B', 2)

    print("\n=== Vetor AB ===")
    v = []
    for i in range(2):
        v.append(B[i] - A[i])
    print(v, "\n")

    print("== Vetor normal à reta ===")
    n = [v[1] * -1, v[0]]
    print(n, "\n")
    
    print("> A equação da reta é dada por: r: ax + by + c = 0")
    print("> Com isso, temos: {}".format(equacao_reta(n[0], n[1], A)))

if __name__ == '__main__':
    main()
