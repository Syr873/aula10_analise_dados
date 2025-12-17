# Atividade 02
SALDO_INICIAL = 2000

try:
    sq = float(input('Informe o valor do saque: '))
except (ValueError, TypeError):
    print('\nErro!!! Digite apenas numeros.')
except KeyboardInterrupt:
    print('Transação encerrada!')
else:
    if sq <= SALDO_INICIAL:
        print(f'Transação aceita! \nRetirando R${sq:.2f}')
    else:
        print('Saldo insuficiente...')
finally:
    print('Operação finalizada!')