from CFG_Test import *

G = create_graph()
dico_test_1 = {'x':5}
dico_test_2 = {'x':4}
dico_test_3 = {'x':-3}
dico_test_4 = {'x':-1}
tests = [dico_test_1, dico_test_2, dico_test_3, dico_test_4]

def test_all_affect(g):
    assign_nodes = [i for i, j in g.edges if g.adj[i][j]['cmd_type']=='assign']
    # for u, v in g.edges:
    #     if (g.adj[u][v]['cmd_type']=='Assign') and (u not in assign_nodes):
    #         assign_nodes += [u]
    for t in tests :
        path = browse_graph(t, g)
        for e in assign_nodes:
            if e in path:
                assign_nodes = [i for i in assign_nodes if i != e]
    return(assign_nodes==[])


def browse_graph(dico, g):
    tmp_node = 1
    path = [1]
    while tmp_node != max(g.nodes):
        successors = list(g.successors(tmp_node))
        i = 0
        not_found = True
        while not_found:
            v = successors[i]
            if g.adj[tmp_node][v]['cond'](dico):
                g.adj[tmp_node][v]['cmd'](dico)
                tmp_node = v
                path += [v]
                not_found = False
            i+=1
    return(path)

print(test_all_affect(G))