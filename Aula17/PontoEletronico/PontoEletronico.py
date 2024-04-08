import sqlite3
import os
import re
import cv2 # pip install opencv-python

PATH = "Aula17/PontoEletronico"

def menu():
    print("\n" + "="*8 + " Sistema de Ponto " + "="*8)
    print("[1] - Incluir")
    print("[2] - Listar")
    print("[3] - Excluir")
    print("[4] - Atualizar")
    print("[5] - Sair")

def criar_tabela(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS funcionarios (id INTEGER PRIMARY KEY, nome TEXT, telefone TEXT, email TEXT, endereco TEXT, sexo TEXT, pix TEXT, horario_entrada TEXT, horario_saida TEXT, foto TEXT, cpf TEXT, dn TEXT, cartao TEXT, cargo TEXT)")

def inserir_funcionario(cursor, nome, telefone, email, endereco, sexo, pix, horario_entrada, horario_saida, foto, cpf, dn, cartao, cargo):
    cursor.execute("INSERT INTO funcionarios (nome, telefone, email, endereco, sexo, pix, horario_entrada, horario_saida, foto, cpf, dn, cartao, cargo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (nome, telefone, email, endereco, sexo, pix, horario_entrada, horario_saida, foto, cpf, dn, cartao, cargo))

def exibir_funcionarios(cursor):
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    for funcionario in funcionarios:
        print(f"Id: {funcionario[0]} Nome: {funcionario[1]} Cargo: {funcionario[13]} Horario Entrada: {funcionario[7]} Horario Saida: {funcionario[8]}")

def salvarFoto(nome):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro ao abrir a câmera.")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar o frame.")
            break
        cv2.imshow('Captura de Imagem', frame)
        key= cv2.waitKey(1)
        if key == ord('q'):
            break
    
    nome.rstrip().replace(" ","_")
    PATH_FOTO = PATH + '/fotos'
    caminho_imagem = os.path.join(PATH_FOTO, f'{nome}_foto.png')
    cv2.imwrite(caminho_imagem, frame)
    print(f"Imagem capturada e salva como '{nome}_foto.png'.")
    cap.release()
    cv2.destroyAllWindows()

    return f'{nome}_foto.png'

def incluir(cursor):
    nome = input("Nome: ")

    padrao = r'^\(\d{2}\)\d{5}-\d{4}$'
    telefone = ''
    while not re.match(padrao, telefone):
        telefone = input("Telefone: ")

    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    email = ''
    while not re.match(padrao, email):
        email = input("E-mail: ")

    endereco = input("Endereço: ")
    sexo = input("Sexo: ")
    pix = input("Pix: ")
    cargo = input("Cargo: ")

    padrao = r'^\d{2}\:\d{2}$'
    hi = ''
    while not re.match(padrao, hi):
        hi = input("Hora de entrada: ")

    ho = ''
    while not re.match(padrao, ho):
        ho = input("Hora de saída: ")

    print("Aperte \"q\" para tirar a foto.")
    foto = salvarFoto(nome)

    padrao = r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$'
    cpf = ''
    while not re.match(padrao, cpf):
        cpf = input("CPF: ")

    padrao = r'^\d{2}/\d{2}/\d{4}$'
    dn = ''
    while not re.match(padrao, dn):
        dn = input("Data de Nascimento: ")

    cartao = input("Cartão: ")

    inserir_funcionario(cursor, nome, telefone, email, endereco, sexo, pix, hi, ho, foto, cpf, dn, cartao, cargo)
    conn.commit()

def listar(cursor):
    print("\n======== Lista de Funcionarios ========")
    exibir_funcionarios(cursor)

def excluir(cursor):
    id_funcionario = input("Digite o ID do funcionário que deseja excluir: ")
    cursor.execute("DELETE FROM funcionarios WHERE id=?", (id_funcionario,))
    conn.commit()

def atualizar(cursor):
    id_funcionario = input("Escolha o ID a atualizar: ")
    print("===== CAMPO ATUALIZAR =====")
    print("[1] Nome")
    print("[2] Telefone")
    print("[3] Email")
    print("[4] Endereço")
    print("[5] Sexo")
    print("[6] Pix")
    print("[7] Hora de entrada")
    print("[8] Hora de saída")
    print("[9] CPF")
    print("[10] Data de Nascimento")
    print("[11] Cartão")
    print("[12] Foto")
    escolha_campo = input("Escolha a opção: ")

    novo_dado = input("Novo dado: ")

    campos = ['nome', 'telefone', 'email', 'endereco', 'sexo', 'pix', 'horario_entrada', 'horario_saida', 'cpf', 'dn', 'cartao', 'foto']
    campo_escolhido = campos[int(escolha_campo) - 1]

    cursor.execute(f"UPDATE funcionarios SET {campo_escolhido}=? WHERE id=?", (novo_dado, id_funcionario))
    conn.commit()

def validar_input_inteiro(mensagem):
    while True:
        try:
            entrada = int(input(mensagem))
            return entrada
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro existente nas opções.")

if not os.path.exists(PATH):
    os.makedirs(PATH)

conn = sqlite3.connect(f'{PATH}/banco.db')
cursor = conn.cursor()

criar_tabela(cursor)

cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()

# Caso o banco esteja vazio, crie 2 funcionários exemplo
if not funcionarios:
    inserir_funcionario(cursor, "Gabriel", "(21) 9 8765-1848", "gabriel@email.com", "Casa dos bobos nº0", "Masculino", "(21) 9 87645-1848", "13:00:00", "19:00:00", "imagem", "123.456.789-00", "11/07/2003", "123456789", "Estagiário de Desenvolvimento")
    inserir_funcionario(cursor, "Ronaldo", "(21) 9 8765-1848", "ronaldo@email.com", "Casa dos bobos nº2", "Masculino", "(21) 9 87645-1849", "10:30:00", "19:30:00", "imagem", "123.456.789-00", "15/08/1994", "123456799", "Analista")
    conn.commit()

while True:
    menu()
    escolha = validar_input_inteiro("Escolha uma opção: ")

    if escolha == 1:
        incluir(cursor)
    elif escolha == 2:
        listar(cursor)
    elif escolha == 3:
        excluir(cursor)
    elif escolha == 4:
        atualizar(cursor)
    elif escolha == 5:
        print("Fim do programa.")
        break
    else:
        print("Opção inválida!")

conn.close()
