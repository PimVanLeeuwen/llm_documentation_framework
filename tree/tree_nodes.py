from enum import Enum

class ASTNodeType(Enum):
    """Enum to list the different types of nodes"""
    FOLDER = 1
    FILE = 2
    METHOD = 3
    CLASS = 4

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
        # Import, this is used only in a File node
        self.imports = []
        # Calls to other methods
        self.calls = []
        # parameter in case of method node
        self.parameters = []

    # Add an import statement
    def add_import(self, import_statement):
        self.imports.append(import_statement)

    # Add an import statement
    def add_call(self, call_statement):
        self.calls.append(call_statement)

    # Add a child to this node
    def add_child(self, child_node):
        self.children.append(child_node)

    # Return the type of the node
    def get_type(self):
        return self.node_type

    # Return the parent of the node
    def get_parent(self):
        return self.parent_node

    # Add parameters to the list
    def add_param(self, param):
        self.parameters.append(param)

    # Get the parameters list
    def get_param(self):
        return self.parameters

    # Get the path of a node
    def get_path(self):
        path = []
        node = self.parent_node
        while node:
            path.append(node.name)
            node = node.parent_node
        return '/'.join(reversed(path))

    # print this node and its children
    def __repr__(self, level=0, recursive=False, extended=True):
        # This is for when we print the entire tree
        if recursive:
            type_prefix = {
                ASTNodeType.FOLDER: "[Folder]",
                ASTNodeType.FILE: "[File]",
                ASTNodeType.CLASS: "[Class]",
                ASTNodeType.METHOD: "[Method]"
            }
            indent = '    ' * (level)
            output = f"{indent}└── {type_prefix.get(self.node_type)} {self.name}\n"
            if extended:
                for i in self.imports:
                    output += f"{indent}    import {i}\n"
                for i in self.parameters:
                    output += f"{indent}    param {i}\n"
                for i in self.calls:
                    output += f"{indent}    [call] {i}\n"
            for child in self.children:
                output += child.__repr__(level + 1, recursive, extended)
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