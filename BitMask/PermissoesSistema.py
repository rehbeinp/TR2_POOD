"""Existem diversos exemplos de uso do Bitmask na prática. Um deles é na representação de 
permissões de acesso em sistemas de controle de acesso. Cada permissão é representada por 
um bit, e a combinação de diferentes permissões é realizada através de operações lógicas com os bits.
"""

def verifica(x:int, j:int ):
    if x&(1<<j):
        return True
    else:
        return False
    
def liga(x:int, j:int):
    x|=(1<<j)
    return x

def desliga(x:int, j:int):
    x = x&~(1<<j)
    return x

def darPermissao(usuario,lista, permissoes= {"READ":0,"WRITE ": 1,"EXEC":2, "SHARE":3,"DELETE":4,"ADMIN":5}):
    totalPermissoes = encontrarValor(usuario, lista)
    for chave, valor in permissoes.items():
        op = input(f"Deseja adicionar a permissão {chave} ao {usuario}: (s/n)")
        if(op=="s" or op=="S"):
            totalPermissoes=liga(totalPermissoes, valor)
    return totalPermissoes

def encontrarValor(valor, lista):
    for elem in lista:
        if(elem[0] == valor):
            return elem[1]
    return False

def removerPermissoes(usuario,lista,permissoes= {"READ":0,"WRITE": 1,"EXEC":2, "SHARE":3,"DELETE":4,"ADMIN":5}):
    totalPermissoes = encontrarValor(usuario, lista)
    for chave, valor in permissoes.items():
        op = input(f"Deseja remover a permissão {chave} ao {usuario}: (s/n)")
        if(op=="s" or op=="S"):
            totalPermissoes=desliga(totalPermissoes, valor)
    return totalPermissoes

permissoes = {"READ":1,"WRITE ": 2,"EXEC":4,
              "SHARE":8,"DELETE":16,"ADMIN":32}

usuarios = list()
while(True):
    op=int(input("""O que deseja fazer?
             1 - encerrar
             2 - ver permissões
             3 - dar permissão
             4 - remover permissão
             5 - adicionar usuário e permições
             Opção: """))
    if(op==1): break
    elif(op==5):
        usuario = input("Inoforme o nome do user: ").upper()
        permissoesUsuario = darPermissao(usuario, usuarios)
        usuarios.append([usuario, permissoesUsuario])
        for elem in usuarios:
            print(elem[0], " -- ", elem[1])

    elif(op==2):
        nome = input("Informe o nome do user: ").upper()
        numPermissao=encontrarValor(nome, usuarios)
        if(numPermissao==0): print("User sem premissões. ")
        elif(numPermissao):
            print("O usuario tem a permissão: ")
            for chave, valor in permissoes.items():
                for i in range(6):
                    if(verifica(numPermissao, i) & verifica(valor, i)):
                        print(chave)
        else: print("Nome não encontrado ;-; ")
            
    elif(op==3):
        nome = input("Informe o nome do user: ").upper()
        numPermissao=encontrarValor(nome, usuarios)

        if(numPermissao is not False):
            permissoesUsuario = darPermissao(nome,usuarios)
            usuarios.remove([nome, numPermissao])
            usuarios.append([nome, permissoesUsuario])
            print("Permissões concedidas. ")
        else: print("--------")

    elif(op==4):
        nome = input("Informe o nome do user: ").upper()
        numPermissao=encontrarValor(nome, usuarios)
        if(numPermissao==0): print("Usuário não tem permissões.")
        elif(numPermissao):
            permissoesUsuario = removerPermissoes(nome,usuarios)
            usuarios.remove([nome, numPermissao])
            usuarios.append([nome, permissoesUsuario])
            print("Permissões retiradas. ")