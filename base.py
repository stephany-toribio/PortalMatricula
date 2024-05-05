import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def cargarData():
    data = pd.read_excel("PlanInformatica.xlsx")
    return data

def grafo_curso(curso):
    data = cargarData()
    G = nx.DiGraph()

    stack = [curso]
    while stack:
        curso_actual = stack.pop()
        codigo = data.loc[data["Nombre"] == curso_actual,"Código"].values[0]
        G.add_node(codigo)

        requisitos = data.loc[data["Requisito"] == codigo, "Nombre"].values[:]
        for descendiente_nombre in requisitos:
            descendiente_codigo = data.loc[data["Nombre"] == descendiente_nombre, "Código"].values[0]
            G.add_node(descendiente_codigo)
            G.add_edge(codigo, descendiente_codigo)
            stack.append(descendiente_nombre)

    return nx.draw_networkx(G)

def grafo_planEstudio():
    data = cargarData()
    G = nx.DiGraph()

    ciclos = sorted((data["Ciclo"].unique()))
    cursos =data["Nombre"].unique()
    for curso in cursos:
        stack = [curso]
        while stack:
            curso_actual = stack.pop()
            codigo = data.loc[data["Nombre"] == curso_actual,"Código"].values[0]
            G.add_node(codigo)
            
            requisitos = data.loc[data["Requisito"] == codigo, "Nombre"].values[:]
            #requisitos = [valor for valor in data.loc[data["Requisito"] == codigo, "Nombre"].values[:] if valor not in ["40 créditos", "80 créditos", "120 créditos", "150 créditos","C0090 /150 créditos"]]
            for descendiente_nombre in requisitos:
                descendiente_codigo = data.loc[data["Nombre"] == descendiente_nombre, "Código"].values[0]
                G.add_node(descendiente_codigo)
                G.add_edge(codigo, descendiente_codigo)
                stack.append(descendiente_nombre)

    pos = {}

    for i, ciclo in enumerate(ciclos):
        cursos_ciclo = data[data["Ciclo"] == ciclo]["Código"].tolist()
        for j, curso in enumerate(cursos_ciclo):
            pos[curso] = (j, -i)

    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, arrowsize=20)
    plt.title("Plan de Estudios")
    plt.show()           

def main():
    #grafo_curso("Estadística y probabilidades")
    grafo_planEstudio()

if __name__ == "__main__":
    main()
