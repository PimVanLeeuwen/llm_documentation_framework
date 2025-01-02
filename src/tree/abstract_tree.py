from src.tree.tree_nodes import ASTNodeType


class AbstractSyntaxTree:
    """The abstract syntax tree that will be used for repository structures"""
    def __init__(self, root=None):
        """initialize the node

        Args:
            root (ASTNode): Root of the tree.

        Vars:
            documentation (str): Documentation of the node.
            short_documentation (str): Short documentation of the node.
        """
        self.root = root

    def get_root(self):
        """Get the root of this tree.

        Returns:
		    ASTNode: Root of the tree.
        """
        return self.root

    def get_nr_nodes(self):
        """Get the number of nodes in the tree.

        Returns:
		    int: Number of nodes in the tree.
        """
        return sum(1 for _ in self)

    def has_documentation(self):
        """Check if there is documentation in all tree nodes.

        Returns:
		    bool: True if there is documentation in all nodes.
        """
        return all(n.has_documentation() or (n.get_type in {ASTNodeType.METHOD, ASTNodeType.OBJECT}) for n in self)

    def __repr__(self):
        """Printing a tree is just printing the root and all children

        Returns:
		    string: representation of this tree.
        """
        return self.root.__repr__(recursive=True, extended=True)

    def __iter__(self):
        """Iterator for nodes in the tree

        Returns:
		    iterator or ASTNode: Iterator for nodes in the tree or node if just one .
        """
        yield from self.root if self.root else None