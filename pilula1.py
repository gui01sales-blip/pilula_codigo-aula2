import math

assinates = int(input('Assinates atuais:  '))
mensalidade = float(input('Valor da mensalidade : '))
taxa = float(input('Taxa de crescimento mensal (%): '))/100
meses = int(input('Meses de projeção'))

#processamento
assinates_finais = assinates * math.pow((1+taxa), meses)
receita_final = assinates_finais * mensalidade
#saida

print(f'Assinates estimados: {assinates_finais:.1f}')
print(f'Receita mensal estimados R$: {receita_final: .2f}')