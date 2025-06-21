#3.	Calculadora de Tarifas de Táxi
#Uma empresa de táxi cobra uma tarifa básica de R$4.00,\
#  mais R$0.25 por quilômetro rodado. Crie um programa que calcula 
# o valor total da corrida com base na distância percorrida.
distancia = float(input('qual a distancia que ira ser percorrida em km '))
tarifa_basica = 4.0
tarifa_por_km = 0.25

tarifa_total = tarifa_basica + (distancia * tarifa_por_km)

print(f' o valor total fica {tarifa_total :.2f}')