valores = [10, 9, 8]
print(list(filter(lambda a: a[1] > 0, enumerate(valores))))


""" (lambda a: a[1] > 0, enumerate(valores))
enumerate sempre retornará uma tupla, por exemplo: (indice, valor)
a[1] retorna a segunda posição da tupla, por exemplo: (indice, 1)
 """
