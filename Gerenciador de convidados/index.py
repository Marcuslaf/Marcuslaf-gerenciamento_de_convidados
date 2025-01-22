import random
import string

# Estrutura para armazenar os convidados
convidados = {"noivo": [], "noiva": []}

# Função para gerar um token único de 6 caracteres para o convidado
def gerar_token():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Função para cadastrar um convidado principal
def cadastrar_convidado(tipo, nome, cpf):
    tipo = tipo.lower()

    if tipo not in ["noivo", "noiva"]:
        print("Tipo inválido! Escolha 'noivo' ou 'noiva'.")
        return

    if cpf in [convidado["cpf"] for convidado in convidados["noivo"]] or cpf in [convidado["cpf"] for convidado in convidados["noiva"]]:
        print(f"O CPF {cpf} já está cadastrado no sistema.")
        return

    if len(convidados[tipo]) >= 10:
        print(f"Limite de 10 convidados principais atingido para o lado do {tipo}.")
        return

    token = gerar_token()
    while any(token.lower() == convidado["token"].lower() for lista in convidados.values() for convidado in lista):  # Garante tokens únicos
        token = gerar_token()

    convidados[tipo].append({
        "nome": nome,
        "cpf": cpf,
        "token": token,
        "dependentes": []
    })
    print(f"Convidado principal {nome} cadastrado com sucesso! Tipo: {tipo.capitalize()} | CPF: {cpf} | Token: {token}")

# Função para cadastrar dependentes de um convidado principal
def cadastrar_dependente(token_principal, nome_dependente):
    token_principal_normalizado = token_principal.strip().lower()
    
    for tipo in ["noivo", "noiva"]:
        for convidado in convidados[tipo]:
            if convidado["token"].lower() == token_principal_normalizado:
                if len(convidado["dependentes"]) >= 3:
                    print("Limite de 3 dependentes já foi atingido para este convidado.")
                    return
                
                token_dependente = f"{convidado['token']}-{len(convidado['dependentes']) + 1}"
                convidado["dependentes"].append({
                    "nome": nome_dependente,
                    "token": token_dependente
                })
                print(f"Dependente {nome_dependente} cadastrado com sucesso! Token: {token_dependente}")
                return
    
    print("Token do convidado principal não encontrado.")

# Função para listar convidados e seus dependentes
def listar_convidados():
    if not any(convidados["noivo"]) and not any(convidados["noiva"]):
        print("Nenhum convidado cadastrado.")
    else:
        print("\nConvidados do Noivo:")
        for convidado in convidados["noivo"]:
            print(f"Convidado Principal: {convidado['nome']} | CPF: {convidado['cpf']} | Token: {convidado['token']}")
            for i, dependente in enumerate(convidado["dependentes"], start=1):
                dependente["token"] = f"{convidado['token']}-{i}"
                print(f"  Dependente: {dependente['nome']} | Token: {dependente['token']}")
        
        print("\nConvidados da Noiva:")
        for convidado in convidados["noiva"]:
            print(f"Convidado Principal: {convidado['nome']} | CPF: {convidado['cpf']} | Token: {convidado['token']}")
            for i, dependente in enumerate(convidado["dependentes"], start=1):
                dependente["token"] = f"{convidado['token']}-{i}"
                print(f"  Dependente: {dependente['nome']} | Token: {dependente['token']}")

# Função para verificar a entrada
def verificar_entrada(token):
    token_normalizado = token.strip().lower()

    for tipo in ["noivo", "noiva"]:
        for convidado in convidados[tipo]:
            if convidado["token"].lower() == token_normalizado:
                print(f"Entrada autorizada. Nome: {convidado['nome']} (Convidado do {tipo.capitalize()})")
                return
            for dependente in convidado["dependentes"]:
                if dependente["token"].lower() == token_normalizado:
                    print(f"Entrada autorizada. Nome: {dependente['nome']} (Dependente do convidado principal {convidado['nome']})")
                    return
    print("Token não encontrado. Entrada não autorizada.")

# Função para remover convidado ou dependente
def remover_convidado_ou_dependente(token):
    token_normalizado = token.strip().lower()

    for tipo in ["noivo", "noiva"]:
        for convidado in convidados[tipo]:
            if convidado["token"].lower() == token_normalizado:
                convidados[tipo].remove(convidado)
                print(f"Convidado principal {convidado['nome']} removido com sucesso.")
                return
            for dependente in convidado["dependentes"]:
                if dependente["token"].lower() == token_normalizado:
                    convidado["dependentes"].remove(dependente)
                    print(f"Dependente {dependente['nome']} removido com sucesso.")
                    return
    print("Token não encontrado. Nenhuma remoção realizada.")

# Função para o menu
def menu():
    while True:
        print("\n1. Cadastrar convidado principal")
        print("2. Cadastrar dependente")
        print("3. Listar convidados e dependentes")
        print("4. Verificar entrada")
        print("5. Remover convidado ou dependente")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            tipo = input("Tipo (noivo/noiva): ").lower()
            nome = input("Nome do convidado principal: ")
            cpf = input("CPF do convidado principal: ")
            cadastrar_convidado(tipo, nome, cpf)
        elif escolha == '2':
            token_principal = input("Informe o token do convidado principal: ")
            nome_dependente = input("Nome do dependente: ")
            cadastrar_dependente(token_principal, nome_dependente)
        elif escolha == '3':
            listar_convidados()
        elif escolha == '4':
            token = input("Informe o token para verificar entrada: ")
            verificar_entrada(token)
        elif escolha == '5':
            token = input("Informe o token para remover: ")
            remover_convidado_ou_dependente(token)
        elif escolha == '6':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida.")

# Inicia o menu (chamamos a função menu)
menu()