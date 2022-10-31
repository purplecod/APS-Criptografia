from Menu import Menu,Limpador
from MaquinaEnigima import MaquinaEnigima
from time import sleep

Criptografar = 1
Descriptografar = -1

Maquina = MaquinaEnigima()

while True:
    while True:
        try:
            Limpador()
            Menu(["Criptografar Texto","Descriptografar Texto","Alterar Chave","Encerrar"])
            OpçãoEscolhida = int(input("Digite o numero da opção desejada: "))

        except ValueError:
            print("Digite um valor valido")
            sleep(1)

        else:
            if OpçãoEscolhida > 0 and OpçãoEscolhida < 5:
                break
            else:
                print("Escolha uma opção valida")
                sleep(1)

    if OpçãoEscolhida == 1:
        while True:
            try:
                Limpador()
                TextoASerCriptografado = input("AVISO: Não use acentos, escreva numeros por extenço e não use caracteres desse tipo: #%¨&=+/ \nEscreva o texto (Digite $$ para voltar ao menu inicial): ")
                if TextoASerCriptografado == "$$":
                    break
                print(Maquina.UsarMaquinaEnigima(TextoASerCriptografado,Criptografar))
                Repetir = input("\nA criptografia foi um sucesso, quer tentar outro texto? [S/N]")

                if Repetir.upper() == "N":
                    break
            
            except ValueError:
                Repitir = input("Ocorreu um erro na criptografia. Quer tentar de novo? [S/N]")
                if Repetir.upper() == "N":
                    break               

    elif OpçãoEscolhida == 2:
        while True:
            try:
                Limpador()
                TextoASerDescriptografado = input("AVISO: Se caso a chave que foi usada pra criptografar esse texto for diferente da atual, o texto não vai fazer sentido.\nDigite o texto criptografado (Digite $$ para voltar ao menu inicial): ")
                if TextoASerDescriptografado == "$$":
                    break
                print(Maquina.UsarMaquinaEnigima(TextoASerDescriptografado,Descriptografar))
                Repetir = input("\nA descriptografia foi um sucesso, quer tentar outro texto? [S/N]")

                if Repetir.upper() == "N":
                    break
            except ValueError:
                Repitir = input("Ocorreu um erro na descriptografia. Quer tentar de novo? [S/N]")
                if Repetir.upper() == "N":
                    break         

    elif OpçãoEscolhida == 3:
        while True:
            Limpador()
            print(Maquina.InformaçõesDaChave())
            PersonalizarChave = input("Deseja modificar a chave? [S/N]: ")
            if PersonalizarChave.upper() == "S":
                while True:
                    try:
                        NovaChave = int(input("Digite um numero de 1 a 10 para definir uma nova chave [99 Para cancelar a função]: "))
                        if NovaChave == 99:
                            break

                        Maquina = MaquinaEnigima(NovaChave)
                    
                    except ValueError:
                        print("Erro digite um valor valido.")
                        sleep(1)
                        Limpador()
                    else:
                        if NovaChave > 0 and NovaChave < 11:
                           print("Nova chave definida.")
                           sleep(2)
                           break
                        
                        else:
                            print("Chave invalida. Tente outra.")
                            sleep(2)
                            Limpador()
            break

    else:break
