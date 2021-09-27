from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []  # [{Produto (o objeto): quantidade}]


def main() -> None:
    menu()


def menu() -> None:
    print(100 * '\n')
    print('========================================')
    print('============= Bem Vindo(a) =============')
    print('============== Mart Shop ===============')
    print('========================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Comprar produtos')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')
    opcao: int = int(input('>> '))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Operação inválida!')
        sleep(2)
        menu()


def cadastrar_produto() -> None:
    print(100 * '\n')
    print('Cadastro de Produto')
    print('===================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produto() -> None:
    print(100 * '\n')
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('====================')

        for produto in produtos:
            print(produto)
            print('--------------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    input('Pressione qualquer tecla para voltar ao menu: \n>>')
    sleep(1)
    menu()


def comprar_produto() -> None:
    print(100 * '\n')
    # Existem produtos cadastrados?
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho:')
        print('--------------------------------------------------------------')
        print('==================== Produtos Disponíveis ====================')

        for produto in produtos:
            print(produto)
            print('----------------------------------------------------------')
            sleep(1)
        codigo: int = int(input('>> '))

        produto: Produto = pega_produto_por_codigo(codigo)
        # No método pega_produto_por_codigo(), o retorno pode ser um produto ou um None, se o código consultado existir
        # ou não. Se for um produto, o if vai validar como verdadeiro, e entrará nas validações do produto, mas se for
        # None, será falso, então irá para o final, onde será informado que o produto não fora encontrado.

        if produto:
            # Existem produtos no carrinho?
            if len(carrinho) > 0:
                # Se sim, esse produto em específico já existe no carrinho?
                tem_no_carrinho: bool = False

                for item in carrinho:
                    quant: int = item.get(produto)

                    # Se existe, adicione uma quantidade a esse produto
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()

                # Houve a verificação e o tem_no_carrinho manteve-se em False, então esse produto ainda não existe no
                # carrinho.
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()

            # Não há produtos cadastrados no carrinho, então estamos cadastrando este produto
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        # O produto consultado não existe.
        else:
            print(f'O produto com códgo {codigo} não foi encontrado.')
            sleep(2)
            menu()

    # Não existem produtos cadastrados
    else:
        print('Ainda não existem produtos para vender.')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    print(100 * '\n')
    if len(carrinho) > 0:
        print('Produtos do carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)

    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    print(100 * '\n')
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do Carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('--------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
        menu()
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
