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


# Extensão da classe de Grafo Nao Direcionado em Matriz de Adjacencia 
class TGrafoMatrizND(gm.Grafo):
    
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
class TGrafoListaD(gm.Grafo):
    pass

# Extensão da classe de Grafo Nao Direcionado em Lista de Adjacencia
class TGrafoListaND(gm.Grafo):
    pass


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

    print("\nGrau de entrada do vértice 4:", gm_dir.inDegree(4))
    
    print("\nGrau de saída do vértice 1:", gm_dir.outDegree(1))
    
    print("\nGrau do vértice:", gm_dir.degree(1))
    
    print("\nVértice 2 é fonte?(1=S/0=N) ->", gm_dir.isSource(2))
    print("\nVértice 1 é fonte?(1=S/0=N) ->", gm_dir.isSource(1))
    
    print("\nVértice 3 é sorvedouro?(1=S/0=N) ->", gm_dir.isSink(3))
    print("\nVértice 4 é sorvedouro?(1=S/0=N) ->", gm_dir.isSink(4))
    
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
    
    gm_dir3 = TGrafoMatrizD(3)
    gm_dir3.insereA(1,2)
    gm_dir3.insereA(1,0)
    gm_dir3.insereA(2,1)
    gm_dir3.insereA(2,0)
    gm_dir3.insereA(0,1)
    gm_dir3.insereA(0,2)
    
    print("\nGrafo Direcionado 3:")
    gm_dir3.show()
    
    print("\nO grafo 3 é completo?(1=S/0=N) ->", gm_dir3.isComplete())
    
    print("\nGrafo Complementar do Grafo 1:")
    gm_dir.complement().show()
    
    
    print("\n")
    
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
    
    # print("\nTeste: TGrafoListaDirecionado")
    # gl_dir = TGrafoListaD(5)
    # print(gl_dir)
    
    # print("\nTeste: TGrafoListaNaoDirecionado")
    # gl_nd = TGrafoListaND(5)
    # print(gl_nd)

if __name__ == '__main__':
    main()
