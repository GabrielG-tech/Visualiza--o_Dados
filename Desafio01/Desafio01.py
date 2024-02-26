import math

# Define a função f(x) = x + 2
def f(x):
    return math.pow(math.e, -math.pow(x,2)/2)

# Define o intervalo e o passo
inicio = -5
fim = 5
passo = 0.1

# Cria ou abre o arquivo para escrita
with open('dados funcao.txt', 'w') as arquivo_txt:
    # Escreve o cabeçalho
    arquivo_txt.write("x \t f(x)\n")
    # Escreve os dados de x e f(x)

    x = inicio

    while x <= fim:
        y= f(x)
        linha = "{:.2f} \t {:.2f}\n".format(x, y)
        arquivo_txt.write(linha)
        x += passo

print("Arquivo de texto gerado com sucesso!")