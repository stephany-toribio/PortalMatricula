import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def cargarData():
    data = pd.read_excel("PlanInformatica.xlsx")
    return data

def grafo_curso(curso):
    data = cargarData()
    G = nx.DiGraph()

    codigo = data.loc[data["Nombre"] == curso,"Código"].values[0]
    G.add_node(codigo)

    flag = False
    while flag == False:
        if (data["Requisito"] == codigo).any():
            descendiente_nombre = data.loc[data["Requisito"] == codigo, "Nombre"].values[0]
            descendiente_codigo = data.loc[data["Requisito"] == codigo, "Código"].values[0]
            G.add_node(descendiente_codigo)
            G.add_edge(codigo, descendiente_codigo)
            codigo = descendiente_codigo
        else:
            nx.draw_networkx(G)
            flag = True

print(grafo_curso("Procesos de innovación en ingeniería"))

"""
def main():
    return "yes"

if __name__ == "__main__":
    main()
"""