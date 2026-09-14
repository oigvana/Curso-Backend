from abc import ABC, abstractmethod

class ItemAcervo(ABC):

    def __init__(self, titulo: str):
        self.titulo = titulo
        self.__disponivel = True

    def emprestar(self) -> bool:
        if self.__disponivel:
            self.__disponivel = False
            print(f'"{self.titulo}" foi emprestado.')
            return True

        print(f'"{self.titulo}" não está disponível para empréstimo.')
        return False

    def devolver(self) -> None:
        self.__disponivel = True
        print(f'"{self.titulo}" foi devolvido.')

    def esta_disponivel(self) -> bool:
        return self.__disponivel

    @abstractmethod
    def descricao(self) -> str:
        pass


class Livro(ItemAcervo):

    def __init__(self, titulo: str, autor: str):
        super().__init__(titulo)
        self.autor = autor

    def descricao(self) -> str:
        status = "disponível" if self.esta_disponivel() else "emprestado"
        return f'Livro: "{self.titulo}" de {self.autor} ({status})'


class Revista(ItemAcervo):

    def __init__(self, titulo: str, edicao: int):
        super().__init__(titulo)
        self.edicao = edicao

    def descricao(self) -> str:
        status = "disponível" if self.esta_disponivel() else "emprestada"
        return f'Revista: "{self.titulo}" - Edição {self.edicao} ({status})'


class Biblioteca:

    def __init__(self):
        self.__itens = []

    def adicionar_item(self, item: ItemAcervo) -> None:
        self.__itens.append(item)
        print(f'"{item.titulo}" foi adicionado ao acervo.')

    def remover_item(self, titulo: str) -> bool:
        for item in self.__itens:
            if item.titulo.lower() == titulo.lower():
                self.__itens.remove(item)
                print(f'"{item.titulo}" foi removido do acervo.')
                return True

        print(f'"{titulo}" não foi encontrado no acervo.')
        return False

    def listar_itens(self) -> None:
        if not self.__itens:
            print("O acervo está vazio.")
            return

        print("\n=== ACERVO ===")

        for i, item in enumerate(self.__itens, start=1):
            print(f"{i} - {item.descricao()}")

    def buscar_por_titulo(self, titulo: str) -> None:
        encontrados = []

        for item in self.__itens:
            if titulo.lower() in item.titulo.lower():
                encontrados.append(item)

        if encontrados:
            print("\n=== RESULTADO DA BUSCA ===")
            for item in encontrados:
                print(item.descricao())
        else:
            print(f'Nenhum item encontrado com o título "{titulo}".')

    def emprestar_item(self, titulo: str) -> bool:
        for item in self.__itens:
            if item.titulo.lower() == titulo.lower():
                return item.emprestar()

        print(f'"{titulo}" não foi encontrado no acervo.')
        return False

    def devolver_item(self, titulo: str) -> bool:
        for item in self.__itens:
            if item.titulo.lower() == titulo.lower():
                item.devolver()
                return True

        print(f'"{titulo}" não foi encontrado no acervo.')
        return False


if __name__ == "__main__":

    biblioteca = Biblioteca()

    livro1 = Livro("O Massacre da Residência Hope", "Riley Sager")
    livro2 = Livro("Game of Thrones", "George R. R. Martin")
    livro3 = Livro("Olhos d'água", "Conceição Evaristo")
    revista1 = Revista("Vogue", 123)

    biblioteca.adicionar_item(livro1)
    biblioteca.adicionar_item(livro2)
    biblioteca.adicionar_item(livro3)
    biblioteca.adicionar_item(revista1)

    while True:

        print("\n=== MENU ===")
        print("1 - Listar itens")
        print("2 - Adicionar item")
        print("3 - Remover item")
        print("4 - Buscar item por título")
        print("5 - Emprestar item")
        print("6 - Devolver item")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            biblioteca.listar_itens()

        elif opcao == "2":

            print("\n=== ADICIONAR ITEM ===")
            print("1 - Livro")
            print("2 - Revista")

            tipo = input("Escolha o tipo: ")

            if tipo == "1":

                titulo = input("Digite o título: ")
                autor = input("Digite o autor: ")

                biblioteca.adicionar_item(
                    Livro(titulo, autor)
                )

            elif tipo == "2":

                titulo = input("Digite o título: ")

                try:
                    edicao = int(input("Digite a edição: "))

                    biblioteca.adicionar_item(
                        Revista(titulo, edicao)
                    )

                except ValueError:
                    print("A edição deve ser um número.")

            else:
                print("Tipo inválido.")

        elif opcao == "3":

            titulo = input("Digite o título do item que deseja remover: ")
            biblioteca.remover_item(titulo)

        elif opcao == "4":

            titulo = input("Digite o título que deseja buscar: ")
            biblioteca.buscar_por_titulo(titulo)

        elif opcao == "5":

            biblioteca.listar_itens()

            titulo = input(
                "\nDigite o título do item que deseja emprestar: "
            )

            biblioteca.emprestar_item(titulo)

        elif opcao == "6":

            biblioteca.listar_itens()

            titulo = input(
                "\nDigite o título do item que deseja devolver: "
            )

            biblioteca.devolver_item(titulo)

        elif opcao == "7":

            print("Programa encerrado.")
            break

        else:

            print("Opção inválida. Escolha uma opção de 1 a 7.")