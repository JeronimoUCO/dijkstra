
from node import node

n5=node({},True)
n4=node({n5:4},False)
n3=node({n5:2},False)
n2=node({n3:4},False)
n1=node({n3:1},False)
n0=node({n5:2,n4:5},False)

def dijkstra(start,end):
    shortest=0
    actual=start
    for i in range(0,9):
      while not actual.isFinal:
          least=list(actual.next.keys())[0]

          for i in actual.next:
              if actual.next[i]<actual.next[least]:
                  least=i
        
          shortest+=actual.next[least] 
          actual=least
    print(f"El camino más corto cuesta {shortest} unidades")

dijkstra(n0,n5)