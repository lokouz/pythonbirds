class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimenetar(self):
        return f'ola {id(self)}'

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
