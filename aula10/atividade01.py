# Atividade 01 
# VsCode - GitHub
def soma_par(x, y):
    total = x + y
    return total


for n in range(3):
    try:
        num01 = float(input('\nInforme o primeiro numero: '))
        num02 = float(input('Informe o segundo numero: '))
    except (ValueError, TypeError):
        print('\nErro!! Digite apenas numeros.')
    except KeyboardInterrupt:
        print('\nO usuario interrompeu o programa...')
        break
    else:
        soma = soma_par(num01, num02)
        print(f'\nA soma é {soma}')
    finally:
        print('\nPrograma encerrado!')
