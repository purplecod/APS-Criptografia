def Vermelho(txt):
  return f'\033[31m{txt}\033[m'
def Verde (txt):
  return f'\033[32m{txt}\033[m'
def Amarelo (txt):
  return f'\033[33m{txt}\033[m'
def Azul (txt):
  return f'\033[34m{txt}\033[m'
def Roxo (txt):
  return f'\033[35m{txt}\033[m'
def Ciano (txt):
  return f'\033[36m{txt}\033[m'
def Cinza (txt):
  return f'\033[37m{txt}\033[m' 
  

def Titulo(txt):
  print('==='*15)
  print(txt.center(44))
  print('==='*15)


def Menu(lista,txt='MENU PRINCIPAL'):
  c=1
  Titulo(txt)
  for items in lista:
    print(f'{c} - {Roxo(items)}')
    c+=1
  print('==='*15)

def Limpador():
  from os import system
  import platform

  sistema_operacional = platform.system()

  if sistema_operacional == "Windows":
      limpador = "cls"
  elif sistema_operacional == "Linux":
      limpador = "clear"
      
  return system(f"{limpador}")
