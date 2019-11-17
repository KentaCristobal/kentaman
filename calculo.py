from statistics import stdev,variance,median
valor = input('escribe   ')

list=[valor]
std=stdev(list)
print('desviacion estandar',std)

var=variance(list)
print('distribucion',var)

med=median(list)
print('promedio',med)
