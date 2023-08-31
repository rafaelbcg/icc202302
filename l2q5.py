user = input('user: ')
password = input('password: ')

if len(password) < 6:
    print('Senha com menos que 6 caracteres')

if len(user) < 3:
    print('Usuário com menos que 3 caracteres')

if user.lower() == password.lower():
    print('Senha e usuário iguais.')

