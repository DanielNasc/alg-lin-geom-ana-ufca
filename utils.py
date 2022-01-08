import numpy as np
from simple_term_menu import TerminalMenu

def reta_ou_plano():
    menu = TerminalMenu(['Reta', 'Plano'], title='O que deseja calcular?')
    escolha = menu.show()
    return escolha + 2

def calculate_det(matrix):
    return round(np.linalg.det(matrix), 10)