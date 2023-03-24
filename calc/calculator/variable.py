#   Class - Variable , expressions and strings

import math


class CLASS_VARIAVEL:

    def __init__(self, nome_var, valor=0.0, expressao='', maiuscula=True):
        self.nome_var = nome_var.upper()
        self.valor = valor
        if maiuscula:
            self.expressao = expressao.upper()
        else:
            self.expressao = expressao


class VARIAVEIS:

    def __init__(self, maiuscula=False, tipo_variavel='VARIAVEL'):

        self.MAIUSCULA = maiuscula

        self.TIPO_VARIAVEL = tipo_variavel

        self.VAR = [
            CLASS_VARIAVEL(' ', 0.0, ' '),
        ]
        self.VAR.pop()

    def prepara_nome_variavel(self, nome_var):
        nome = nome_var.upper()
        nome = nome_var.strip()
        nome = nome_var.replace('\n', ' ')
        nome_var = ''
        for letra in nome:
            if letra in ' +-*/^?><,;:=!"%[]()|':
                break
            nome_var += letra
        return (nome_var)

    def mostra_variaveis(self):
        print('\n         ', self.TIPO_VARIAVEL, ' :', '\n')
        for i in range(len(self.VAR)):
            print(self.VAR[i].nome_var, end='')
            if math.fabs(self.VAR[i].valor) >= 0.00000001:
                print(' =', self.VAR[i].valor, end='')
            if self.VAR[i].expressao != '':
                if self.TIPO_VARIAVEL == 'EXPRESSAO':
                    print(' : [', self.VAR[i].expressao, ']', sep='', end='')
                elif self.TIPO_VARIAVEL == 'STRING':
                    print(' : "', self.VAR[i].expressao, '"', sep='', end='')
                else:
                    print(' :', self.VAR[i].expressao, end='')
            print()

    def entra_variavel(self, nome_var, valor, expressao=''):
        itens = len(self.VAR)
        num = 0
        nome_var = self.prepara_nome_variavel(nome_var)
        if self.MAIUSCULA:
            expressao = expressao.upper()
        while num < itens:
            if (self.VAR[num].nome_var == nome_var):
                self.VAR[num].valor = float(valor)
                self.VAR[num].expressao = expressao
                break
            num += 1
        if (num == itens):
            VARX = CLASS_VARIAVEL(nome_var, float(valor), expressao)
            self.VAR.append(VARX)
        return (num)

    def busca_variavel(self, nome_var):
        num = self.achou_variavel(nome_var)
        if num != -1:
            return (self.VAR[num].valor)
        else:
            return (0.0)

    def achou_variavel(self, nome_var):
        nome_var = self.prepara_nome_variavel(nome_var)
        for num in range(len(self.VAR)):
            if (self.VAR[num].nome_var == nome_var):
                return (num)
        return (-1)

    # str = 'Valor= continua'  retorna('Valor',5)
    def copia_string_ate_caracter(self, str, chr=' '):
        str_aux = ''
        pos = 0
        for letra in str:
            if letra in chr:
                return (str_aux, pos)
            str_aux += letra
            pos += 1
        return (str_aux, pos)
