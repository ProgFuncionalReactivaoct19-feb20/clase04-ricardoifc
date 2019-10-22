"""
	@ricardoifc
	ejercicio1
"""
listaA = [10, 2, 3, 4]
listaB = ["a", "b", "c", "d"]

lista1 = (sorted(listaA))
lista2 = (sorted(listaB, reverse=True))
listaFinal = list(zip(lista1, lista2))
print(listaFinal)