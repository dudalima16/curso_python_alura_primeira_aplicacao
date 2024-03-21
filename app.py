import os

restaurantes = [{'nome': 'Praça', 'categoria':'Japonesa', 'ativo':False}, #dicionário
                {'nome':'Pizza Suprema', 'categoria':'Pizza','ativo':True},
                {'nome': 'cantina', 'categoria': 'Italiano', 'ativo':False}]

def exibir_nome_do_programa(): 
    '''Exibe o nome do programa na tela''' 
    print('Sabor Express\n')


def exibir_opcoes(): 
    '''Exibe as opções disponiveis no menu principal'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alternar estado do Restaurante')
    print('4. Sair')

def finalizar_app():
    '''Exibe mensagem de finalização do aplicativo'''
    exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
    '''Solicita uma tecla para voltar ao menu
    Outputs:
        - retorna ao menu principal

    Input('\nDigite uma tecla para voltar ao menu')
    '''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção invalida\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    os.system('cls') # comando para limpar a tela do user
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novos_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante
       
       Inputs:
       - Nome do restaurente
       - Categoria

       Output:
       - Adiciona um novo restaurente a lista de restaurantes
    
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digeite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes')
    '''Essa função é responsavel por listar os restaurantes'''

    print(f"{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restautante in restaurantes:    # para cada restaurante na lista restaurantes:
        nome_restaurante = restautante['nome']
        categoria = restautante['categoria']
        ativo = 'ativado' if restautante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}' )

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsavel por alterar o estado do restaurante'''

    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar: ')
    restaurante_encontrado = False

    for restautante in restaurantes:
        if  nome_restaurante == restautante['nome']:
            restaurante_encontrado = True
            restautante['ativo'] = not restautante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restautante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()



def escolher_opcao():
    '''Essa função é responsavel pelo MENU'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novos_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls') # limpar a tela
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
    