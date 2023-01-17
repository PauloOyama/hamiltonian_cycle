import random    
from pyvis.network import Network
from hamiltonian_cycle import cicloHamiltoniano

net = Network(notebook=True,cdn_resources="remote" )

bairros = ["Centro",
    "Fundinho",
    "Nossa Senhora Aparecida"
    "Martins",
    "Osvaldo Rezende",
    "Bom Jesus",
    "Brasil",
    "Cazeca",
    "Lídice",
    "Daniel Fonseca",
    "Tabajaras",
    "Presidente Roosevelt",
    "Jardim Brasília",
    "São José",
    "Marta Helena",
    "Pacaembu",
    "Santa Rosa",
    "Residencial Gramado",
    "Nossa Senhora das Graças",
    "Minas Gerais",
    "Distrito Industrial",
    "Maravilha",
    "Jaraguá",
    "Planalto",
    "Chácaras Tubalina",
    "Chácaras Panorama",
    "Luizote de Freitas",
    "Jardim das Palmeiras",
    "Jardim Patrícia",
    "Jardim Holanda",
    "Jardim Europa",
    "Jardim Canaã",
    "Mansour",
    "Dona Zulmira",
    "Taiaman",
    "Guarani",
    "Tocantins ",
    "Morada do Sol",
    "Monte Hebron",
    "Residencial Pequis",
    "Morada Nova ",
    "Tubalina",
    "Cidade Jardim",
    "Nova Uberlândia",
    "Patrimônio",
    "Morada da Colina",
    "Vigilato Pereira",
    "Saraiva",
    "Lagoinha",
    "Carajás",
    "Pampulha",
    "Jardim Karaíba",
    "Jardim Inconfidência",
    "Santa Luzia",
    "Granada",
    "São Jorge",
    "Laranjeiras",
    "Shopping Park",
    "Jardim Sul",
    "Gávea",
    "Santa Mônica",
    "Tibery",
    "Segismundo Pereira",
    "Umuarama",
    "Alto Umuarama",
    "Custódio Pereira",
    "Aclimação",
    "Mansões Aeroporto",
    "Alvorada",
    "Novo Mundo",
    "Morumbi",
    "Residencial Integração",
    "Morada dos Pássaros",
    "Jardim Ipanema",
    "Portal do Vale",
    "Granja Marileusa",
    "Grand Ville",
    ]

path = []

N_Vertices = random.randint(10, 25)

E_number = random.randint(25,75)

print(N_Vertices, E_number)

matrix = list()

#------------------------------------------

# Criando matrix 
for i in range(N_Vertices):
    matrix.append([])
    
edges= []
#Criando vertices aleatoriamente
for i in range(E_number):
    u = random.randint(1,N_Vertices)
    v = random.randint(1,N_Vertices)
    if u == v:
        while u==v:
            v = random.randint(1,N_Vertices)
    edges.append([u-1,v-1])
    matrix[u-1].append(v-1)
    matrix[v-1].append(u-1)

#------------------------------------------

#Plot de Nós
nodes = [x for x in range(N_Vertices)]
for x in range(N_Vertices): 
    net.add_node(x,label=bairros[x], size=10)

#Plot de Vértices
for i in range(len(edges)):
    net.add_edge(edges[i][0],edges[i][1])

net.show_buttons(filter_=['physics'])
net.show(name='graph.html')

#------------------------------------------

hasHamilton, path = cicloHamiltoniano(matrix,N_Vertices,0)

print(hasHamilton)
if hasHamilton:
    for x in range(N_Vertices):
        print(bairros[path[x]] + " - ", end= "") 
