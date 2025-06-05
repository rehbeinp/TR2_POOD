import random

#classe que inicia um novo objeto que tem um valor, um galho direito e um galho esquerdo
class NoDaArvore:
    def __init__(self, item=0):
        self.valor = item
        self.esquerda, self.direita = None, None

raiz = NoDaArvore()
raiz = None


def inserir(valor):
    global raiz          #chama a variavel global para passar como parametro
    raiz = inserirGalho(raiz, valor)


def inserirGalho(raiz, valor):

    if raiz == None:              #verifica se raiz guarda algum dado ou não
        raiz = NoDaArvore(valor)  # raiz recebe uma nova instância da classe NoDaArvore
        return raiz               #recebendo um galho direito e esquerdo e retornando uma nova raiz


    #se a raiz tem umdado maior que o dado da variável valor, então o galho esquerdo de raiz 
    # recebe uma nova instância da classe NoDaArvore, guardando o dado da
    # variável valor e recebendo um galho direito e esquerdo
    if valor < raiz.valor:
        raiz.esquerda = inserirGalho(raiz.esquerda, valor)  


    #caso o dado da raiz não for maior que o dado da variável valor, então o galho direito de 
    # raiz recebe uma nova instância da classe NoDaArvore, guardando o dado da variável valor e 
    # recebendo um galho direito e esquerdo
    elif valor > raiz.valor:
        raiz.direita = inserirGalho(raiz.direita, valor)

    return raiz           #retorna uma nova raiz


#mostraEmOrdem se chama recursivamente até chegar na folha mais à esquerda da árvore binária, 
# que terá necessáriamente o galho esquerdo nulo, fazendo com que comece a ser mostrado no console 
# os valores das folhas
def mostraEmOrdem(raiz):
    if raiz != None:
        mostraEmOrdem(raiz.esquerda)
        print(raiz.valor)
        mostraEmOrdem(raiz.direita)


def arvore(arr):
    for i in range(len(arr)):
        inserir(arr[i])



tamanho = int(input("Informe o tamanho do array para ordenação: "))
arr = [random.randint(1, 100+tamanho) for _ in range(tamanho)]
print("Seu array inicial: ")
for i in range(len(arr)):
        print(arr[i])

print("Seu array ordenado: ")
arvore(arr)
mostraEmOrdem(raiz)



