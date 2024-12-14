import random

def sorteio_mega_sena():
    numeros_sorteados = random.sample(range(1, 61), 6)
    return sorted(numeros_sorteados)

# Realizando o sorteio
resultado = sorteio_mega_sena()
print(f"Números sorteados:{resultado}")


