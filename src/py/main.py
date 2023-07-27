from math import sqrt


def calcular(cs, svs):
    dists = []
    for index, c in enumerate(cs):
        for indexS, sv in enumerate(svs):
            x1, y1 = c
            x2, y2 = sv

            distancia = sqrt( ((x2 - x1) ** 2) + ((y2 - y1) ** 2) )
            novo = { 'C': index+1, 'SV': indexS+1, 'distancia': round(distancia, 2)}
            dists.append(novo)
    return dists


cs = [
    (6,2),
    (14,9),
    (5,14),
    (3,9)
]

svs = [
    (5,7),
    (2,5),
    (6,11)
]


d = calcular(cs, svs)

for i in d:
    print(i)

maior = None
menor = None

for i in d:
    if menor is None or i['distancia'] > maior['distancia']:
        maior = i

    if menor is None or i['distancia'] < menor['distancia']:
        menor = i

print('Maior distancia: ', maior['distancia'])

print('Menor distancia: ', menor['distancia'])

