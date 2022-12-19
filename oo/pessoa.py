class Pessoa:
    def cumprimenetar(self):
        return f'ola {id(self)}'

if __name__== '__main__':
    p = Pessoa()
    print(Pessoa.cumprimenetar(p))
    print(id(p))
    print(p.cumprimenetar())