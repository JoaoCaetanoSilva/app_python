conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9}
conjunto_uniao = conjunto1.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto1.intersection(conjunto2)
print('Interseccao: {}'.format(conjunto_interseccao))
conjunto_diferenca1 = conjunto1.difference(conjunto2)
conjunto_diferenca2 =conjunto2.difference(conjunto1)
print('Diferença entre o conjunto 1 e o conjunto 2: {}'.format(conjunto_diferenca1))
print('Diferença entre o conjunto 2 e o conjunto 1: {}'.format(conjunto_diferenca2))

# Obs: 0 (+) não funciona pois é {}.