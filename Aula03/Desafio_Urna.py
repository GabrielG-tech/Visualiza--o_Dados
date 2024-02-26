import os

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

# # Resultados da votação
# resultados = {
#     "Candidato A": 150,
#     "Candidato B": 200,
#     "Candidato C": 100
# }


# # Nome do arquivo para salvar os resultados
# nome_arquivo = "resultados_votacao.txt"

# # Caminho para a pasta onde deseja criar o arquivo
# caminho_pasta = "Aula03"

# # Verifica se o caminho da pasta existe, se não, cria a pasta
# if not os.path.exists(caminho_pasta):
#     os.makedirs(caminho_pasta)

# # Caminho completo para o arquivo
# caminho_completo = os.path.join(caminho_pasta, nome_arquivo)

# # Abrir o arquivo em modo de escrita
# with open(caminho_completo, "w") as arquivo:
#     for candidato, votos in resultados.items():
#         arquivo.write(f"{candidato}: {votos} votos\n")

# =================
        
import os
import random

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
pasta_resultados = "Aula03"

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

