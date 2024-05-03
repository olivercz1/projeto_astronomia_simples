# Importando a biblioteca para calcular a distância entre os planetas e o Sol
from scipy.constants import astronomical_unit

# Criando um dicionário com informações sobre os planetas
planetas = {
    "Mercúrio": {"distancia_media_ao_sol": 0.39, "diametro": 4879},
    "Vênus": {"distancia_media_ao_sol": 0.72, "diametro": 12104},
    "Terra": {"distancia_media_ao_sol": 1.00, "diametro": 12742},
    "Marte": {"distancia_media_ao_sol": 1.52, "diametro": 6779},
    "Júpiter": {"distancia_media_ao_sol": 5.20, "diametro": 139820},
    "Saturno": {"distancia_media_ao_sol": 9.58, "diametro": 116460},
    "Urano": {"distancia_media_ao_sol": 19.18, "diametro": 50724},
    "Netuno": {"distancia_media_ao_sol": 30.06, "diametro": 49244}
}

# Função para calcular a distância em km
def calcular_distancia_km(distancia_ao_sol):
    return distancia_ao_sol * astronomical_unit / 1000

# Função para mostrar informações sobre um planeta
def mostrar_informacoes(planeta):
    distancia_km = calcular_distancia_km(planetas[planeta]["distancia_media_ao_sol"])
    diametro = planetas[planeta]["diametro"]
    print(f"Planeta: {planeta}")
    print(f"Distância média ao Sol: {distancia_km:.2f} km")
    print(f"Diâmetro: {diametro} km")

# Menu para o usuário
def menu():
    print("Bem-vindo ao programa de informações sobre planetas!")
    print("Escolha um planeta para obter informações:")
    for index, planeta in enumerate(planetas.keys()):
        print(f"{index + 1}. {planeta}")
    escolha = int(input("Digite o número correspondente ao planeta desejado: "))
    if escolha > 0 and escolha <= len(planetas):
        planeta_escolhido = list(planetas.keys())[escolha - 1]
        mostrar_informacoes(planeta_escolhido)
    else:
        print("Escolha inválida. Por favor, tente novamente.")

# Execução do programa
if __name__ == "__main__":
    menu()
1




