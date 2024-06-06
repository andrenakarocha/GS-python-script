menu = ''' 
---------Menu---------
1 - Adicionar Dados
2 - Analisar Dados
3 - Histórico de Dados
4 - Sair
----------------------
'''

print('Seja bem vindo, escolha abaixo uma opção:')

# Listas para armazenar os dados
data = []
pH = []
temperatura = []

# funcões padrões
def adicionar_dados (lista_datas, lista_pH, lista_temperatura):
    print('Adicione os dados baseando-se na análise da água do mar: ')

    dia = forcar_data('Qual o dia de hoje? (dd) ')
    mes = forcar_data('Qual o mês? (mm) ')
    pH = forcar_numero('Qual o pH da água encontrado? ')
    temperatura = forcar_numero('Qual a temperatura da água encontrada? ')

    lista_datas.append(f'{dia}/{mes}')
    lista_pH.append(pH)
    lista_temperatura.append(temperatura)

def analisar_dados (lista_datas, lista_pH, lista_temperatura):
    data = input('Qual a data registrada dos dados que deseja analisar? (dd/mm)')
    indexDados = 0
    for i in range(len(lista_datas)):
        if data == lista_datas[i]:
            indexDados = i
        else:
            print('Digite uma data válida!')
            data = input('Qual a data registrada dos dados que deseja analisar? (dd/mm)')


    print('Dados analisados! Segue o resultado: ')

    pH = verificar_pH(lista_pH, indexDados)
    temperatura = verificar_temperatura(lista_temperatura, indexDados)

    print(f'pH = {pH} \nTemperatura = {temperatura}')

def visualizar_historico (lista_data, lista_pH, lista_temperatura):
    print('Segue o histórico de dados: ')
    print(transformar_lista(lista_data, lista_pH, lista_temperatura))

# funcões de apoio
def transformar_lista (lista_data, lista_pH, lista_temperatura):
    novoTexto = ""
    for i in range(len(lista_data)):
        novoTexto += f'Dia = {lista_data[i]} - pH = {lista_pH[i]} - Temperatura = {lista_temperatura[i]}\n'
    return novoTexto

def verificar_pH (lista_pH, index):
    lista_pH[index] = int(lista_pH[index])

    if lista_pH[index] == 7:
        return 'pH Neutro!'
    
    elif 8 <= lista_pH[index] <= 9:
        return 'pH Okay!'

    elif lista_pH[index] < 8:
        return 'pH Ácido!'

    elif lista_pH[index] > 9:
        return 'pH Base!'
    
def verificar_temperatura (lista_temperatura, index):
    lista_temperatura[index] = int(lista_temperatura[index])
    
    if lista_temperatura[index] < 25:
        return 'Temperatura OK!'
    else:
        return 'Temperatura não ideal!'

def forcar_data (mensagem):
    data = input(mensagem)

    while True:
        if data.isnumeric() and len(data) == 2:
            break
        else:
            print('Digite um número!')
            data = input(mensagem)

    return data

def forcar_numero (mensagem):
    num = input(mensagem)

    while True:
        if num.isnumeric():
            break
        else:
            print('Digite um número!')
            num = input(mensagem)
            
    return num

# Opcões
while True:
    escolha = input(menu)

    if escolha == '1':
        adicionar_dados(data, pH, temperatura)

    elif escolha == '2':
        analisar_dados(data, pH, temperatura)

    elif escolha == '3':
        visualizar_historico(data, pH, temperatura)

    elif escolha == '4':
        break

    else:
        print('Essa opção não é válida!')