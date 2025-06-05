def verifica(x: int, j: int) -> bool:
    return (x & (1 << j)) != 0

def liga(x: int, j: int) -> int:
    return x | (1 << j)

def desliga(x: int, j: int) -> int:
    return x & ~(1 << j)

PERMISSOES = {
    "READ": 0,
    "WRITE": 1,
    "EXEC": 2,
    "SHARE": 3,
    "DELETE": 4,
    "ADMIN": 5
}

usuarios = {}

def dar_permissao(usuario: str, permissao_atual: int) -> int:
    for nome, bit in PERMISSOES.items():
        op = input(f"Deseja adicionar a permissão {nome} ao usuário {usuario}? (s/n): ").strip().lower()
        if op == "s":
            permissao_atual = liga(permissao_atual, bit)
    return permissao_atual

def remover_permissao(usuario: str, permissao_atual: int) -> int:
    for nome, bit in PERMISSOES.items():
        op = input(f"Deseja remover a permissão {nome} do usuário {usuario}? (s/n): ").strip().lower()
        if op == "s":
            permissao_atual = desliga(permissao_atual, bit)
    return permissao_atual

def mostrar_permissoes(usuario: str, valor: int):
    print(f"Permissões de {usuario}:")
    for nome, bit in PERMISSOES.items():
        if verifica(valor, bit):
            print(f"- {nome}")

while True:
    try:
        op = int(input("""
O que deseja fazer?
1 - Encerrar
2 - Ver permissões
3 - Dar permissões
4 - Remover permissões
5 - Adicionar usuário e permissões
Opção: """).strip())
    except ValueError:
        print("Entrada inválida.")
        continue

    if op == 1:
        break

    elif op == 5:
        nome = input("Informe o nome do usuário: ").strip().upper()
        if nome in usuarios:
            print("Usuário já existe.")
        else:
            usuarios[nome] = dar_permissao(nome, 0)

    elif op == 2:
        nome = input("Informe o nome do usuário: ").strip().upper()
        if nome in usuarios:
            if usuarios[nome] == 0:
                print("Usuário sem permissões.")
            else:
                mostrar_permissoes(nome, usuarios[nome])
        else:
            print("Usuário não encontrado.")

    elif op == 3:
        nome = input("Informe o nome do usuário: ").strip().upper()
        if nome in usuarios:
            usuarios[nome] = dar_permissao(nome, usuarios[nome])
            print("Permissões concedidas.")
        else:
            print("Usuário não encontrado.")

    elif op == 4:
        nome = input("Informe o nome do usuário: ").strip().upper()
        if nome in usuarios:
            usuarios[nome] = remover_permissao(nome, usuarios[nome])
            print("Permissões removidas.")
        else:
            print("Usuário não encontrado.")

    else:
        print("Opção inválida.")
