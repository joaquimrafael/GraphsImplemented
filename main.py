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



# Extensão da classe de Grafo Nao Direcionado em Matriz de Adjacencia 
class TGrafoMatrizND(gm.Grafo):
    pass

# Extensão da classe de Grafo Direcionado em Lista de Adjacencia
class TGrafoListaD(gm.Grafo):
    pass

# Extensão da classe de Grafo Nao Direcionado em Lista de Adjacencia
class TGrafoListaND(gm.Grafo):
    pass


def main():
    print("Starting main.py")
    
    # Instanciando as classes de extensão para testes iniciais
    print("\nTeste: TGrafoMatrizDirecionado")
    gm_dir = TGrafoMatrizD(5)
    gm_dir.insereA(1,3)
    gm_dir.insereA(1,4)
    gm_dir.insereA(3,4)
    gm_dir.insereA(2,1)

    gm_dir.show()

    print("\nGrau de entrada do vértice 4:", gm_dir.inDegree(4))
    print("\nGrau de saída do vértice 1:", gm_dir.outDegree(1))
    print("\nGrau do vértice:", gm_dir.degree(1))
    
    print("\nTeste: TGrafoMatrizNaoDirecionado")
    gm_nd = TGrafoMatrizND(5)
    print(gm_nd)
    
    print("\nTeste: TGrafoListaDirecionado")
    gl_dir = TGrafoListaD(5)
    print(gl_dir)
    
    print("\nTeste: TGrafoListaNaoDirecionado")
    gl_nd = TGrafoListaND(5)
    print(gl_nd)

if __name__ == '__main__':
    main()
