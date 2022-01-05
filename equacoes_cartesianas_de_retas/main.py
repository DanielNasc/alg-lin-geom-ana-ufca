from sys import path, exit
path.insert(1, '../')
from vectors import *
from beauty_prints import equacao_reta, equacao_plano

from simple_term_menu import TerminalMenu

def main():

    # Usuario escolhe se quer a equação de uma reta ou de um plano.
    menu = TerminalMenu(['Reta', 'Plano'], title='O que deseja calcular?')
    escolha = menu.show()

    qtd_coordenadas = escolha + 2

    A = get_ponto('A', qtd_coordenadas)

    print("\nQue informações você tem?")
    menu = TerminalMenu(['A e n', 'A e B' if qtd_coordenadas == 2 else 'A, B e C' , 'Sair'])
    opcao = menu.show()

    if opcao == 0:
        com_A_e_n(A, qtd_coordenadas)
    elif opcao == 1:
        com_A_e_B(A, qtd_coordenadas)
    else:
        print("\nSaindo...")

    return 0
    

def com_A_e_n(A, qtd_c):
    print("\n=== Vetor normal à reta ===")
    n = get_vector(qtd_c)

    print("> {}".format(equacao_reta(n, A) if qtd_c == 2 else equacao_plano(n, A)))

def com_A_e_B(A, qtd_c):
    B = get_ponto('B', qtd_c)

    print("\n=== Vetor AB ===")
    v = []
    for i in range(qtd_c):
        v.append(B[i] - A[i])
    print(v, "\n")

    if qtd_c == 2:
        print("== Vetor normal à reta ===")
        n = [v[1] * -1, v[0]]
        print(n, "\n")
        
        print("> A equação da reta é dada por: r: ax + by + c = 0")
        print("> Com isso, temos: {}".format(equacao_reta(n[0], n[1], A)))
    else:
        C = get_ponto('C', qtd_c)
        
        pv("Vetor AC")
        w = []
        for i in range(qtd_c):
            w.append(C[i] - A[i])
        print(w, "\n")

        if (checar_se_sao_colineares(v, w)):
            print("Digite vetores não colineares")
            exit(1)

        pv("Vetor normal à reta")
        n = cross_product(v, w)
        print(n, "\n")

        print("> A equação do plano é dada por: p: ax + by + cz = 0")
        print("> Com isso, temos: {}".format(equacao_plano(n, A)))

if __name__ == '__main__':
    main()
