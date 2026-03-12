import datetime 
#entrada
data_compra = input('Digite a data de compra d/m/aaas ')
meses = int(input('Prazo de garantia'))
#processamento
data_inicial = datetime.datetime.strftime(data_compra, '%d/%m/&Y')
data_final = data_inicial + datetime.timedelta(days=meses * 30)
#saida
print(f'Garantia válida até {data_final.strftime(' %%d/%m/%Y')}')
print(f'Dia da semana: {data_final.strftime('%A')}')