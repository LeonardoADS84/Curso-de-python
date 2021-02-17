class NPC:  # classe pai
    def __init__(self, nome, time, forca, municao):  # consttutor com parametro de entrada
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True  # criado está proprietade porem não passado como parametro
        self.energia = 100

    def info(self):
        print("Nome.......:", self.nome)
        print("Time.......:", self.time)
        print("Força......:", self.forca)
        print("Munição....:", self.municao)
        print("Vivo.......:", ("Sim" if self.vivo else "Não"))
        print("Energia....:", self.energia)
        print("..........................")


class Soldado(NPC):  # classe filho, herançad
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)


class Guarda(NPC):  # classe filho, herança
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time, self.forca, self.municao)


class Elite(NPC):  # classe filho, herança
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome, time, self.forca, self.municao)
        # def inf(self):
        # super().info()


s1 = Guarda("Olho vivo", 1)
s2 = Soldado("Bala na agulha", 1)
s3 = Elite("Ninja", 1)
s4 = Guarda("Super Atento", 2)
s5 = Soldado("Tiro Certo", 2)
s6 = Elite("Samurai", 2)

s1.vivo = False
s6.vivo = False

s1.info()
s2.info()

s3.info()
s4.info()
s5.info()
s6.info()
