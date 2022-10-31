from unidecode import unidecode
from datetime import datetime

class MaquinaEnigima:
    def __init__(self, chave = (datetime.now().day % 5) + 1):
        self.texto_criptografado = ""
        self.index_do_deslocador_de_rotor = 0
        self.rotor = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",",",".","?","!",";","(",")","[","]","-","_",":"]
        self.deslocador_de_rotor = [0,-3, 2,-1]
        self.chave = chave

    def UsarMaquinaEnigima(self,texto,CriptografarOuDescriptografar):# terceiro parametro só pode ser 1 ou -1
        for i in unidecode(texto.upper()):
            if self.index_do_deslocador_de_rotor > 3:
                self.index_do_deslocador_de_rotor = 0

            posição_a_ser_usada = self.chave + self.deslocador_de_rotor[self.index_do_deslocador_de_rotor]
            letra_a_ser_adicionada = self.rotor[(self.rotor.index(i) + posição_a_ser_usada * CriptografarOuDescriptografar) % 39]
            self.texto_criptografado += letra_a_ser_adicionada
            self.index_do_deslocador_de_rotor += 1
        
        self.index_do_deslocador_de_rotor = 0
        texto_retorno = self.texto_criptografado
        self.texto_criptografado = ""

        return texto_retorno
    
    def InformaçõesDaChave(self):
        if self.chave ==  (datetime.now().day % 5) + 1:
            return f"Chave Padrão: {self.chave}"
        else:
            return f"Chave Personalizada: {self.chave}"
