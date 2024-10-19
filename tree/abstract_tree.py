class AbstractSyntaxTree:
    """The abstract syntax tree that will be used for repository structures"""
    def __init__(self, root=None):
        self.root = root
        self.str_rep = None
        self.nr_nodes = None

    def get_nr_nodes(self):
        if self.nr_nodes:
            return self.nr_nodes
        else:
            self.nr_nodes = 0
            for n in self:
                self.nr_nodes += 1
            return self.nr_nodes

    def __repr__(self):
        # Printing a tree is just printing the root and all children
        # We also store this to not have to regenerate it every time (since it does not change)
        if self.str_rep:
            return self.str_rep
        else:
            self.str_rep = self.root.__repr__(recursive=True, extended=True)
            return self.str_rep

    # Loop over the tree
    def __iter__(self):
        if self.root:
            yield from self.root