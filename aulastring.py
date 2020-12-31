curso = "Curso de Python"
print(curso[9:15])
print(curso.strip())
print(curso.lower().strip())
print(curso.upper())
print(curso.replace("Python","P"))
a=curso.split(" ")
print(a[0])
print("Tamanho: " + str(len(curso)))

texto = "Curso de Python"
palavra = "Python"
res = palavra.upper() in texto.upper()
print(res)

#print(" Eu sou Leonardo tenho {} anos e nasci em {} ".format(36, 1984))
cidade = "cubatão"
dia = 24
mes = "julho"
ano = 1984
status = "{}, {} de {} de {} "
print(status.format(cidade,dia,mes,ano))


#res = " Java " in curso
#print(res)