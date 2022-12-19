class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=36):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimenetar(self):
        return f'ola {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__== '__main__':
    takechi = Pessoa(nome='takechi')
    fabio = Pessoa(takechi, nome='fabio')
    print(Pessoa.cumprimenetar(fabio))
    print(id(fabio))
    print(fabio.cumprimenetar())
    print(fabio.nome)
    print(fabio.idade)
    for filho in fabio.filhos:
        print(filho.nome)
    fabio.sobrenome = 'sato'
    del fabio.filhos
    fabio.olhos = 1
    del fabio.olhos
    print(fabio.__dict__)
    print(takechi.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(fabio.olhos)
    print(takechi.olhos)
    print(id(Pessoa.olhos), id(fabio.olhos), id(takechi.olhos))
    print(Pessoa.metodo_estatico(), fabio.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), fabio.nome_e_atributos_de_classe())
