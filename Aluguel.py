name = str(input('Diga o seu nome Completo: '))
car = str(input('Diga o nome do carro que gostaria de alugar senhor {}: '.format(name)))
mar = str(input('Sr {} qual seria o fabricante do carro {} :'.format(name, car)))

km = float(input('Diga quantos quilometros foi percorrido pelo carro {} Durante toda a viagem, senhor {}.\nKM: '
                 .format(car, name)))

print('O valor da diaria do carro {} é R$ 60,00 !!'.format(car))
day = float(input('Diga a quantidade de dias que o carro {} ficou alugado senhor {}: '.format(car, name)))

pag = (60 * day) + (0.15 * km)

print('Senhor {} o carro {} ficara pelo valor de R$ {:.2F} Durante todo o periodo de aluguel !'.format(name, car, pag))
print('Obrigado, Volte sempre !!')
