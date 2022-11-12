from datetime import datetime

class MaquinaEnigima:
    """
    Classe responsável pela criptografia do programa.
    """

    def __init__(self, chave = (datetime.now().day % 5) + 1):
        self.texto_criptografado = ""
        self.index_do_deslocador_de_rotor = 0
        self.rotor =  ['5', '?', 'B', ']', '¡', 'p', 'd', 'è', '¹', 'M', 'X', 'Ï', 'ø', '¸', '±', 'q', 'È', '#', 's', '6', 'h', ' ', 'ç', 'S', 'ó', '³', 'j', 'Á', 't', '¶', 
                       'Â', '%', 'é', 'C', 'Ë', 'Ò', '>', 'x', '²', 'Ô', '}', 'ª', '½', 'g', 'U', 'y', 'Î', '.', 'õ', 'b', '×', 'ã', 'Ö', 'À', 'N', '&', 'c', 'Ā', '8', '¦', 
                       ')', 'à', '(', ';', 'L', 'v', 'á', 'â', 'Y', '\\', 'l', 'ð', 'Ç', 'ü', '¨', ':', '¤', 'o', '2', '¯', '/', 'É', '~', 'R', '{', '7', '@', 'Q', 'º', 'V',
                       'A', 'ë', 'W', '+', '4', 'u', 'Ñ', '^', 'ù', 'û', 'µ', 'ä', 'ï', 'þ', 'Ì', 'Ù', 'ì', 'k', '`', 'å', 'ò', 'P', 'a', 'Þ', 'ý', '9', 'Ð', 'Ü', '<', '«',
                       '¾', 'e', '®', 'T', '¬', 'z', 'æ', "'", 'G', 'Ú', 'ñ', '÷', '$', 'n', '£', 'ÿ', '3', '¢', 'O', 'ê', '¥', ',', '0', '=', 'Ó', 'D', 'Ý', 'm', 'Å', '·', 
                       'H', 'J', 'Û', 'ß', '¼', '-', '°', '1', 'Æ', '§', 'ú', '´', 'r', 'Í', '©', 'I', 'ö', 'î', '_', '*', 'i', '"', 'Ã', '[', 'Ä', '»', 'Ø', 'í', 'Z', 'f',
                       'Õ', 'E', 'Ê', '|', 'w', 'F', '¿', '!', 'K']

        self.deslocador_de_rotor = [0, 10,-9,-8, 7,-6, 5, 4,-3, 2, 1]
        self.chave = chave

    def UsarMaquinaEnigima(self,texto,CriptografarOuDescriptografar):
        """
        Criptografa ou descriptografa o texto que for dado no parametro "texto"

        Paramêtros:
                texto (string): texto que vai ser criptogrfado ou descriptografado

                CriptografarOuDescriptografar (int): Paramêtro que vai definir se a maquina vai descriptografar ou criptografar. 
                se igual 1, criptografar.
                se igual 2, descriptografar.
                se nenhum dos dois, o metodo vai lançar uma exceção

                retorno (string): retorna o texto criptografado ou descriptografado
        """
        if CriptografarOuDescriptografar != 1 and CriptografarOuDescriptografar != -1:
            raise "Valor invalido: o valor do paramêtro CriptografarOuDescriptografar precisa ser 1 ou -1"

        for i in texto:
            if self.index_do_deslocador_de_rotor > 3:
                self.index_do_deslocador_de_rotor = 0

            posição_a_ser_usada = self.chave + self.deslocador_de_rotor[self.index_do_deslocador_de_rotor]
            letra_a_ser_adicionada = self.rotor[(self.rotor.index(i) + posição_a_ser_usada * CriptografarOuDescriptografar) % len(self.rotor)]
            self.texto_criptografado += letra_a_ser_adicionada
            self.index_do_deslocador_de_rotor += 1
        
        self.index_do_deslocador_de_rotor = 0
        texto_retorno = self.texto_criptografado
        self.texto_criptografado = ""

        return texto_retorno
    
    def InformaçõesDaChave(self):
        """
        Retorno (int): Retorna o numero da chave que esta sendo usada hoje.
        """
        if self.chave ==  (datetime.now().day % 5) + 1:
            return f"Chave Padrão: {self.chave}"
        else:
            return f"Chave Personalizada: {self.chave}"
