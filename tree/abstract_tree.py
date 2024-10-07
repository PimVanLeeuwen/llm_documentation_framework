from enum import Enum

class ASTNodeType(Enum):
    """Enum to list the different types of nodes"""
    FOLDER = 1
    FILE = 2
    METHOD = 3
    IMPORT = 4

class ASTNode:
    """The nodes of the AST"""
    def __init__(self, name, node_type: ASTNodeType, children=None, parent_node=None, content=None):
        # Name of the node
        self.name = name
        # Parent of the node
        self.parent_node = parent_node
        # Type of the node
        self.node_type = node_type
        # Content of the node
        self.content = content
        # All the children of this node
        self.children = children if children is not None else []

    # Add a child to this node
    def add_child(self, child_node):
        self.children.append(child_node)

    # Get the path of a node
    def get_path(self):
        path = []
        node = self.parent_node
        while node:
            path.append(node.name)
            node = node.parent_node
        return '/'.join(reversed(path))

    # print this node and its children
    def __repr__(self, level=0, recursive=False):
        # This is for when we print the entire tree
        if recursive:
            type_prefix = {
                ASTNodeType.FOLDER: "[Folder]",
                ASTNodeType.FILE: "[File]",
                ASTNodeType.IMPORT: "[Import]",
                ASTNodeType.METHOD: "[Method]"
            }
            indent = '    ' * (level)
            output = f"{indent}└── {type_prefix.get(self.node_type)} {self.name}\n"
            for child in self.children:
                output += child.__repr__(level + 1, recursive)
            return output
        # This is for just printing a node
        else:
            output = f"[Name] {self.name}\n"
            output += f"[Type] {self.node_type}\n"
            output += f"[Content] {self.content}\n"
            output += f"[Parent] {self.parent_node.name}\n" if self.parent_node else f"[Parent] None\n"
            output += f"[Children]"
            for c in self.children:
                output += f"{c.name}"
            output += "\n"
            return output

    # Loop over the tree
    def __iter__(self):
        yield self
        for child in self.children:
            yield from child


class AbstractSyntaxTree:
    """The abstract syntax tree that will be used for repository structures"""
    def __init__(self, root=None):
        self.root = root
        self.str_rep = None

    def __repr__(self):
        # Printing a tree is just printing the root and all children
        # We also store this to not have to regenerate it every time (since it does not change)
        if self.str_rep:
            return self.str_rep
        else:
            self.str_rep = self.root.__repr__(recursive=True)
            return self.str_rep

    # Loop over the tree
    def __iter__(self):
        if self.root:
            yield from self.root