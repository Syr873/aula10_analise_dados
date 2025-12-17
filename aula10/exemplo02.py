lst_vendas = []
resposta = 'S'
venda = 1
tentativa = 1

while resposta == 'S':
    try:
        valor = float(input(f'\nInforme a {venda}º venda: '))
    except (ValueError, TypeError):
        print('\nErro!! informe apenas numeros.')
    except KeyboardInterrupt:
        print('\nPrograma encerrado pelo usuario!')
        break
    else:
        lst_vendas.append(valor)
        resposta = input('\nDeseja continuar(S/N)? ')[0].upper()
        venda += 1
    finally:
        print(f'\nTentativa {tentativa} finalizada!')
        tentativa += 1
print(f'\nVendas registradas: {lst_vendas}')

