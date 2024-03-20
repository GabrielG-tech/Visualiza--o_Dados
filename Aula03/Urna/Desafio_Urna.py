import os
import random

# tabela_votacao = [
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0]
#     ]

# Definindo os candidatos
candidatos = ['Candidato A', 'Candidato B', 'Candidato C']

# Função para gerar os votos aleatórios para cada turno
def gerar_votos():
    return [random.randint(1, 100) for _ in range(len(candidatos))]

# Função para escrever os resultados de um turno no arquivo
def escrever_resultados(arquivo, turno, votos):
    arquivo.write(f"Turno {turno}:\n")
    for candidato, voto in zip(candidatos, votos):
        arquivo.write(f"{candidato}: {voto} votos\n")
    arquivo.write("\n")

# Nome da pasta onde o arquivo será gerado
pasta_resultados = "Aula03\\Urna"

# Verifica se a pasta existe, senão a cria
if not os.path.exists(pasta_resultados):
    os.makedirs(pasta_resultados)

# Nome do arquivo de saída
nome_arquivo = os.path.join(pasta_resultados, "resultados_eleicao.txt")

# Gerando os resultados dos 5 turnos e escrevendo no arquivo
with open(nome_arquivo, 'w') as arquivo:
    for turno in range(1, 6):
        votos = gerar_votos()
        escrever_resultados(arquivo, turno, votos)

print(f"Arquivo '{nome_arquivo}' gerado com sucesso na pasta '{pasta_resultados}'.")

