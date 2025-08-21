from datetime import date, timedelta
        
class Item:
    def __init__(self, codigo, titulo, ano, estoque=1, tipo="item"):
        self.codigo = codigo
        self.titulo = titulo
        self.ano = ano
        self.estoque = estoque
        self.tipo = tipo
    
    def dias_de_emprestimo(self):
        return 14
    
    def __str__(self):
        return f"{self.tipo.title()}('{self.titulo}', {self.ano})"

class Livro(Item):
    def __init__(self, codigo, titulo, ano, estoque=1):
        super().__init__(codigo, titulo, ano, estoque, tipo="livro")

    def dias_de_emprestimo(self):
        return 7
    
    def __str__(self):
        return f"{self.tipo.title()}('{self.titulo}', {self.ano})"
        
class Revista(Item):
    def __init__(self, codigo, titulo, ano, estoque=1):
        super().__init__(codigo, titulo, ano, estoque, tipo="revista")

    def dias_de_emprestimo(self):
        return 14
        
    def __str__(self):
        return f"{self.tipo.title()}('{self.titulo}', {self.ano})"

class Usuario:
    def __init__(self, id_usuario, nome, limite_emprestimos=3):
        self.id_usuario = id_usuario
        self.nome = nome
        self.limite_emprestimos = limite_emprestimos
        self.itens_emprestados = []

class Professor(Usuario):
    def __init__(self, id_usuario, nome, limite_emprestimos=5):
        super().__init__(id_usuario, nome, limite_emprestimos)
        
        
class Aluno(Usuario):
    def __init__(self, id_usuario, nome, limite_emprestimos=3):
        super().__init__(id_usuario, nome, limite_emprestimos)

class Emprestimo:
    def __init__(self, item, usuario, data=None):
        self.item = item
        self.usuario = usuario
        self.data_emprestimo = data or date.today()
        self.data_devolucao = None
        self.prazo = self.data_emprestimo + timedelta(days=item.dias_de_emprestimo())

    @property
    def em_aberto(self):
        return self.data_devolucao is None

    @property
    def dias_atraso(self):
        data_fim = self.data_devolucao or date.today()
        if data_fim > self.prazo:
            return (data_fim - self.prazo).days
        return 0
    
    
    @property
    def multa(self):
        return self.dias_atraso * 2.5

    def devolver(self):
        if not self.em_aberto:
            raise ValueError("Empréstimo já devolvido.")
        self.data_devolucao = date.today()

    def __str__(self):
        status = "aberto" if self.em_aberto else f"devolvido em {self.data_devolucao}"
        atraso = ""
        if self.dias_atraso > 0:
            atraso = f" | fora do prazo: {self.dias_atraso} dias | multa: R${self.multa:.2f}"
        return f"[{status}] {self.item} -> {self.usuario.nome} (prazo {self.prazo}){atraso}"
    
    
    
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = {}
        self.usuarios = {}
        self.__emprestimos = []
        
    @property
    def emprestimos(self):
        return list(self.__emprestimos)
    

    def adicionar_item(self, item):
        if item.codigo in self.catalogo:
            raise ValueError("Código já cadastrado.")
        self.catalogo[item.codigo] = item

    def buscar_item(self, codigo):
        if codigo not in self.catalogo:
            raise KeyError("Item não encontrado.")
        return self.catalogo[codigo]

    def cadastrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            raise ValueError("Usuário já cadastrado.")
        self.usuarios[usuario.id_usuario] = usuario

    def buscar_usuario(self, id_usuario):
        if id_usuario not in self.usuarios:
            raise KeyError("Usuário não encontrado.")
        return self.usuarios[id_usuario]

    def emprestar(self, id_usuario, codigo_item):
        usuario = self.buscar_usuario(id_usuario)
        item = self.buscar_item(codigo_item)
        if len(usuario.itens_emprestados) >= usuario.limite_emprestimos:
            raise PermissionError("Usuário atingiu o limite de empréstimos.")
        if item.estoque <= 0:
            raise ValueError("Sem unidades disponíveis.")
        item.estoque -= 1
        emp = Emprestimo(item, usuario)
        usuario.itens_emprestados.append(emp)
        self.__emprestimos.append(emp)
        return emp

    def devolver(self, id_usuario, codigo_item):
        usuario = self.buscar_usuario(id_usuario)
        item = self.buscar_item(codigo_item)
        alvo = None
        for e in self.__emprestimos:
            if e.usuario is usuario and e.item is item and e.em_aberto:
                alvo = e
                break
        if not alvo:
            raise LookupError("Empréstimo em aberto não encontrado.")
        alvo.devolver()
        item.estoque += 1
        usuario.itens_emprestados = [e for e in usuario.itens_emprestados if e is not alvo]

    def listar_itens(self):
        return [f"{i.codigo}: {i} | estoque={i.estoque}" for i in self.catalogo.values()]

    def listar_usuarios(self):
        return [f"{u.id_usuario}: {u.nome} ({len(u.itens_emprestados)} empréstimo(s))"
                for u in self.usuarios.values()]

    def listar_emprestimos_abertos(self):
        return [e for e in self.__emprestimos if e.em_aberto]

    def pesquisar_itens(self, termo):
        t = (termo or "").strip().lower()
        if not t:
            return list(self.catalogo.values())
        achados = []
        for item in self.catalogo.values():
            if (t in str(item.codigo).lower()
                or t in str(item.titulo).lower()
                or t in str(item.tipo).lower()):
                achados.append(item)
        return achados

    def pesquisar_usuarios(self, termo):
        t = (termo or "").strip().lower()
        if not t:
            return list(self.usuarios.values())
        achados = []
        for u in self.usuarios.values():
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

        return [e for e in self.__emprestimos if casa(e)]


    def demo_polimorfismo():
        itens = [
            Livro("L-001", "Clean Code", 2008),
            Revista("R-101", "Ciência Hoje #250", 2024),
            Item("I-500", "handmen", 2010)
        ]

        def demo():
            print(">>> Biblioteca base")
            bib = Biblioteca("Biblioteca Central")
            bib.adicionar_item(Livro("I-001", "Clean Code", 2008, estoque=2))
            bib.adicionar_item(Livro("I-002", "Python Fluente", 2015, estoque=1))
            bib.adicionar_item(Revista("I-003", "Ciência Hoje #250", 2024, estoque=3))
            bib.cadastrar_usuario(Professor("u1", "Ana"))
            bib.cadastrar_usuario(Aluno("u2", "Bruno"))
            bib.emprestar("u1", "I-001")
            bib.emprestar("u1", "I-003")
            bib.emprestar("u2", "I-002")
            bib.devolver("u1", "I-003")

if __name__ == "__main__":
    bib = Biblioteca("Biblioteca Central")
    while True:
            print("\n=== MENU PRINCIPAL ===")
            print("[1] Adicionar")
            print("[2] Pesquisar")
            print("[0] Sair")
            escolha = input("Escolha uma opção: ").strip()
    
            if escolha == "0":
                print("Até mais...")
                break
    
            elif escolha == "1":
                while True:
                    print("\n--- ADICIONAR ---")
                    print("[1] Livro")
                    print("[2] Revista")
                    print("[3] Usuário")
                    print("[4] Empréstimo")
                    print("[0] Voltar")
                    subop = input("Escolha: ").strip()
    
                    if subop == "0":
                        break
    
                    elif subop == "1":
                        print("\n>>> Adicionar Livro")
                        codigo = input("Código: ").strip()
                        titulo = input("Título: ").strip()
                        ano = int(input("Ano: "))
                        estoque = int(input("Estoque: "))
                        try:
                            livro = Livro(codigo, titulo, ano, estoque)
                            bib.adicionar_item(livro)
                            print("Livro adicionado com sucesso.")
                        except ValueError as ve:
                            print("Erro:", ve)
    
                    elif subop == "2":
                        print("\n>>> Adicionar Revista")
                        codigo = input("Código: ").strip()
                        titulo = input("Título: ").strip()
                        ano = int(input("Ano: "))
                        estoque = int(input("Estoque: "))
                        try:
                            revista = Revista(codigo, titulo, ano, estoque)
                            bib.adicionar_item(revista)
                            print("Revista adicionada com sucesso.")
                        except ValueError as ve:
                            print("Erro:", ve)
    
                    elif subop == "3":
                        print("\n>>> Adicionar Usuário")
                        id_usuario = input("ID: ").strip()
                        nome = input("Nome: ").strip()
                        tipo = input("Tipo [professor/aluno]: ").strip().lower()
                        if tipo == "professor":
                            usuario = Professor(id_usuario, nome)
                        else:
                            usuario = Aluno(id_usuario, nome)
                        try:
                            bib.cadastrar_usuario(usuario)
                            print("Usuário cadastrado com sucesso.")
                        except ValueError as ve:
                            print("Erro:", ve)
    
                    elif subop == "4":
                        while True:
                            print("\n>>> EMPRÉSTIMO <<<")
                            print("[1] Realizar empréstimo")
                            print("[2] Devolver item")
                            print("[0] Voltar")
                            op_emp = input("Escolha: ").strip()
    
                            if op_emp == "0":
                                break
    
                            elif op_emp == "1":
                                print("\n>>> Realizar Empréstimo")
                                id_usuario = input("ID do usuário: ").strip()
                                codigo_item = input("Código do item: ").strip()
                                try:
                                    emp = bib.emprestar(id_usuario, codigo_item)
                                    print("Empréstimo realizado com sucesso:")
                                    print(emp)
                                except (KeyError, ValueError, PermissionError) as e:
                                    print("Erro:", e)
    
                            elif op_emp == "2":
                                print("\n>>> Devolver Item")
                                id_usuario = input("ID do usuário: ").strip()
                                codigo_item = input("Código do item: ").strip()
                                try:
                                    bib.devolver(id_usuario, codigo_item)
                                    print("Item devolvido com sucesso.")
                                except (KeyError, LookupError, ValueError) as e:
                                    print("Erro:", e)
    
                            else:
                                print("Opção inválida.")
    
                    else:
                        print("Opção inválida.")
    
            elif escolha == "2":
                while True:
                    print("\n=== PESQUISAS ===")
                    print("[1] Pesquisar ITENS (por código, título ou tipo)")
                    print("[2] Pesquisar USUÁRIOS (por id ou nome)")
                    print("[3] Pesquisar EMPRÉSTIMOS (por item/usuário)")
                    print("[0] Voltar")
                    op = input("Escolha: ").strip().lower()
    
                    if op == "0":
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
                        termo = input("Termo (item/usuário; vazio lista todos): ").lower()
                        status = input("Status [enter=Todos | aberto | devolvido]: ").lower()
    
                        achou = False
                        for e in bib.emprestimos:
                            usuario_ok = termo in e.usuario.nome.lower() or termo in e.usuario.id_usuario.lower()
                            item_ok = termo in e.item.titulo.lower() or termo in e.item.codigo.lower()
                            if (not termo or usuario_ok or item_ok):
                                if (not status) or (status == "aberto" and e.em_aberto) or (status == "devolvido" and not e.em_aberto):
                                    print(e)
                                    achou = True
                        if not achou:
                            print("Nenhum empréstimo encontrado.")
    
            else:
                print("Opção inválida.")
