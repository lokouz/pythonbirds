class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimenetar(self):
        return f'ola {id(self)}'

if __name__== '__main__':
    p = Pessoa()
    print(Pessoa.cumprimenetar(p))
    print(id(p))
    print(p.cumprimenetar())
    print(p.nome)
    p.nome = 'Fabio'
    print(p.nome)
    print(p.idade)