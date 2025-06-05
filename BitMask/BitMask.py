def verifica(x:int, j:int ):  #verifica se o bit está ligado
    if x&(1<<j):
        return True
    else:
        return False
    
def liga(x:int, j:int):      #liga  o bit
    x|=(1<<j)
    return x

def desliga(x:int, j:int):    #desliga  o bit
    x = x&~(1<<j)
    return x

def flip(x:int, j:int):      #liga se estiver desligado e desliga se estiver ligado 
    x^=(1<<j)
    return x

def lbs(x:int):  # mostra o bit menos significativo   least significant bit
    x = x&(-x)
    return x

while(True):
    print("""Menu:
        1 - Verificar bit
        2 - Ligar bit
        3 - Desligar bit
        4 - Ligar bit se desligado e desligar se ligado
        5 - Ver bit menos significativo
        0 - Sair
        """)

    op:int = int(input("Opção: "))
    if op==0: break


    numero = int(input("Informe o número: "))
    indice_bit = int(input("Informe o índice do bit: "))

    if op == 1:
        if verifica(numero,indice_bit):
            print("Bit ativo")
        else: print("Bit desligado")

    elif op==2:
        retorno = liga(numero,indice_bit)
        print(f"Número atualizado: {retorno}.")

    elif op==3:
        retorno = desliga(numero,indice_bit)
        print(f"Número atualizado: {retorno}.")

    elif op==4:
        retorno = flip(numero,indice_bit)
        print(f"Número atualizado: {retorno}.")

    elif op==5:
        retorno = lbs(numero)
        print(f"Bit menos significativo: {retorno}.")