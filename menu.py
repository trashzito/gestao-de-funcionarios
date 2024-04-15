import biblioteca

while True:
    print("\nMenu:")
    print("1. Adicionar livro")
    print("2. Emprestar livro")
    print("3. Devolver livro")
    print("4. Exibir livros disponíveis")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o nome do autor: ")
        ano = input("Digite o ano de publicação: ")
        livro = biblioteca.Livro(titulo, autor, ano)
        biblioteca.adicionar_livro(livro)
        print("Livro adicionado com sucesso!")
    elif opcao == "2":
        titulo = input("Digite o título do livro que deseja emprestar: ")
        if biblioteca.emprestar_livro(titulo):
            print("Livro emprestado com sucesso!")
        else:
            print("Livro não encontrado ou já emprestado.")
    elif opcao == "3":
        titulo = input("Digite o título do livro que deseja devolver: ")
        if biblioteca.devolver_livro(titulo):
            print("Livro devolvido com sucesso!")
        else:
            print("Livro não encontrado ou já disponível.")
    elif opcao == "4":
        biblioteca.exibir_livros_disponiveis()
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")