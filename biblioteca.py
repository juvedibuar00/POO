class Livro:
    def __init__(self, titulo, autor, ano, status):
        #criando anotation
        '''CRIA UM OBJETO DA CLASSE LIVRO COM OS ATRIBUTOS SOLICITADOS. 
        O STATUS DEVE SER "DISPONIVEL OU INDISPOINIVEL" '''
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = status



    def setDisponivel(self):
        self.status = 'disponível'
    
    def setIndisponivel(self):
        self.status = 'indisponível'




    











class Biblioteca:
    '''Cria um objeto da classe biblioteca, para agrupar objetos da classe livros. Contará com os métodos
    listar e adionar lirvro'''
    def __init__(self):
        self.lista=[]

    #metodo
    def adicoinarLivro(self, objetoLivro):
        self.lista.append(objetoLivro)
        return 'O livro foi adionado com sucesso!'
    
    def listarLivros(self):
        for livro in self.lista:
            print(f'titulo: {livro.titulo} | ano: {livro.ano} | autor: {livro.autor} | status: {livro.status}')



    def emprestarLivro (self, tituloLivro):
        '''laço de repetição para percorrer toda a lista'''
        for livro in self.lista:
            if livro.titulo == tituloLivro:
                livro.setIndisponivel()
                print(f'O livro {livro.titulo} foi emprestado com sucesso. O seu status agora é indisponível.')



livro1 = Livro('Título 1', 'Autor 1', '2001', 'disponível')
livro2 = Livro('Título 2', 'Autor 2', '2002', 'indisponivel')
livro3 = Livro('Título 3', 'Autor 3', '2003', 'disponível')


minhaBiblioteca = Biblioteca()
minhaBiblioteca.adicoinarLivro(livro1)
minhaBiblioteca.adicoinarLivro(livro2)
minhaBiblioteca.adicoinarLivro(livro3)

print(minhaBiblioteca.lista)
minhaBiblioteca.listarLivros()
minhaBiblioteca.emprestarLivro("Título 3")
minhaBiblioteca.listarLivros()
