from Controller import ControllerCadastro, ControllerLogin

while True:
    print('='*10, '[MENU]', '='*10)
    decidir = int(input(('Digite 1 para cadastrar \nDigite 2 para logar\nDigite 3 para sair\n')))

    # CADASTRO
    if decidir == 1:
        nome = input('Digite seu nome:\n')
        email = input('Digite seu email:\n')
        senha = input('Digite sua senha:\n')
        resultado = ControllerCadastro.cadastrar(nome, email, senha)

        # Tratamento dos retornos de cadastro
        if resultado == 2:
            print('Tamanho do nome digitado inválido')
        elif resultado == 3:
            print('E-mail maior que 200 caracteres')
        elif resultado == 4:
            print('Tamanho da senha inválido')
        elif resultado == 5:
            print('E-mail já cadastrado')
        elif resultado == 6:
            print('Erro interno do sistema')
        elif resultado == 1:
            print('Cadastro realizado com sucesso')
    # LOGIN
    elif decidir == 2:
        email = input('Digite o e-mail cadastrado:\n')
        senha = input('Digite a senha cadastrada:\n')

        resultado = ControllerLogin.verificaLogin(email, senha)

        if not resultado:
            print('Falha no login!')
        else:
            print('Login realizado com sucesso', resultado)
        break
    # EXIT
    else:
        break