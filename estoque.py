import datetime

meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro' , 'dezembro']

ano, mes, dia = str(datetime.date.today()).split('-')
print(dia, meses[int(mes)-1], ano)

# mes = meses[0]

print(mes)

for i in meses:
    exec(f'estoque{i} = open("C:/Users/User/Desktop/estoque de {i}.txt", "w")')
    exec(f'estoque{i}.write("")')
    exec(f'vendas{i} = open("C:/Users/User/Desktop/vendas de {i}.txt", "w")')

estoque = {}
fim = False
produtos = []

# Programa
while not fim:
    print('''
- Digite 'fim' para finalizar
- Digite 'p' para exibir o estoque
- Digite 'c' para comprar algo do estoque
- Digite 'e' para adicionar no estoque''')

    opcao = input("Opção:  ").lower()

    if opcao == 'e':
        produto = input("\nNome do produto: ")
        produtos.append(produto)
        quantidade = int(input("Quantidade do produto: "))
        preco = float(input("Preço do produto: "))
        
        estoque[produto] = [quantidade, preco]

        for i in meses:
            if i == mes:
                exec(rf"estoque{i}.write(f'produto: {produto}\npreco: R${preco}\nestoque: {quantidade}')")

    elif opcao == 'c':
        itens_disponiveis = []

        for i in estoque: 
            itens_disponiveis.append(i)
        
        if not not itens_disponiveis:
            print(f'Produtos disponiveis: {", ".join(itens_disponiveis)}')
        else:
            print('Não há nada nos produtos!')
        
        nome = input("Nome do produto: ")
        
        # Verificar se existe
        if not nome in itens_disponiveis:
            print('O item não existe!')
        else:
            print(f'\t{nome} tem {estoque[nome][0]} unidades no estoque')
            print(f'\tPreço do {nome} = R${estoque[produto][1]}')

            qtde = int(input("Quantidade a comprar: "))

            if qtde <= estoque[produto][0]:  # qtde < estoque
                preco = qtde * estoque[produto][1]  # preco
                estoque[produto][0]=estoque[produto][0]-qtde

                for i in meses:
                    exec(rf'vendas{i}.write(f"Produto: {produto}\nPreço: R${preco}\nEstoque: {quantidade - qtde}\n\n")')
                
                print(f'\nO total da compra deu R${preco}')
            else:
                print('Coloque uma quantidade menor que o estoque')
                
    elif opcao == 'p':
        print(estoque)
        
    elif opcao == 'fim':
        for i in meses:
            exec(rf'estoque{i}.close()')
            exec(rf'vendas{i}.close()')
        fim = True 
        print(estoque)
        break
