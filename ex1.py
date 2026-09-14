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
        """Retorna a descrição do item."""
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


def imprimir_descricoes(itens: list[ItemAcervo]) -> None:
    for i, item in enumerate(itens, start=1):
        print(f"{i} - {item.descricao()}")


if __name__ == "__main__":
    acervo = [
        Livro("O Massacre da Residência Hope", "Riley Sager"),
        Livro("Game of Thrones", "George R. R. Martin"),
        Livro("Olhos d'água", "Conceição Evaristo"),
        Revista("Vogue", 123)
    ]

    while True:
        print("\n=== MENU ===")
        print("1 - Ver acervo")
        print("2 - Emprestar item")
        print("3 - Devolver item")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n=== ACERVO ===")
            imprimir_descricoes(acervo)

        elif opcao == "2":
            print("\n=== ESCOLHA O ITEM PARA EMPRESTAR ===")
            imprimir_descricoes(acervo)

            try:
                numero = int(input("Digite o número do item: "))

                if 1 <= numero <= len(acervo):
                    acervo[numero - 1].emprestar()
                else:
                    print("Item inválido.")

            except ValueError:
                print("Digite apenas um número.")

        elif opcao == "3":
            print("\n=== ESCOLHA O ITEM PARA DEVOLVER ===")
            imprimir_descricoes(acervo)

            try:
                numero = int(input("Digite o número do item: "))

                if 1 <= numero <= len(acervo):
                    acervo[numero - 1].devolver()
                else:
                    print("Item inválido.")

            except ValueError:
                print("Digite apenas um número.")

        elif opcao == "4":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Escolha uma opção de 1 a 4.")
