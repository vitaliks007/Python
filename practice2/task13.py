import os
from sys import argv
from graphviz import Digraph


def dir_bypass(path):
    for fname in os.listdir(path):
        dot.node(path + '/' + fname, fname)
        dot.edge(path, path + '/' + fname)
        if os.path.isdir(path + '/' + fname) and os.listdir(path + '/' + fname):
            dir_bypass(path + '/' + fname)
    return


name = argv[1]
dot = Digraph(comment='Dirs')
dot.node(name, os.path.basename(name))

dir_bypass(name)

dot.render('output/dirs.gv', view=True)
