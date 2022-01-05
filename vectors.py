def get_int(description):
    try:
        return int(input(description))
    except ValueError:
        print("Valor inválido.")
        return get_int(description)

def get_float(description):
    try:
        return float(input(description))
    except ValueError:
        print("Valor inválido.")
        return get_float(description)

def get_ponto(letra, qtd_elementos):
    print("=== Preencha os valores do ponto {} ===\n".format(letra))
    ponto = []

    for i in range(qtd_elementos):
        ponto.append(get_float("Digite o valor da coordenada {}: ".format(
            i+1 if i >= 3 else chr(i + 120))))
    return ponto

def get_vector(size=0):
    if not size:
        size = 0
        while True:
            size = get_int("Digite o número de coordenadas do vetor: ")
            if size > 0:
                break
    vector = []
    print()
    for i in range(size):
        vector.append(get_int("Digite a coordenada {}: ".format(i+1)))
    return vector

def calculate_norm(vector):
    """
    Calcula a norma de um vetor
    """
    sum = 0
    for i in range(len(vector)):
        sum += vector[i]**2
    return [sum**(1/2), sum]

def inner_product(vector1, vector2):
    """
    Calcula o produto interno de dois vetores
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vetores de tamanhos diferentes")
    sum = 0
    for i in range(len(vector1)):
        sum += vector1[i] * vector2[i]
    return sum

def cross_product(v, w):
    """
    Calcula o produto vetorial de dois vetores
    """
    if len(v) != len(w):
        raise ValueError("Vetores de tamanhos diferentes")
    if len(v) != 3:
        raise ValueError("Vetores de tamanho diferente de 3")
    return [v[1]*w[2] - v[2]*w[1], v[2]*w[0] - v[0]*w[2], v[0]*w[1] - v[1]*w[0]]

def pv(n):
    print("\n=== Vetor {} ===".format(n))