carros = ["Fusion", "Gol", "Uno", "Opala"]
itCarros = iter(carros)

while itCarros:

    try:

        print(next(itCarros))
    except StopIteration:
        print("Lista finalizada")
        break