def leitaint(str = ':'):
    """validação numérica simples, tal qual um 'int(input())'
com a diferença fundamental de que rejeita o parâmetro caso o mesmo não seja numérico
(não é nescessário utilizar entrada do tipo 'int')"""
    while True:
        i = input(str)
        if i.isnumeric():
            return int(i)
        else:
            print('digite um número válido')