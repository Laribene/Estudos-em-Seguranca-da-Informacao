import math # Biblioteca para calcular bhaskara

mensagem_criptografada = []
resultado_funcao = []
mensagem_descriptografada = []

def mensagem_cripto_lista(arquivo):
    for linha in arquivo:  # Colocar os numeros da mensagem criptografada em uma lista
           for n in linha.split(' '):
               if n != '':
                   mensagem_criptografada.append(n)

    calcular_bhaskara(mensagem_criptografada)


def calcular_bhaskara(mensagem_criptografada):
    for numero_criptografado in mensagem_criptografada: # Colocar os numeros da mensagem criptografada em uma lista
        if numero_criptografado != '\n':        # Equação de bhaskara
            numero_criptografado = int(numero_criptografado)
            numero_criptografado = numero_criptografado * -1
            calculo_bhaskara=(2**2)-(4*1*numero_criptografado)
            calculo_bhaskara=math.sqrt(calculo_bhaskara)
            calculo_bhaskara=(-2+calculo_bhaskara)/(2*1)
            resultado_funcao.append(calculo_bhaskara)
        elif numero_criptografado == '\n':
            resultado_funcao.append('\n')

    converter_numero_em_letra(resultado_funcao)


def converter_numero_em_letra(resultado_funcao):
    for numero in resultado_funcao:   # Conversão de numeros para letras
        if numero == 1:
            mensagem_descriptografada.append('a')
        elif numero == 2:
            mensagem_descriptografada.append('b')
        elif numero == 3:
            mensagem_descriptografada.append('c')
        elif numero == 4:
            mensagem_descriptografada.append('d')
        elif numero == 5:
            mensagem_descriptografada.append('e')
        elif numero == 6:
            mensagem_descriptografada.append('f')
        elif numero == 7:
            mensagem_descriptografada.append('g')
        elif numero == 8:
            mensagem_descriptografada.append('h')
        elif numero == 9:
            mensagem_descriptografada.append('i')
        elif numero == 10:
            mensagem_descriptografada.append('j')
        elif numero == 11:
            mensagem_descriptografada.append('k')
        elif numero == 12:
            mensagem_descriptografada.append('l')
        elif numero == 13:
            mensagem_descriptografada.append('m')
        elif numero == 14:
            mensagem_descriptografada.append('n')
        elif numero == 15:
            mensagem_descriptografada.append('o')
        elif numero == 16:
            mensagem_descriptografada.append('p')
        elif numero == 17:
            mensagem_descriptografada.append('q')
        elif numero == 18:
            mensagem_descriptografada.append('r')
        elif numero == 19:
            mensagem_descriptografada.append('s')
        elif numero == 20:
            mensagem_descriptografada.append('t')
        elif numero == 21:
            mensagem_descriptografada.append('u')
        elif numero == 22:
            mensagem_descriptografada.append('v')
        elif numero == 23:
            mensagem_descriptografada.append('w')
        elif numero == 24:
            mensagem_descriptografada.append('x')
        elif numero == 25:
            mensagem_descriptografada.append('y')
        elif numero == 26:
            mensagem_descriptografada.append('z')
        elif numero == '\n':
            mensagem_descriptografada.append('\n')

    salvar_mensagem_descriptografa_em_arquivo(mensagem_descriptografada)

def salvar_mensagem_descriptografa_em_arquivo(mensagem_descriptografada):
    arquivo = open('decrypted-text.txt', 'w')
    for letra in mensagem_descriptografada:
        arquivo.write(letra)

    arquivo.close()

if __name__ == '__main__':
    arquivo = open('encrypted-text.text', 'r') # Abertura do arquivo que contem a mensagem criptografada
    mensagem_cripto_lista(arquivo) #Chamada da primeira função
