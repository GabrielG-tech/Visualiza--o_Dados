#Cria ou abre o arquivo para escrita
with open('resultados_votacao.txt', 'w') as arquivo_txt:
    #Escreve o cabeçalho
    arquivo_txt.write("A \t B \tC \tBranco \tNulo\n")
     
    (...)

    #Escreve no arquivo de texto
    for i in range(0,10):
        linha = "{} \t {} \t {} \t {} \t {}\n".format(tabela_votacao[i][0],tabela_votacao[i][1], tabela_votacao[i][2], tabela_votacao[i][3], tabela_votacao[i][4])
        arquivo_txt.write(linha)