path = []

#------------------------------------------
'''
Verifica se o vertice nao esta no caminho ja
'''
def temCiclo(node):
    if(node in path):
        return False
    
    return True     

#-------------------------------------------

def DetectaCiclo(E,n,root):
    path.append(root)
    #Vendo todos os vizinhos da raiz

    for i in E[root]:
        #Checa se o vertex nao esta no path ja
        if(temCiclo(i)):
            #Senao, pula para o filho e faz a mesma coisa com ele
            if(DetectaCiclo(E,n,i)):
                return True
    
    #Tem todos os vertices ?
    if(len(path) == n):
        # Se tem todos os vertices, o primeiro e o ultimo sao os mesmo ?
        # Se sim, eh um ciclo
        if(path[0] in E[path[len(path)-1]]):
            return True 
        else:
            return False
    
    path.pop()

#-------------------------------------------    

'''
Retorna True or False, tendo em vista uma detectacao de ciclo
'''

def cicloHamiltoniano(E,n,root):
    if(DetectaCiclo(E,n,root)):
        return True, path
    else:
        return False, path
