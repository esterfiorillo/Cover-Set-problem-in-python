import numpy as np 

def proximo_set(A, x, c, point): #seleciona o proximo set a ser adicionado na cobertura testada

	sets_lin = A[point,:]

	#lista com numero de sets que cobrem o ponto
	num_set = [i if sets_lin[i]==1 else None for i in range(len(sets_lin))]
	num_set = [i for i in num_set if i is not None]

	#lista com indices dos pontos que o set cobre. cada indice é um set
	pontos_set = [A[:,i] if sets_lin[i]==1 else None for i in range(len(sets_lin))]
	pontos_set = [i for i in pontos_set if i is not None]

	#aumentar x ao maximo considerando vetor de custos c
	valores1 = [num_set[i] for i in range (len(num_set))]
	valores2 = []
	for jdx, j in enumerate(num_set):
		val = c[j]
		ind = pontos_set[jdx]

		for idx, i in enumerate(ind):
			if i == 1:
				val = val - x[idx]
		valores2.append(val)

	valores = zip(valores2, valores1)
	valores = sorted(valores)	
	x[point] = valores[0][0]

	return valores[0][1]


def set_cover(elementos, sets, c, A): #implementa algoritmo set cover

	x = np.zeros(elementos)
	y = np.zeros(sets)

	coberturas = list(np.arange(elementos))

	while len(coberturas) != 0: #enquanto existir elemento que nao esteja coberto

		prox_ponto = coberturas[0] #escolher ponto
		prox_set = proximo_set(A, x, c, prox_ponto)
		y[prox_set] = 1

		#retornar pontos que faltam apos a cobertura
		pontos_col = A[:,prox_set]
		pontos_tirar = [idx if i == 1 else None for idx, i in enumerate(pontos_col)]
		remover = [i if i in coberturas  else None for i in pontos_tirar]
		remover = [i for i in remover if i is not None]
		for i in remover:
			coberturas.remove(i)

	for i in y:
		print(int(i), end=' ')
	print()

	for i in x:
		print(int(i), end=' ')
	print()


n, m = input().split()
c = input().split()
a = []
for i in range(int(n)):
  a.append(input().split())

elementos = int(n)
sets = int(m)
A = np.array(a)
A = np.float32(a)
c = np.array(c)
c = np.float32(c)

set_cover(elementos, sets, c, A)


















































