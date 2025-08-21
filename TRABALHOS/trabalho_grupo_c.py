from datetime import date, timedelta
from abc import ABC, abstractmethod

# ===== ABSTRAÇÃO E ENCAPSULAMENTO =====
class Item(ABC):
    def __init__(self, codigo, titulo, ano, estoque=1, tipo="item"):
        self._codigo = codigo
        self._titulo = titulo
        self._ano = ano
        self._estoque = estoque
        self._tipo = tipo
    
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def ano(self):
        return self._ano
    
    @property
    def estoque(self):
        return self._estoque
    
    @estoque.setter
    def estoque(self, valor):
        if valor < 0:
            raise ValueError("Estoque não pode ser negativo")
        self._estoque = valor
    
    @property
    def tipo(self):
        return self._tipo
    
    @abstractmethod
    def dias_de_emprestimo(self):
        pass
    
    def __str__(self):
        return f"{self.tipo.title()}('{self.titulo}', {self.ano})"


# ===== HERANÇA =====
class Livro(Item):
    def __init__(self, codigo, titulo, ano, estoque=1, tipo="livro"):
        super().__init__(codigo, titulo, ano, estoque, tipo)
    
    def dias_de_emprestimo(self):
        return 14


class Revista(Item):
    def __init__(self, codigo, titulo, ano, estoque=1, tipo="revista"):
        super().__init__(codigo, titulo, ano, estoque, tipo)
    
    def dias_de_emprestimo(self):
        return 14


# ===== EMCPSULAMENTO =====
class Usuario:
    def __init__(self, id_usuario, nome, limite_emprestimos=3):
        self._id_usuario = id_usuario
        self._nome = nome
        self._limite_emprestimos = limite_emprestimos
        self._itens_emprestados = []
    
    @property
    def id_usuario(self):
        return self._id_usuario
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def limite_emprestimos(self):
        return self._limite_emprestimos
    
    @property
    def itens_emprestados(self):
        return self._itens_emprestados


# ===== EMCPSULAMENTO =====
class Emprestimo:
    def __init__(self, item, usuario, data=None):
        self._item = item
        self._usuario = usuario
        self._data_emprestimo = data or date.today()
        self._data_devolucao = None
        self._prazo = self._data_emprestimo + timedelta(days=item.dias_de_emprestimo())
    
    @property
    def item(self):
        return self._item
    
    @property
    def usuario(self):
        return self._usuario
    
    @property
    def data_emprestimo(self):
        return self._data_emprestimo
    
    @property
    def data_devolucao(self):
        return self._data_devolucao
    
    @property
    def prazo(self):
        return self._prazo
    
    @property
    def em_aberto(self):
        return self._data_devolucao is None
    
    def devolver(self):
        if not self.em_aberto:
            raise ValueError("Empréstimo já devolvido.")
        self._data_devolucao = date.today()
    
    def __str__(self):
        status = "aberto" if self.em_aberto else f"devolvido em {self.data_devolucao}"
        return f"[{status}] {self.item} -> {self.usuario.nome} (prazo {self.prazo})"


# ===== EMCPSULAMENTO =====
class Biblioteca:
    def __init__(self, nome):
        self._nome = nome
        self._catalogo = {}
        self._usuarios = {}
        self._emprestimos = []
    
    @property
    def nome(self):
        return self._nome

    def adicionar_item(self, item):
        if item.codigo in self._catalogo:
            raise ValueError("Código já cadastrado.")
        self._catalogo[item.codigo] = item

    def buscar_item(self, codigo):
        if codigo not in self._catalogo:
            raise KeyError("Item não encontrado.")
        return self._catalogo[codigo]

    def cadastrar_usuario(self, usuario):
        if usuario.id_usuario in self._usuarios:
            raise ValueError("Usuário já cadastrado.")
        self._usuarios[usuario.id_usuario] = usuario

    def buscar_usuario(self, id_usuario):
        if id_usuario not in self._usuarios:
            raise KeyError("Usuário não encontrado.")
        return self._usuarios[id_usuario]

    def emprestar(self, id_usuario, codigo_item):
        usuario = self.buscar_usuario(id_usuario)
        item = self.buscar_item(codigo_item)
        if len(usuario.itens_emprestados) >= usuario.limite_emprestimos:
            raise PermissionError("Usuário atingiu o limite de empréstimos.")
        if item.estoque <= 0:
            raise ValueError("Sem unidades disponíveis.")
        item.estoque -= 1
        emp = Emprestimo(item, usuario)
        usuario._itens_emprestados.append(emp)
        self._emprestimos.append(emp)
        return emp

    def devolver(self, id_usuario, codigo_item):
        usuario = self.buscar_usuario(id_usuario)
        item = self.buscar_item(codigo_item)
        alvo = None
        for e in self._emprestimos:
            if e.usuario is usuario and e.item is item and e.em_aberto:
                alvo = e
                break
        if not alvo:
            raise LookupError("Empréstimo em aberto não encontrado.")
        alvo.devolver()
        item.estoque += 1
        usuario._itens_emprestados = [e for e in usuario._itens_emprestados if e is not alvo]

    def listar_itens(self):
        return [f"{i.codigo}: {i} | estoque={i.estoque}" for i in self._catalogo.values()]

    def listar_usuarios(self):
        return [f"{u.id_usuario}: {u.nome} ({len(u.itens_emprestados)} empréstimo(s))"
                for u in self._usuarios.values()]

    def listar_emprestimos_abertos(self):
        return [e for e in self._emprestimos if e.em_aberto]

    def pesquisar_itens(self, termo):
        t = (termo or "").strip().lower()
        if not t:
            return list(self._catalogo.values())
        achados = []
        for item in self._catalogo.values():
            if (t in str(item.codigo).lower()
                or t in str(item.titulo).lower()
                or t in str(item.tipo).lower()):
                achados.append(item)
        return achados

    def pesquisar_usuarios(self, termo):
        t = (termo or "").strip().lower()
        if not t:
            return list(self._usuarios.values())
        achados = []
        for u in self._usuarios.values():
            if (t in str(u.id_usuario).lower()
                or t in str(u.nome).lower()):
                achados.append(u)
        return achados

    def pesquisar_emprestimos(self, termo, status=None):
        t = (termo or "").strip().lower()

        def casa(e):
            alvo = (
                t in str(e.item.codigo).lower()
                or t in str(e.item.titulo).lower()
                or t in str(e.usuario.id_usuario).lower()
                or t in str(e.usuario.nome).lower()
            ) if t else True
            if not alvo:
                return False
            if status == "aberto":
                return e.em_aberto
            if status == "devolvido":
                return not e.em_aberto
            return True

        return [e for e in self._emprestimos if casa(e)]


def demo():
    print(">>> Biblioteca base com POO")
    bib = Biblioteca("Biblioteca Central")
    
    # HERANÇA
    bib.adicionar_item(Livro("I-001", "Clean Code", 2008, estoque=2))
    bib.adicionar_item(Livro("I-002", "Python Fluente", 2015, estoque=1))
    bib.adicionar_item(Revista("I-003", "Ciência Hoje #250", 2024, estoque=3))
    
    bib.cadastrar_usuario(Usuario("u1", "Ana", limite_emprestimos=2))
    bib.cadastrar_usuario(Usuario("u2", "Bruno", limite_emprestimos=1))
    
    bib.emprestar("u1", "I-001")
    bib.emprestar("u1", "I-003")
    bib.emprestar("u2", "I-002")
    bib.devolver("u1", "I-003")

    while True:
        print("\n=== PESQUISAS ===")
        print("[1] Pesquisar ITENS (por código, título ou tipo)")
        print("[2] Pesquisar USUÁRIOS (por id ou nome)")
        print("[3] Pesquisar EMPRÉSTIMOS (por item/usuário)")
        print("[0] Sair")
        op = input("Escolha: ").strip().lower()

        if op == "0":
            print("Até mais...")
            break

        if op == "1":
            termo = input("Termo (se vazio lista todos): ").strip()
            achados = bib.pesquisar_itens(termo)
            if not achados:
                print("  Nenhum item encontrado.")
            else:
                for it in achados:
                    print(f"  {it.codigo}: {it} | estoque={it.estoque}")

        elif op == "2":
            termo = input("Termo (se vazio lista todos): ").strip()
            achados = bib.pesquisar_usuarios(termo)
            if not achados:
                print("  Nenhum usuário encontrado.")
            else:
                for u in achados:
                    print(f"  {u.id_usuario}: {u.nome} | empréstimos={len(u.itens_emprestados)}")

        elif op == "3":
            termo = input("Termo (item/usuário; vazio lista todos): ").strip()
            status = input("Status [enter=Todos | aberto | devolvido]: ").strip().lower() or None
            if status not in (None, "aberto", "devolvido"):
                print("  Status inválido. Usando 'Todos'.")
                status = None
            achados = bib.pesquisar_emprestimos(termo, status=status)
            if not achados:
                print("  Nenhum empréstimo encontrado.")
            else:
                for e in achados:
                    print("  ", e)
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    demo()