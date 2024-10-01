from enum import Enum

class ASTNodeType(Enum):
    """Enum to list the different types of nodes"""
    FOLDER = 1
    FILE = 2
    METHOD = 3
    IMPORT = 4

class ASTNode:
    """The nodes of the AST"""
    def __init__(self, name, node_type: ASTNodeType, children=None):
        # Name of the node
        self.name = name
        # Type of the node
        self.node_type = node_type
        # All of the children of this node
        self.children = children if children is not None else []

    # Add a child to this node
    def add_child(self, child_node):
        self.children.append(child_node)

    # print this node and its children
    def __repr__(self, level=0):
        type_prefix = {
            ASTNodeType.FOLDER: "[Folder]",
            ASTNodeType.FILE: "[File]",
            ASTNodeType.IMPORT: "[Import]",
            ASTNodeType.METHOD: "[Method]"
        }
        indent = '    ' * (level)
        output = f"{indent}└── {type_prefix.get(self.node_type)} {self.name}\n"
        for child in self.children:
            output += child.__repr__(level + 1)
        return output


class AbstractSyntaxTree:
    """The abstract syntax tree that will be used for repository structures"""
    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        # Printing a tree is just printing the root and all children
        return self.root.__repr__()