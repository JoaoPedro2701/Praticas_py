nome = input('Digite seu nome aqui: ')
idade = int(input('Qual sua idade? '))

print(10 * '---')

maior = 18

if idade >= maior:
    print("Você é de maior")
    print(10 * '---')
else:
    print("Você é de menor (Acesso Negado)")
    print(10 * '---')

if idade >= maior:
    participa = input('[E] para entra e [N] para não entra: ')
    if (participa == 'E' or participa == 'e'):
        print('Seja Bem vindo!')
        print(10 * '---')
        senha = int(input('Cria uma senha? '))
        print(f'Sua senha é {senha}')
        print(10 * '---')
        corrigir = input('[C] para confirma [E] para errado: ')

        if (corrigir == 'C' or corrigir == 'c'):
            print('Senha confirmada')
            print(f'Boa Navegação Sr. {nome}')
            print(10 * '---')
        elif (corrigir == 'E' or corrigir == 'e'):
            print('Erro na confirmação de senha')
            print(10 * '---')

    elif (participa == 'N' or participa == 'n'):
        print('Acesso encerrado!')
