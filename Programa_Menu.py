import os
carros=[]


class Carro:
    nome = ""
    pot = 0
    velMax = 0
    ligado = False

    def __init__(self, nome, pot):
        self.nome = nome
        self.pot = pot
        self.velMax = pot * 2
        self.ligado = False

    def ligado(self):
        self.ligado = True

    def desligado(self):
        self.desligado = False

    def info(self):
        print("Nome.............:", self.nome)
        print("Potência.........:", self.pot)
        print("Velocidade.......:", self.velMax)
        print("Ligado...........:", ("Sim" if self.ligado == True else "Não"))

    # essas funções(método)estão dentro do programa.


def Menu():
    os.system("cls") or None
    print("1 - Novo Carro ")
    print("2 - Informações do Carro ")
    print("3 - Excluir Carro ")
    print("4 - Ligar Carro ")
    print("5 - Desligar Carro ")
    print("6 - Listar  Carro ")
    print("7 - Sair ")
    print("Quantidade de carros: ", len(carros))
    opc = input("Digite uma opção: ")
    return opc


def NovoCarro():
    os.system("cls") or None
    n=input("Nome do carro......: ")
    p=input("Potência do carro..: ")
    car=Carro(n,p)
    carros.append(car)
    print("Novo carro criado")
    os.system("pause")


def informacao():
    os.system("cls") or None
    n = input("Informe o número do carro que deseja ver as informações: ")

    try:

        carros[int(n)].info()

    except:

        print("Carro não localizado")

    os.system("pause")


def excluirCarro():
    os.system("cls") or None
    n = input("Informe o número do carro que deseja excluir: ")

    try:

        del carros[int(n)]

    except:

        print("Carro não localizado")

    os.system("pause")


def ligarCarro():
    os.system("cls") or None
    n = input("Informe o número do carro que deseja ligar: ")

    try:

        carros[int(n)].ligar()
        print("Carro ligado")

    except:

        print("Carro não localizado")

    os.system("pause")


def desligarCarro():
    os.system("cls") or None
    n = input("Informe o número do carro que deseja Desligar: ")

    try:

        carros[int(n)].desligar()
        print("Carro desligado")


    except:

        print("Carro não localizado")

    os.system("pause")


def listarCarro():
    os.system("cls") or None

    p = 0

    for c in carros:
        print(str(p) + " - " + c.nome)

        p = p + 1

    os.system("pause")


ret=Menu()
while ret < "7":
    if ret=="1":
        NovoCarro()
    elif ret=="2":
        informacao()
    elif ret=="3":
        excluirCarro()
    elif ret=="4":
        ligarCarro()
    elif ret=="5":
        desligarCarro()
    elif ret=="6":
        listarCarro()
    ret=Menu()

os.system("cls") or None
print("Programa Finalizado")