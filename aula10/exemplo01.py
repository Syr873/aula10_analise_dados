def calcula_atingimento(v, m):
    r = v/m
    return r * 100


for num in range(1, 4):
    try:
        venda = float(input('\nInforme o valor da venda: '))
        meta = float(input('\nInforme o valor da meta: '))
        resultado = calcula_atingimento(venda, meta)
    except (ValueError,TypeError):
        print('\nErro!! Digite apenas numeros.')
    except ZeroDivisionError:
        print('\nErro!! A meta não pode ser zero.')
    except KeyboardInterrupt:
        print('Operação encerrada pelo usuário!')
    else:
        print(f'Resultado: {resultado:.1f}%')
    finally:
        print('\nOperação finalizada!')





