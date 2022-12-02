from módulo import leitaint
while True:
# d = decisão, com o leiaint() [help(leitaint)] guarda a escolha da opção aceitando apenas números de 1 a 3
    d = leitaint('''[1] - ver pessoas cadastradas
[2] - cadastrar nova pessoa
[3] - sair do sistema
''')
    if d == 1:
# se "d" = 1 abra arquivo de texto escolhido como "reader" e escreva oq está escrito
        with open("Ex115.txt","r") as ex115:
            print('')
            lista = []
            lista.append(ex115.read())
            print(lista[0])
            print('')
    if d == 2:
#se "d" = 2 peça ao usuário escrever um nome e uma idade e guarde em um documento sob a forma:
#Nome Exemplo - 9;
        with open("Ex115.txt","a") as ex115:
            ex115.write(f"\n{input('nome escolhido:')}")
            ex115.write(f" - {leitaint('idade:')},")
    if d == 3:
# se "d" = 3 escreva "obrigado por usar e encerre o programa"
        print('obrigado por usar')
        exit()
