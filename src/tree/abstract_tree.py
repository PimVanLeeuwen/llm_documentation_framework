from src.tree.tree_nodes import ASTNodeType


class AbstractSyntaxTree:
    """The abstract syntax tree that will be used for repository structures"""
    def __init__(self, root=None):
        self.root = root
        self.str_rep = None
        self.nr_nodes = None

    # Get the root of the tree
    def get_root(self):
        return self.root

    # get the number of nodes in the tree and cache this
    def get_nr_nodes(self):
        if self.nr_nodes:
            return self.nr_nodes
        else:
            self.nr_nodes = 0
            for _n in self:
                self.nr_nodes += 1
            return self.nr_nodes

    # return if the tree is 'filled' with docs
    def has_documentation(self):
        for n in self:
            if not n.has_documentation() and (n.get_type == ASTNodeType.METHOD or n.get_type == ASTNodeType.OBJECT):
                return False

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