import sqlite3
import os
import time

def formatarTitulo(texto):
    """Função responsável por formatar o título dos menus

    Args:
        texto (string): Texto original (feio)

    Returns:
        string: Texto formatado (bonito)
    """
    return ("\n"+ "=" * (len(texto) + 16)) + "\n\t" + texto + "\n" + ("=" * (len(texto) + 16) + "\n")

def introducaoPrograma():
    print(formatarTitulo("Gerenciamento de Visitantes") + "\nInsira a opção desejada: \n\n[1] Cadastrar \n[2] Listar \n[3] Atualizar Dados \n[4] Excluir \n[5] Sair\n")
    while (True):
        try:
            opcaoEscolhida = int(input("> "))
            break
        except (ValueError):
            print("ERRO: Apenas números, por gentileza.")
    return opcaoEscolhida

def cadastroVisitante():
    #Cadastrar  
            print(formatarTitulo("Cadastrar"))
            #Nome
            nomeVisitante = input("Nome: ")
            #telefone
            telefoneVisitante = input("Telefone: ")
            #email
            emailVisitante = input("E-Mail: ")
            #idade
            while (True): 
                try:
                    idadeVisitante = int(input("Idade: "))
                    break
                except (ValueError):
                    print("ERRO: Apenas números, por favor.")
            #sexo
            while (True):
                sexoVisitante = input("Sexo (m/f): ").upper()
                if (len(sexoVisitante) > 1 and (sexoVisitante != "M" or sexoVisitante != "F")):
                    print("ERRO: Apenas \"M\" ou \"F\"")
                else: 
                    break
            #data de agendamento
            dataAgendamentoVisita = input("Data de Agendamento: ")
            #especialidade
            especialidadeVisitante = input("Especialidade: ")

            #Cadastrar na tabela
            cursor.execute("INSERT INTO visitantes (nome, telefone, email, idade, sexo, data_agendamento, especialidade) VALUES (?, ?, ?, ?, ?, ?, ?)", (nomeVisitante, telefoneVisitante, emailVisitante, idadeVisitante, sexoVisitante, dataAgendamentoVisita, especialidadeVisitante))
            opcaoEscolhida = 0
            conn.commit()
            print("\nOs dados foram cadastrados com sucesso!")
            time.sleep(1.5)

def listarVisitantes(): 
    print(formatarTitulo("Listar Visitantes"))
    #Checar o número de registros
    cursor.execute("SELECT COUNT(*) FROM visitantes")
    numeroDeRegistros = cursor.fetchone()[0]
    #Verificar se o sistema tem, pelo menos, um registro
    if numeroDeRegistros == 0:
        print("ERRO: Não há registros disponíveis!")
    else: 
        cursor.execute("SELECT * FROM visitantes")
        visitantes = cursor.fetchall()

        #Imprimir visitantes
        for v in visitantes:
            print("Id: {} \nNome: {} \nTelefone: {} \nE-Mail: {} \nIdade: {} \nSexo: {} \nData de Agendamento: {} \nEspecialidade: {}\n".format(v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7]))

    time.sleep(1.5)

def removerVisitante():
    print(formatarTitulo("Excluir"))
    #Checar o número de registros
    cursor.execute("SELECT COUNT(*) FROM visitantes")
    numeroDeRegistros = cursor.fetchone()[0]
    #Verificar se o sistema tem, pelo menos, um registro
    if numeroDeRegistros == 0:
        print("ERRO: Não há registros disponíveis!")
    else: 
        #Input do ID 
        print("Insira o ID do registro de visitante que você deseja remover: \n")
        while (True): 
            try:
                idVisitante = int(input("> "))
                break
            except (ValueError):
                print("ERRO: Apenas números, por favor.")
        if (idVisitante > numeroDeRegistros):
            #Mensagem de erro, caso o ID seja inválido
            print("ERRO: ID inválido.")
        else: 
            #Realizar a exclusão, caso o ID seja válido
            print(idVisitante)
            cursor.execute("DELETE FROM visitantes WHERE id=?",(str(idVisitante)))
            print("\nRegistro do visitante #{} excluído com sucesso!".format(idVisitante))
        conn.commit()
        time.sleep(1.5)

def modificarVisitante():
    print(formatarTitulo("Modificar"))
    #Checar o número de registros
    cursor.execute("SELECT COUNT(*) FROM visitantes")
    numeroDeRegistros = cursor.fetchone()[0]
    #Verificar se o sistema tem, pelo menos, um registro
    if numeroDeRegistros == 0:
        print("ERRO: Não há registros disponíveis!")
    else: 
        #Input do ID 
        print("Insira o ID do registro de visitante que você deseja modificar: \n")
        while (True): 
            try:
                idVisitante = int(input("> "))
                break
            except (ValueError):
                print("ERRO: Apenas números, por favor.")
        if (idVisitante > numeroDeRegistros):
            #Mensagem de erro, caso o ID seja inválido
            print("ERRO: ID inválido.")
        else: 
            #Input do que o usuário deseja modificar
            print("O que deseja modificar? \n\n[1] Nome \n[2] Telefone \n[3] E-Mail \n[4] Idade \n[5] Sexo \n[6] Data de Agendamento \n[7] Especialidade \n[8] Cancelar \n")

            while (True): 
                try:
                    escolhaModificacao = int(input("> " ))
                    #Checar se o usuário inseriu um número entre 1 e 8
                    if (0 < escolhaModificacao < 9):
                        break
                    else: 
                        print("\nERRO: Apenas números entre 1 e 8, por gentileza.")
                except (ValueError):
                    print("\nERRO: Apenas números, por favor.")

            #Modificação de...
            if escolhaModificacao == 1:
                #...nome
                novoNomeVisitante = input("Novo nome: ")
                cursor.execute("UPDATE visitantes SET nome=? WHERE id=?",(novoNomeVisitante,idVisitante))
                print("\nNome do visitante #{} modificado com sucesso!".format(idVisitante))
            elif escolhaModificacao == 2:
                #...telefone
                novoTelefoneVisitante = input("Novo telefone: ")
                cursor.execute("UPDATE visitantes SET telefone=? WHERE id=?",(novoTelefoneVisitante,idVisitante))
                print("\nTelefone do visitante #{} modificado com sucesso!".format(idVisitante))
            elif escolhaModificacao == 3:
                #...email
                novoEmailVisitante = input("Novo E-Mail: ")
                cursor.execute("UPDATE visitantes SET email=? WHERE id=?",(idVisitante,novoEmailVisitante))
                print("\nE-Mail do visitante #{} modificado com sucesso!".format(idVisitante))
            elif escolhaModificacao == 4:
                #...idade
                while (True):
                    try:
                        novaIdadeVisitante = input("Nova idade: ")
                        break
                    except (ValueError):
                        print("\nERRO: Apenas números, por favor.")
                cursor.execute("UPDATE visitantes SET idade=? WHERE id=?",(idVisitante,novaIdadeVisitante))
                print("\nIdade do visitante #{} modificado com sucesso!".format(idVisitante))
            elif escolhaModificacao == 5:
                #...sexo (eita bicho)
                while (True):
                    novoSexoVisitante = input("Novo sexo (m/f): ").upper()
                    if len(novoSexoVisitante) > 1:
                        print("\nERRO: Apenas \"m\" ou \"f\", por gentileza.")
                    else: 
                        break
                cursor.execute("UPDATE visitantes SET sexo=? WHERE id=?",(novoSexoVisitante, idVisitante))
                print("\nSexo do visitante #{} modificado com sucesso!".format(idVisitante))
            elif escolhaModificacao == 6:
                #...data de agendamento
                novaDataAgendamentoVisitante = input("Nova data de agendamento: ")
                cursor.execute("UPDATE visitantes SET dataAgendamento=? WHERE id=?",(novaDataAgendamentoVisitante, idVisitante))
                print("\nData de agendamento do visitante #{} modificado com sucesso!".format(idVisitante))
            elif escolhaModificacao == 7:
                #...especialidade
                novaEspecialidadeVisitante = input("Nova especialidade: ")
                cursor.execute("UPDATE visitantes SET especialidade=? WHERE id=?",(novaEspecialidadeVisitante, idVisitante))
                print("\nEspecialidade do visitante #{} modificado com sucesso!".format(idVisitante))
            elif escolhaModificacao == 8:
                #CANCELAR
                pass
        conn.commit()
        time.sleep(1.5)

# Nome da pasta onde o arquivo será gerado
pasta_resultados = "C:\\Users\\gabriel.gsouza\\Documents\\Visualização_Dados\\Aula13"

# Verifica se a pasta existe, senão a cria
if not os.path.exists(pasta_resultados):
    os.makedirs(pasta_resultados)

# Nome do arquivo de saída
nome_arquivo = os.path.join(pasta_resultados, "visitantes.db")

opcaoEscolhida = 0

#Preparar banco de dados
conn = sqlite3.connect(nome_arquivo)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS visitantes(id INTEGER PRIMARY KEY, nome VARCHAR(30), telefone VARCHAR(30), email VARCHAR(30), idade INTEGER, sexo VARCHAR(1), data_agendamento VARCHAR(10), especialidade VARCHAR(30))")

while (True):
    match (opcaoEscolhida):
        case 0:
            #Introdução
            opcaoEscolhida = introducaoPrograma()
        case 1:
            #Cadastrar
            cadastroVisitante()
            opcaoEscolhida = 0
        case 2:
            #Listar
            listarVisitantes()
            opcaoEscolhida = 0
        case 3:
            #Modificar
            modificarVisitante()
            opcaoEscolhida = 0
        case 4:
            #Excluir
            removerVisitante()
            opcaoEscolhida = 0  
        case 5:
            #Sair
            break
        case _:
            print("Erro: Opção inválida!")
            time.sleep(1.5)
            opcaoEscolhida = 0