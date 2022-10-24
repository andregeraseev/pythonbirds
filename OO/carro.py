"""Criar uma classe que vai possuir dois
atributos composta por outras duas classes:

1 Motor
2 Direçao

O motor tera a responsabiliadde de controlar a velocidade.
Ele oferece os seguintes atributos:
1)Atributo de dado velocidade
2)metodo acelerar, que devera incremetar a velocidade em uma unidade
3) metodo frear que devera decremetar a velocidade em duas unidades



A Direção tera a responsabilidade de controlar a direção. Ele oferece
os seguintes atributos:
1) Valor de direçao com valores Possiveis, Norte, Sul, Leste, Oeste
2) Metodo girar_a_direita
2) Metodo de girar_a_esquerda

>>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro()
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    Norte
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    Leste
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    Norte
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    Oeste
"""


class Motor():

    velocidade=0

    def acelerar(self):
        self.velocidade += 1


    def frear(self):
        self.velocidade -= 2
        if self.velocidade <= 0:
            self.velocidade = 0

    def calcular_velocidade(self):
        print(self.velocidade)

class Direcao():
    valor = "Norte"


    def girar_a_direita(self):
        match self.valor:
            case "Norte":
                self.valor = 'Leste'
            case 'Leste':
                self.valor = 'Sul'
            case 'Sul':
                self.valor = 'Oeste'
            case 'Oeste':
                self.valor = 'Norte'


    def girar_a_esquerda(self):
        match self.valor:
            case "Norte":
                self.valor = 'Oeste'
            case 'Oeste':
                self.valor = 'Sul'
            case 'Sul':
                self.valor = 'Leste'
            case 'Leste':
                self.valor = 'Norte'

    def calcular_direcao(self):
        print(self.valor)


class Carro(Direcao,Motor):
    pass

if __name__=='__main__':
    # carro = Carro()
    # carro.calcular_direcao()
    # carro.calcular_velocidade()
    # carro.girar_esquerda()
    # carro.calcular_direcao()
    # carro.acelerar()
    # carro.calcular_velocidade()
    # carro.girar_esquerda()
    # carro.calcular_direcao()
    # carro.girar_esquerda()
    # carro.calcular_direcao()
    # carro.acelerar()
    # carro.calcular_velocidade()
    # carro.acelerar()
    # carro.calcular_velocidade()
    # carro.frear()
    # carro.calcular_velocidade()
    # carro.frear()
    # carro.calcular_velocidade()
    # carro.girar_esquerda()
    # carro.girar_direita()
    # carro.calcular_direcao()
    # carro.girar_direita()
    # carro.calcular_direcao()
    # carro.girar_direita()
    # carro.calcular_direcao()
    # carro.girar_direita()
    # carro.calcular_direcao()

    motor = Motor()
    motor.velocidade
        #0
    motor.acelerar()
    motor.velocidade
        #1
    motor.acelerar()
    motor.velocidade
        #2
    motor.acelerar()
    motor.velocidade
        #3
    motor.frear()
    motor.velocidade
        #1
    motor.frear()
    motor.velocidade
        #0
    # Testando Direcao
    direcao = Direcao()
    direcao.valor
        #'Norte'
    direcao.girar_a_direita()
    direcao.valor
        #'Leste'
    direcao.girar_a_direita()
    direcao.valor
        #'Sul'
    direcao.girar_a_direita()
    direcao.valor
        #'Oeste'
    direcao.girar_a_direita()
    direcao.valor
        #'Norte'
    direcao.girar_a_esquerda()
    direcao.valor
        #'Oeste'
    direcao.girar_a_esquerda()
    direcao.valor
        #'Sul'
    direcao.girar_a_esquerda()
    direcao.valor
        #'Leste'
    direcao.girar_a_esquerda()
    direcao.valor
        #'Norte'
    carro = Carro()
    carro.calcular_velocidade()
        #0
    carro.acelerar()
    carro.calcular_velocidade()
        #1
    carro.acelerar()
    carro.calcular_velocidade()
        #2
    carro.frear()
    carro.calcular_velocidade()
        #0
    carro.calcular_direcao()
        #'Norte'
    carro.girar_a_direita()
    carro.calcular_direcao()
        #'Leste'
    carro.girar_a_esquerda()
    carro.calcular_direcao()
        #'Norte'
    carro.girar_a_esquerda()
    carro.calcular_direcao()









