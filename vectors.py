def get_int(description):
    try:
        return int(input(description))
    except ValueError:
        print("Valor inválido.")
        return get_int(description)

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