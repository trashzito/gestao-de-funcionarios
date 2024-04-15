class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.status = "Disponível"

    def esta_disponivel(self):
        return self.status == "Disponível"

    def emprestar(self):
        if self.esta_disponivel():
            self.status = "Emprestado"
            return True
        else:
            return False

    def devolver(self):
        self.status = "Disponível"

# Módulo biblioteca
livros = []

def adicionar_livro(livro):
    livros.append(livro)

def emprestar_livro(titulo):
    for livro in livros:
        if livro.titulo == titulo:
            return livro.emprestar()
    return False

def devolver_livro(titulo):
    for livro in livros:
        if livro.titulo == titulo:
            livro.devolver()
            return True
    return False

def exibir_livros_disponiveis():
    print("Livros disponíveis na biblioteca:")
    for livro in livros:
        if livro.esta_disponivel():
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}")