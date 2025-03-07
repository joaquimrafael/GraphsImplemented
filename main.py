# Implementação Atividade em Grupo do Projeto
# Joaquim Rafael M. P. Pereira 10408805
# Antonio Carlos Sciamarelli Neto 10409160
# Henrique Arabe Neres de Farias 10410152

import classes.filaCircular as fc
import classes.grafoLista as gl
import classes.grafoMatriz as gm
import classes.pilha as p

# Extensão da classe de Grafo Direcionado em Matriz de Adjacencia 
class TGrafoMatrizD(gm.Grafo):

    # EX01
    def inDegree(self,v):
        degree = 0
        for i in range (self.n):
            if self.adj[i][v] == 1:
                degree+=1
        
        return degree
    
    # EX02
    def outDegree(self, v):
        degree = 0
        for j in range (self.n):
            if self.adj[v][j] == 1:
                degree+=1
        
        return degree
    
    # EX03
    def degree(self, v):
        return self.inDegree(v) + self.outDegree(v)
    
    # EX04
    def isSource(self, v):
        if self.inDegree(v) == 0:
            if self.outDegree(v) > 0:
                return 1
        return 0
    
    # EX05
    def isSink(self, v):
        if self.outDegree(v) == 0:
            if self.inDegree(v) > 0:
                return 1
        return 0
    
    # EX06
    def isSymetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j] != self.adj[j][i]:
                    return 0
        return 1
    
    # EX07
    @staticmethod
    def readGraphFromFile(filename: str):
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
        V = int(lines[0])
        A = int(lines[1])
        matriz = [[0 for _ in range(V)] for _ in range(V)]
        for line in lines[2:]:
            v, w = map(int,line.split())
            matriz[v][w] = 1
        return matriz

    # EX13
    def isComplete(self):
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    continue
                if self.adj[i][j] == 0:
                    return 0
        return 1
    
    # EX14
    def complement(self):
        gComplement = TGrafoMatrizD(self.n)
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j] == 0:
                    gComplement.insereA(i,j)
        return gComplement
    
    # EX16
    def connectivityCategory(self):
        n = self.n

        def dfs_directed(start):
            visited = [False] * n
            stack = [start]
            visited[start] = True
            while stack:
                v = stack.pop()
                for w in range(n):
                    if self.adj[v][w] == 1 and not visited[w]:
                        visited[w] = True
                        stack.append(w)
            return visited
        
        strongly = True
        for v in range(n):
            if not all(dfs_directed(v)):
                strongly = False
                break
        if strongly:
            return 3
        
        for v in range(n):
            if all(dfs_directed(v)):
                return 2
            
        def dfs_undirected(start):
            visited = [False] * n
            stack = [start]
            visited[start] = True
            while stack:
                v = stack.pop()
                for w in range(n):
                    if(self.adj[v][w] == 1 or self.adj[w][v] == 1) and not visited[w]:
                        visited[w] = True
                        stack.append(w)
                return visited
            
        if all(dfs_undirected(0)):
            return 1
        
        return 0
    
    # EX17
    def reducedGraph(self):
        n = self.n
        visited = [False] * n
        order = []

        def dfs(v):
            visited[v] = True
            for w in range(n):
                if self.adj[v][w] == 1 and not visited[w]:
                    dfs(w)
                order.append(v)
        for v in range(n):
            if not visited[v]:
                dfs(v)

        transpose = [[self.adj[j][i] for j in range(n)] for i in range(n)]

        visited = [False] * n
        comp = [-1] * n
        current_component = 0

        def dfs_tranposed(v):
            visited[v] = True
            comp[v] = current_component
            for w in range(n):
                if transpose[v][w] == 1 and not visited[w]:
                    dfs_tranposed(w)
        for v in reversed(order):
            if not visited[v]:
                dfs_tranposed(v)
                current_component += 1
        
        reduced = TGrafoMatrizD(current_component)
        for v in range(n):
            for w in range(n):
                if self.adj[v][w] == 1 and comp[v] != comp[w]:
                    if reduced.adj[comp[v]][comp[w]] == 0:
                        reduced.adj[comp[v]][comp[w]] = 1
                        reduced.m += 1
        return reduced
    
class TGrafoMatrizRotuladoD(gm.Grafo):
    def __init__(self,n):
        super().__init__(n)
        self.adj = [[0.0 for _ in range(n)] for _ in range(n)]
    
    def insereA(self, v, w, peso: float):
        if self.adj[v][w] == 0.0:
            self.adj[v][w] = peso
            self.m += 1
    
    def removeA(self, v, w):
        if self.adj[v][w] != 0.0:
            self.adj[v][w] = 0.0
            self.m -= 1

    def show(self):
        print(f"\n n: {self.n} m: {self.m}\n")
        for i in range(self.n):
            for j in range(self.n):
                print(f"{self.adj[i][j]:6.2f}", end= " ")
            print()
        print("\nfim da impressão do grafo.")




# Extensão da classe de Grafo Nao Direcionado em Matriz de Adjacencia 
class TGrafoMatrizND(gm.Grafo):

    # EX08
    def insereA(self, v, w):
        if self.adj[v][w] == 0:
            self.adj[v][w] = 1
            self.adj[w][v] = 1
            self.m += 1
    
    def removeA(self, v, w):
        if self.adj[v][w] == 1:
            self.adj[v][w] = 0
            self.adj[w][v] = 0
            self.m -= 1
    
    def show(self):
        print(f"n: {self.n} m: {self.m}")
        for i in range(self.n):
            for j in range(self.n):
                print(f"{self.adj[i][j]:2d}", end=" ")
            print()

    # EX09
    def degree(self, v: int) -> int:
        return sum(self.adj[v])

    # EX15
    def isConnected(self):
        visited = [0]* self.n
        stack = p.Pilha(self.n)
        stack.push(0)
        visited[0] = 1
        
        while not stack.isEmpty():
            v = stack.pop()
            for j in range(self.n):
                if self.adj[v][j] == 1 and visited[j] == 0:
                    stack.push(j)
                    visited[j] = 1
        
        return int(all(visited))


# Extensão da classe de Grafo Direcionado em Lista de Adjacencia
class TGrafoListaD(gl.Grafo):
    # EX22
    def isEqual(self, g):
        if self.n != g.n or self.m != g.m:
            return 0
        else:
            for i in range(self.n):
                if set(self.listaAdj[i]) != set(g.listaAdj[i]):
                    return 0
        return 1
    
    # EX 23
    def invert(self):
        for i in range(self.n):
            self.listaAdj[i].reverse()
        return self
    
    # EX25
    def isSource(self, v: int) -> int:
        in_degree = 0
        for i in range(self.n):
            if v in self.listaAdj[i]:
                in_degree += 1
        out_degree = len(self.listaAdj[v])
        if in_degree == 0 and out_degree > 0:
            return 1
        else:
            return 0
        
    # EX26

    def isSink(self, v: int) -> int:
        in_degree = 0

        for i in range(self.n):
            if v in self.listaAdj[i]:
                in_degree += 1
        out_degree = len(self.listaAdj[v])
        if in_degree > 0 and out_degree == 0:
            return 1
        else:
            return 0
        
    # EX27

    def isSymetric(self) -> int:

        for v in range(self.n):
            for w in self.listaAdj[v]:
                if v not in self.listaAdj[w]:
                    return 0
        return 1
    
    # EX30

    def remove(self, v: int):

        for i in range(self.n):
            if i!= v:
                nova_lista = []
                for w in self.listaAdj[i]:
                    if w == v:
                        self.m -= 1
                    elif w > v:
                        nova_lista.append(w-1)
                    else:
                        nova_lista.append(w)
                self.listaAdj[i] = nova_lista

        num_outgoing = len(self.listaAdj[v])
        self.listaAdj.pop(v)
        self.n -= 1
        self.m -= num_outgoing

        return self        

# Extensão da classe de Grafo Nao Direcionado em Lista de Adjacencia
class TGrafoListaND(gl.Grafo):
    # EX 23
    def invert(self):
        for i in range(self.n):
            self.listaAdj[i].reverse()
        return self
    
    # EX 29
    def remove(self, v):
        for i in range(self.n):
            new_list = []
            for j in self.listaAdj[i]:
                if j == v:
                    self.m -= 1
                elif j > v:
                    new_list.append(j - 1)
                else:
                    new_list.append(j)
            self.listaAdj[i] = new_list
                
        self.listaAdj.pop(v)
        self.n -= 1
        return self

# EX23
@staticmethod
def fromMatrixToList(matrix: gm.Grafo):
    g = TGrafoListaD(matrix.n)
    for i in range(matrix.n):
        for j in range(matrix.n):
            if matrix.adj[i][j] > 0:
                g.insereA(i,j)
    return g

@staticmethod
def fromListToMatrix(lista: gl.Grafo):
    g = TGrafoMatrizD(lista.n)
    for i in range(lista.n):
        for j in lista.listaAdj[i]:
            g.insereA(i,j)
    return g
        
    
    
def main():    
    
    print("Testes: TGrafoMatrizDirecionado\n")
    
    gm_dir = TGrafoMatrizD(5)
    gm_dir.insereA(1,3)
    gm_dir.insereA(1,4)
    gm_dir.insereA(3,4)
    gm_dir.insereA(2,1)
    gm_dir.insereA(2,3)

    print("Grafo Direcionado 1:")
    gm_dir.show()

    # Teste EX01
    print("\nGrau de entrada do vértice 4:", gm_dir.inDegree(4))
    
    # Teste EX02    
    print("\nGrau de saída do vértice 1:", gm_dir.outDegree(1))
    
    # Teste EX03
    print("\nGrau do vértice:", gm_dir.degree(1))
    
    # Teste EX04
    print("\nVértice 2 é fonte?(1=S/0=N) ->", gm_dir.isSource(2))
    print("\nVértice 1 é fonte?(1=S/0=N) ->", gm_dir.isSource(1))
    
    # Teste EX05
    print("\nVértice 3 é sorvedouro?(1=S/0=N) ->", gm_dir.isSink(3))
    print("\nVértice 4 é sorvedouro?(1=S/0=N) ->", gm_dir.isSink(4))
    
    # Teste EX06
    print("\nO grafo 1 é simétrico?(1=S/0=N) ->", gm_dir.isSymetric())
    
    gm_dir2 = TGrafoMatrizD(4)
    gm_dir2.insereA(1,2)
    gm_dir2.insereA(1,3)
    gm_dir2.insereA(2,1)
    gm_dir2.insereA(3,1)
    gm_dir2.insereA(0,1)
    gm_dir2.insereA(1,0)
    
    print("\nGrafo Direcionado 2:")
    gm_dir2.show()
    
    print("\nO grafo 2 é simétrico?(1=S/0=N) ->", gm_dir2.isSymetric())
    
    # Teste EX13
    gm_dir3 = TGrafoMatrizD(3)
    gm_dir3.insereA(1,2)
    gm_dir3.insereA(1,0)
    gm_dir3.insereA(2,1)
    gm_dir3.insereA(2,0)
    gm_dir3.insereA(0,1)
    gm_dir3.insereA(0,2)
    
    print("\nGrafo Direcionado 3:")
    gm_dir3.show()
    
    print("\nO grafo 1 é completo?(1=S/0=N) ->", gm_dir.isComplete())
    print("\nO grafo 3 é completo?(1=S/0=N) ->", gm_dir3.isComplete())
    
    # Teste EX14
    print("\nGrafo Complementar do Grafo 1:")
    gm_dir.complement().show()
    
    gm_ndir = TGrafoMatrizD(3)
    gm_ndir.insereA(1,2)
    gm_ndir.insereA(1,0)
    gm_ndir.insereA(2,1)
    
    print("\nGrafo Complementar do Grafo ND:")
    gm_ndir.show()
    gm_ndir.complement().show()
    
    # Teste EX15    
    print("\nTeste: TGrafoMatrizNaoDirecionado")
    gm_nd = TGrafoMatrizND(5)
    gm_nd.insereA(1,3)
    gm_nd.insereA(1,4)
    gm_nd.insereA(3,4)
    gm_nd.insereA(2,1)
    
    print("\nGrafo Não Direcionado 1:")
    gm_nd.show()
    
    print("\nO grafo 1 é conexo?(1=S/0=N) ->", gm_nd.isConnected())
    
    gm_nd2 = TGrafoMatrizND(3)
    gm_nd2.insereA(1,2)
    gm_nd2.insereA(1,0)
    gm_nd2.insereA(2,0)
    
    print("\nGrafo Não Direcionado 2:")
    gm_nd2.show()
    
    print("\nO grafo 2 é conexo?(1=S/0=N) ->", gm_nd2.isConnected())

    # EX07 Teste

    print("Starting main.py")

    filename = "grafo.txt"
    matriz = TGrafoMatrizD.readGraphFromFile(filename)

    print("Matriz de Adjacência: ")
    for linha in matriz:
        print(linha)

    # EX08 Teste

    print("\nTeste: Grafo Não Direcionado (Matriz de Adjacência)")
    gm_nd = TGrafoMatrizND(5)
    gm_nd.insereA(0,1)
    gm_nd.insereA(0,2)
    gm_nd.insereA(1,2)
    gm_nd.insereA(3,4)
    
    print("Grafo após inserção das arestas:")
    gm_nd.show()

    gm_nd.removeA(0,2)

    print("\nGrafo após remoção das arestas entre 0 e 2:")
    gm_nd.show()


    # EX09 Teste

    print("\nTeste: Grau de vértice em Grafo Não Direcionado (Matriz)")

    gm_nd = TGrafoMatrizND(5)

    gm_nd.insereA(0,1)
    gm_nd.insereA(0,2)
    gm_nd.insereA(1,2)
    gm_nd.insereA(3,4)

    gm_nd.show()

    for v in range(gm_nd.n):
        print(f"Vértice {v}: grau = {gm_nd.degree(v)}")

    # EX16 Teste

    g = TGrafoMatrizD(4)

    g.insereA(0,1)
    g.insereA(1,2)
    g.insereA(2,0)
    g.insereA(2,3)
    g.insereA(3,2)

    categoria = g.connectivityCategory()
    print("\nCategoria de conectividade: ",categoria)

    # EX17 Teste

    print("\nTeste: Grafo Reduzido")

    gt = TGrafoMatrizD(6)

    gt.insereA(0,1)
    gt.insereA(1,2)
    gt.insereA(2,0)
    gt.insereA(3,4)
    gt.insereA(4,3)
    gt.insereA(2,3)
    gt.insereA(4,5)

    print("Grafo original:")
    gt.show()

    reduced = gt.reducedGraph()
    print("\nGrafo reduzido:")
    reduced.show()

    # EX22 Teste
    gl_d = TGrafoListaD(4)
    gl_d.insereA(0, 2)
    gl_d.insereA(0, 1)
    gl_d.insereA(1, 2)
    gl_d.insereA(2, 3)

    gl2_d = TGrafoListaD(4)
    gl2_d.insereA(0, 1)
    gl2_d.insereA(0, 2)
    gl2_d.insereA(1, 2)
    gl2_d.insereA(2, 3)

    print("Grafo gl_d:")
    gl_d.show()
    print("\nGrafo gl2_d:")
    gl2_d.show()

    if gl_d.isEqual(gl2_d):
        print("\nOs grafos gl1_d e gl2_d são iguais.")
    else:
        print("\nOs grafos gl1_d e gl2_d NÃO são iguais.")
        
    # EX23 Teste
    print("\nTeste: fromMatrixToList")
    glm_d = fromMatrixToList(gm_dir)
    
    glm_d.show()
    
    print("\nTeste: fromListToMatrix")
    gml_d = fromListToMatrix(gl_d)
    
    gml_d.show()
    
    # EX24 Teste
    glTeste = TGrafoListaD(4)
    glTeste.insereA(0, 1)
    glTeste.insereA(2, 3)
    glTeste.insereA(1, 2)
    glTeste.insereA(0, 3)
    glTeste.insereA(1 ,3)
    glTeste.show()
    glTeste.invert().show()
    
    print("\nTeste: TGrafoListaNaoDirecionado")
    gl_nd = TGrafoListaND(5)
    gl_nd.insereA(0,1)
    gl_nd.insereA(0,2)
    gl_nd.insereA(1,2)
    gl_nd.insereA(3,4)
    gl_nd.insereA(3,0)
    gl_nd.insereA(3,1)
    gl_nd.insereA(4,0)
    
    print("Grafo Não Direcionado 1:")
    gl_nd.show()
    
    print("\nGrafo invertido:")
    gl_nd.invert().show()
    
    # EX29 Teste
    print("Grafo Não Direcionado:")
    gl_nd.show()
    print("\nTeste: Remoção de vértice")
    gl_nd.remove(0).show()

    # EX18 Teste

    print("Teste: Grafo Direcionado Rotulado (Matriz de Adjacência)")

    g = TGrafoMatrizRotuladoD(5)
    g.insereA(0, 1, 2.5)
    g.insereA(0, 2, 1.75)
    g.insereA(1, 3, 3.0)
    g.insereA(2, 3, 4.25)
    g.insereA(3, 4, 0.5)

    g.show()

    # EX25 Teste

    g = TGrafoListaD(4)
    g.insereA(0, 1)
    g.insereA(0, 2)
    g.insereA(1, 2)
    g.insereA(2, 3)

    print("\nGrafo (lista de adjacência):")
    g.show()

    for v in range(g.n):
        if g.isSource(v):
            print(f"Vértice {v} é fonte.")
        else:
            print(f"Vértice {v} NÃO é fonte.")

    # EX26 Teste

    g = TGrafoListaD(4)
    g.insereA(0, 3)
    g.insereA(1, 3)
    g.insereA(2, 3)

    g.insereA(0, 1)
    g.insereA(1, 2)

    g.show()

    if g.isSink(3):
        print("\nVértice 3 é soverdouro.")
    else:
        print("\nVértice 3 NÃO é soverdouro.")

    # EX27 Teste

    g = TGrafoListaD(4)
    g.insereA(0, 1)
    g.insereA(1, 0)
    g.insereA(0, 2)
    g.insereA(2, 0)
    g.insereA(1, 2)
    g.insereA(2, 1)

    g.insereA(3, 0)

    g.show()

    if g.isSymetric():
        print("\nO grafo é simétrico.")
    else:
        print("\nO grafo NÃO é simétrico.")
    
    # EX 30 Teste

    g = TGrafoListaD(5)
    g.insereA(0, 1)
    g.insereA(0, 3)
    g.insereA(1, 2)
    g.insereA(2, 4)
    g.insereA(3, 4)
    g.insereA(4, 0)

    print("Grafo original:")
    g.show()

    g.remove(2)

    print("\nGrafo após remover o vértice 2:")
    g.show()

if __name__ == '__main__':
    main()
