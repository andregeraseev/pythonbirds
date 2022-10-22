class Pessoa:
    olhos = 2
    def __init__(self,*filhos, nome=None, idade = None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


# if __name__=='__main__':
#     renzo = Pessoa(nome='Renzo')
#     luciano= Pessoa(renzo,nome='Andre')
#     print(luciano.cumprimentar())
#     print(luciano.filhos[0].nome)
#     for filho in luciano.filhos:
#         print(filho.nome)
#     luciano.sobrenome="Ramalho"
#     del luciano.filhos
#     print(luciano.__dict__)
#     print(renzo.__dict__)
#     print(Pessoa.olhos)
#     print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
#     print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())