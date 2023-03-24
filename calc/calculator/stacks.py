#   Class - Stacks 

#   The CODE is in Portuguese , sorry for now 


class CLASS_PILHA:

    def __init__(self, tipo_pilha):  # Tipos pilha : str float int bool
        if tipo_pilha == 'NUMERO' or tipo_pilha == 'VALOR':
            tipo_pilha = float
        if tipo_pilha == 'STRING' or tipo_pilha == 'STR':
            tipo_pilha = str
        if tipo_pilha == 'INTEIRO':
            tipo_pilha = int
        if tipo_pilha == 'BOLEANO':
            tipo_pilha = bool

        self.TIPO_PILHA = tipo_pilha

        self.ITENS_PILHA = []

    def entra_pilha(self, valor):
        if type(valor) == str and valor != '':
            if self.TIPO_PILHA == float:
                valor = (float)(valor)
            elif self.TIPO_PILHA == int:
                valor = (int)(valor)
            elif self.TIPO_PILHA == bool:
                valor = (float)(valor)
                if valor == 0.0:
                    valor = False
                else:
                    valor = True
        self.ITENS_PILHA.append(valor)
        return (len(self.ITENS_PILHA))

    def atualiza_pilha(self, valor, numero=-1):
        itens = len(self.ITENS_PILHA)
        if numero == -1:
            numero = itens-1
        if numero < itens and itens > 0:
            if self.TIPO_PILHA != float:
                self.ITENS_PILHA[numero] = valor
            else:
                self.ITENS_PILHA[numero] = (float)(valor)

    def atualiza_ultima_pilha(self, valor):
        self.atualiza_pilha(valor, -1)

    def mostra_pilha(self):
        if self.TIPO_PILHA != str:
            print(self.ITENS_PILHA)
            return (len(self.ITENS_PILHA))
        itens = len(self.ITENS_PILHA)
        for i in range(itens):
            if i > 0 and i < itens:
                print(" ,  ", end='')
            print('"', self.ITENS_PILHA[i], '"', end='')
        print()
        return (len(self.ITENS_PILHA))

    def retorno_pilha_vazia(self):
        if self.TIPO_PILHA == str:
            return ('')
        elif self.TIPO_PILHA == bool:
            return (False)
        elif self.TIPO_PILHA == int:
            return (0)
        else:
            return (0.0)

    def primeira_pilha(self):
        if len(self.ITENS_PILHA) < 1:
            return (self.retorno_pilha_vazia())
        return (self.ITENS_PILHA[0])

    def ultima_pilha(self):
        if len(self.ITENS_PILHA) < 1:
            return (self.retorno_pilha_vazia())
        return (self.ITENS_PILHA[-1])

    def retorna_pilha_numero(self, numero_pilha):
        if len(self.ITENS_PILHA) < numero_pilha:
            return (self.retorno_pilha_vazia())
        return (self.ITENS_PILHA[numero_pilha])

    def proxima_pilha(self, numero_pilha):
        if len(self.ITENS_PILHA) < numero_pilha:
            return (self.retorno_pilha_vazia())
        return (self.ITENS_PILHA[numero_pilha])

    def apaga_ultima_pilha(self):
        if len(self.ITENS_PILHA) < 1:
            return (self.retorno_pilha_vazia())
        return (self.ITENS_PILHA.pop())

    def apaga_pilha_numero(self, numero):
        itens = len(self.ITENS_PILHA)
        if numero == -1:
            numero = itens-1
        if numero < itens and itens > 0:
            self.ITENS_PILHA.pop(numero)
        else:
            return (self.retorno_pilha_vazia())

    def limpa_pilha(self):
        self.ITENS_PILHA.clear()

    def soma_pilha(self, sep=' '):
        itens = len(self.ITENS_PILHA)
        soma = 0.0
        str_aux = ''
        for i in range(itens):
            if (self.TIPO_PILHA == float or self.TIPO_PILHA == int):
                soma += (float)(self.ITENS_PILHA[i])
            elif (self.TIPO_PILHA == bool):
                if self.ITENS_PILHA[i]:
                    soma += 1.0
            elif (self.TIPO_PILHA == str):
                str_aux += self.ITENS_PILHA[i]
                if i < itens:
                    str_aux += sep
        if self.TIPO_PILHA == str:
            return (str_aux)
        return (soma)

    def achou_pilha(self, conteudo):
        if type(conteudo) != self.TIPO_PILHA:
            return (-1)
        for i in range(len(self.ITENS_PILHA)):
            if conteudo == self.ITENS_PILHA[i]:
                return (i)
        return (-1)
