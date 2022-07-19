def opcao(pergunta, min, max):
  pergunta = int(input(pergunta))
  while((pergunta < min) or (pergunta > max)):
    pergunta = int(input('DIGITE UMA DAS OPÇÕES LISTADAS NA TABELA '))
  return pergunta


def criar_txt(nome_arquivado):
  try:
    tentar_criar = open(nome_arquivado, 'wt+')
    tentar_criar.close()
  except:
    print('Erro na ciação do arquivo indicado, pedimos desculpas...')
  else:
    print('Arquivo criado com sucesso, iniciando programa...')
    print('')


def buscar_arquivo(nome_arquivado):
  try:
    tentar_abrir = open(nome_arquivado,'rt')
    tentar_abrir.close()
  except FileNotFoundError:
    return False
  else:
    return True


def listadejogos(arquivo):
  try:
    arquivo = open(arquivo, 'rt')
  except:
    print('Erro ao listar jogos...')
  else:
    print(arquivo.read())
  finally:
    arquivo.close()


def inserirjogo(arquivo, jogo, plataforma):
  try:
    arquivo = open(arquivo, 'at')
  except:
    print('Erro ao inserir jogo em arquivo TXT...')
  else:
    arquivo.write('JOGO: {} \n PLATAFORMA DO MESMO: {} \n'.format(jogo, plataforma))
  finally:
    arquivo.close()


arquivo = 'coleção.txt'
if buscar_arquivo(arquivo):
  print('Arquivo encontrado, iniciando programa...')
  print('')
else:
  print('Arquivo não encontrado, iniciando criação de um novo...') 
  criar_txt(arquivo)

while True:
  try:
    print(' >>>>>>>>>>>>>>>>>>>>>_<<<<<<<<<<<<<<<<<<<<<')
    print('|       COLECIONADOR DE JOGOS DO MATT       |')
    print('| Digite um dos numeros para obter funções: |')
    print('| 1 - COMEÇA UM CADASTRO DE UM NOVO JOGO    |')
    print('| 2 - OBTENHA UMA LISTA DE JOGOS CADASTRADOS|')
    print('| 3 - SAIR DO APLICATIVO COM UM ARQUIVO     |')
    print(' >>>>>>>>>>>>>>>>>>>>>_<<<<<<<<<<<<<<<<<<<<<')
    print('')

    escolha = opcao('O que você deseja fazer meu jovem? ', 1, 3)
  except:
    print('Erro de digitação')
  if(escolha == 1):
    print('Iniciando cadastro de um novo game...')
    jogo = input('Hora de cadastrar um jogo! \n Digite o nome do jogo:')
    plataforma = input('Digite a palatforma do jogo em questão: ')
    inserirjogo(arquivo, jogo, plataforma )


  elif(escolha == 2):
    print('Obtendo lista de jogos e organizando...')
    listadejogos(arquivo)

  elif(escolha == 3):
    print('Obrigado pela preferência, desligando console...')
    break
