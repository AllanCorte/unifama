#Você foi a uma padaria e comprou alguns itens:
#●	Pão: R$3.50
#●	Leite: R$4.20
#●	Café: R$2.80
#Você pagou com uma nota de R$20. Calcule quanto de troco você deve receber.

pao = 3.50
leite = 4.20
cafe = 2.80

conta = pao + leite + cafe
pagamento = 20

troco = pagamento - conta

print(f'o seu troco é {troco}')