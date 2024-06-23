import sqlite3
import os
import re
import cv2  # pip install opencv-python
import time

PATH = "Aula17\\PontoEletronico"

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
        print(f"Id: {funcionario[0]} Nome: {funcionario[1]} Cartão: {funcionario[12]} Cargo: {funcionario[13]} Horário Entrada: {funcionario[7]} Horário Saída: {funcionario[8]}")

def salvar_foto(nome, cpf):
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
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    nome_foto = nome.replace(" ", "_")
    cpf_foto = cpf.replace(".", "_")
    PATH_FOTO = os.path.join(PATH, 'fotos')
    nome_arquivo = f'{nome_foto}_{cpf_foto}_foto.png'
    caminho_imagem = os.path.join(PATH_FOTO, nome_arquivo)
    cv2.imwrite(caminho_imagem, frame)
    print(f"Imagem capturada e salva como {nome_arquivo}.")
    cap.release()
    cv2.destroyAllWindows()

    return caminho_imagem

def incluir(cursor):
    nome = input("Nome: ").strip()

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

    cpf = input("CPF: ")

    padrao = r'^\d{2}/\d{2}/\d{4}$'
    dn = ''
    while not re.match(padrao, dn):
        dn = input("Data de Nascimento: ")

    print("Clique na janela e aperte \"q\" para tirar a foto.")
    foto = salvar_foto(nome, cpf)

    cartao = input("Cartão: ")

    inserir_funcionario(cursor, nome, telefone, email, endereco, sexo, pix, hi, ho, foto, cpf, dn, cartao, cargo)
    conn.commit()

def listar(cursor):
    print("\n======== Lista de Funcionários ========")
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

    if escolha_campo == "12":
        nome_funcionario = input("Nome do funcionário: ")
        cpf_funcionario = input("CPF do funcionário: ")
        nova_foto = salvar_foto(nome_funcionario, cpf_funcionario)  # Tira uma nova foto
        cursor.execute("UPDATE funcionarios SET foto=? WHERE id=?", (nova_foto, id_funcionario))
        print("Foto atualizada com sucesso.")
    else:
        novo_dado = input("Novo dado: ")

        campos = ['nome', 'telefone', 'email', 'endereco', 'sexo', 'pix', 'horario_entrada', 'horario_saida', 'cpf', 'dn', 'cartao', 'foto']
        campo_escolhido = campos[int(escolha_campo) - 1]

        cursor.execute(f"UPDATE funcionarios SET {campo_escolhido}=? WHERE id=?", (novo_dado, id_funcionario))
        print(f"{campo_escolhido.capitalize()} atualizado com sucesso.")

    conn.commit()

def registrar_ponto(cursor, cartao):
    cursor.execute("SELECT * FROM funcionarios WHERE cartao=?", (cartao,))
    funcionario_existente = cursor.fetchone()
    if funcionario_existente:
        foto_path = funcionario_existente[9]  # Índice 9 é onde o caminho da foto está armazenado
        print(foto_path)
        foto = cv2.imread(foto_path)  # Lê a foto
        if foto is not None:
            cv2.imshow('Foto do Funcionário', foto)  # Mostra a foto numa nova janela
            cv2.waitKey(5000)  # Espera 5 segundos
            cv2.destroyAllWindows()  # Fecha a janela
        else:
            print("Foto não encontrada.")
        print("Funcionário existente:")
        print(f"Nome: {funcionario_existente[1]}")
        print(f"CPF: {funcionario_existente[10]}")  # Índice 10 é onde o CPF está armazenado
        print(f"Horário de Entrada: {funcionario_existente[7]}")
        print(f"Data: {funcionario_existente[8]}")
    else:
        print("Cartão \033[1mnão\033[0m registrado!")

    
    # if funcionario:
    #     print(f"Ponto registrado para {funcionario[1]}")
    #     # Aqui você pode implementar a lógica para registrar o ponto (entrada/saída)
    # else:
    #     print("Funcionário não encontrado.")

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

# def add_funcionarios_exemplo():
#     # Caso o banco esteja vazio, crie 2 funcionários exemplo
#     if not funcionarios:
#         inserir_funcionario(cursor, "Gabriel", "(21) 9 8765-1848", "gabriel@email.com", "Casa dos bobos nº0", "Masculino", "(21) 9 87645-1848", "13:00:00", "19:00:00", "imagem", "123.456.789-00", "11/07/2003", "123456789", "Estagiário de Desenvolvimento")
#         inserir_funcionario(cursor, "Ronaldo", "(21) 9 8765-1848", "ronaldo@email.com", "Casa dos bobos nº2", "Masculino", "(21) 9 87645-1849", "10:30:00", "19:30:00", "imagem", "123.456.789-00", "15/08/1994", "123456799", "Analista")
#         conn.commit()

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
        registrar_ponto(cursor, str(escolha))
conn.close()
