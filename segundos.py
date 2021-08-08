secsEntrada = int(input('Por favor, entre com o numero de segundos que deseja converter: '))
dias = secsEntrada // 86400
horas = (secsEntrada % 86400) // 3600
minutos = ((secsEntrada % 86400) % 3600) // 60
segs = ((secsEntrada % 86400) % 3600) % 60
print(f'{dias} dias, {horas} horas, {minutos} minutos e {segs} segundos')
