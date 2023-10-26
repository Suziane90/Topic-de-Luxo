from src.passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios):
        self.capacidade = capacidade
        self.qtdPrioritarios = qtdPrioritarios
        self.qtdNormal = capacidade - qtdPrioritarios
        self.passageirosN = []
        self.passageirosP = []
        self.assentosP = ['@'] * qtdPrioritarios
        self.assentosN = ['='] * (self.qtdNormal)
        self.assentos = '[' + ' '.join(self.assentosP) + ' ' + ' '.join(self.assentosN) + ' ]'

    def getNumeroAssentosPrioritarios(self):
        return self.qtdPrioritarios

    def getNumeroAssentosNormais(self):
        return self.qtdNormal

    def getPassageiroAssentoNormal(self, lugar):
        return self.passageirosN[lugar]

    def getPassageiroAssentoPrioritario(self, lugar):
        return self.passageirosP[lugar]

    def getVagas(self):
        return self.qtdNormal + self.qtdPrioritarios

    def subir(self, passageiro: Passageiro):  # consertar erro
        if self.getVagas() == 0:
            return False
        elif passageiro.ePrioridade() is True and self.qtdPrioritarios > 0:
            self.passageirosP.append(passageiro)
            self.assentosP[self.passageirosP.index(passageiro)] = '@' + passageiro.getNome()
            self.assentos = '[' + ' '.join(self.assentosP) + ' ' + ' '.join(self.assentosN) + ' ]'
            self.qtdPrioritarios -= 1

        elif passageiro.ePrioridade() is False and self.qtdNormal > 0:
            self.passageirosN.append(passageiro)
            self.assentosN[self.passageirosN.index(passageiro)] = '=' + passageiro.getNome()
            self.assentos = '[' + ' '.join(self.assentosP) + ' ' + ' '.join(self.assentosN) + ' ]'
            self.qtdNormal -= 1

        elif passageiro.ePrioridade() is True and self.qtdPrioritarios == 0:
            if self.qtdNormal > 0:
                self.passageirosN.append(passageiro)
                self.assentosN[self.passageirosN.index(passageiro)] = '=' + passageiro.getNome()
                self.assentos = '[' + ' '.join(self.assentosP) + ' ' + ' '.join(self.assentosN) + ' ]'
                self.qtdNormal -= 1

        elif passageiro.ePrioridade() is False and self.qtdNormal == 0:
            if self.qtdPrioritarios > 0:
                self.passageirosP.append(passageiro)
                self.assentosP[self.passageirosP.index(passageiro)] = '@' + passageiro.getNome()
                self.assentos = '[' + ' '.join(self.assentosP) + ' ' + ' '.join(self.assentosN) + ' ]'
                self.qtdPrioritarios -= 1

        return True

    def descer(self, nome):
        if nome in self.assentosP:
            for i in range(len(self.passageirosP)):
                if self.passageirosP[i].getNome() == nome:
                    self.passageirosP.pop(i)
                    self.assentosP[i] = '@'
                    self.assentos = '[' + ' '.join(self.assentosP)+' '+' '.join(self.assentosN) + ' ]'
                    self.qtdPrioritarios += 1
                    return True

        elif nome in self.assentosN:
            for i in range(len(self.passageirosN)):
                if self.passageirosN[i].getNome() == nome:
                    self.passageirosN.pop(i)
                    self.assentosN[i] = '='
                    self.assentos = '[' + ' '.join(self.assentosP)+' '+' '.join(self.assentosN) + ' ]'
                    self.qtdNormal += 1
                    return True
