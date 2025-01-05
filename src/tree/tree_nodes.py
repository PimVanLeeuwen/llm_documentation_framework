"""
File that contains ASTNodeType Enum and ASTNode Class

Author:
	Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""

from enum import Enum

class ASTNodeType(Enum):
    """Enum to list the different types of nodes
	"""
    FOLDER = 1
    FILE = 2
    METHOD = 3
    OBJECT = 4

class ASTNode:
    """The nodes of the abstract syntax tree
	"""
    def __init__(self, name, node_type: ASTNodeType, children=None, imports=None, calls=None,
                 parameters=None, parent_node=None, content=None):
        """initialize the node

        Args:
            name (str): Name of the node.
            parent_node (ASTNode): Parent of the node.
            node_type (str): Type of the node.
            children (ASTNode[] or None): Children of the node.
            imports (string[] or None): Imports of the node, this is used only in a File node.
            calls (string[] or ASTNode[] or None): Calls to other methods, this might initially be in string
                format but should eventually be in ASTNode format.
            parameters (string[] or None)
            content (str): Content of the node.

        Vars:
            documentation (str): Documentation of the node.
            short_documentation (str): Short documentation of the node.
        """

        self.name = name
        self.parent_node = parent_node
        self.node_type = node_type
        self.content = content
        self.children = children if children else []
        self.imports = imports if imports else []
        self.calls = calls if calls else []
        self.parameters = parameters if parameters else []
        self.documentation = None
        self.short_documentation = None


    def get_name(self):
        """Get the name of the node

        Returns:
		    string: Name of the node.
		"""
        return self.name

    def get_parent(self):
        """Get the parent of the node

        Returns:
		    ASTNode: Parent of the node.
		"""
        return self.parent_node

    def get_type(self):
        """Get the type of the node

        Returns:
		    ASTNodeType: Type of the node.
		"""
        return self.node_type

    def get_content(self):
        """Get the content of the node

        Returns:
		    string: Content of the node.
        """
        return self.content

    def get_children(self):
        """Get the children of the node

        Returns:
		    ASTNode[]: Children documentation of the node.
        """
        return self.children

    def add_child(self, child_node):
        """Add a child to the node

        Args:
		    child_node (ASTNode): The node to add.
		"""
        self.children.append(child_node)

    def get_imports(self):
        """Get the imports of the node

        Returns:
		    string[]: Imports documentation of the node.
        """
        return self.imports

    def add_import(self, import_statement):
        """Add an import to the node

        Args:
		    import_statement (string): The import to add.
		"""
        self.imports.append(import_statement)

    def get_calls(self):
        """Get the calls of the node

        Returns:
		    string[] or ASTNode[]: Calls of the node.
        """
        return self.calls

    def add_call(self, call_statement):
        """Add a call to the node

        Args:
		    call_statement (string): The call to add.
		"""
        self.calls.append(call_statement)

    def set_calls(self, calls):
        """Set the calls of the node

        Args:
		    calls (ASTNode[] or string[]): The calls to set.
		"""
        self.calls = calls

    def get_parameters(self):
        """Get the parameters of the node

        Returns:
		    string[]: Parameters of the node.
        """
        return self.parameters

    def add_parameter(self, param):
        """Add a parameter to the node

        Args:
		    param (string): The param to add.
		"""
        self.parameters.append(param)

    def get_documentation(self):
        """Get the documentation of the node

        Returns:
		    string: Documentation of the node.
        """
        return self.documentation

    def set_documentation(self, documentation):
        """Set the documentation of the node

        Args:
		    documentation (string): The documentation to set.
		"""
        self.documentation = documentation

    def has_documentation(self):
        """Check if there is documentation

        Returns:
		    bool: True if there is documentation.
        """
        return self.documentation is not None

    def get_short_documentation(self):
        """Get the short documentation of the node

        Returns:
		    string: Short documentation of the node.
        """
        return self.short_documentation

    def set_short_documentation(self, short_documentation):
        """Set the short documentation of the node

        Args:
		    short_documentation (string): The short_documentation to set.
		"""
        self.short_documentation = short_documentation

    def can_document(self):
        """Check if all calls and children are documented

        Returns:
		    bool: True if there is documentation for all children and all called methods.
        """
        return (all(call.has_documentation() for call in self.calls) and
                all(child.has_documentation() for child in self.children))

    def get_path(self):
        """Get the path of a node

        Returns:
		    string: Path of this node.
        """
        path = []
        node = self.parent_node
        while node:
            path.append(node.name)
            node = node.parent_node
        return '/'.join(reversed(path))

    def __repr__(self, level=0, recursive=False, extended=True):
        """print this node and its children

        Args:
		    level (int): Depth of printing, initially 0.
		    recursive (bool): If also children are printed.
		    extended (bool): Print extensive debugging information.

        Returns:
		    string: representation of this tree.
        """

        # This is for when we print the entire tree
        if recursive:
            type_prefix = {
                ASTNodeType.FOLDER: "[Folder]",
                ASTNodeType.FILE: "[File]",
                ASTNodeType.OBJECT: "[Object]",
                ASTNodeType.METHOD: "[Method]"
            }
            indent = '    ' * level
            output = f"{indent}└── {type_prefix.get(self.node_type)} {self.name}\n"
            if extended:
                for i in self.imports:
                    output += f"{indent}    [import] {i}\n"
                for i in self.parameters:
                    output += f"{indent}    [param] {i}\n"
                for i in self.calls:
                    output += f"{indent}    [call] {i.get_name() if isinstance(i, ASTNode) else i}\n"
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
                output += f"{c.name}, "
            output += "\n"
            return output

    def __iter__(self):
        """Iterator for nodes in the subtree rooted at this node.

        Returns:
		    iterator or ASTNode: Iterator for nodes in the tree or node if just one.
        """
        yield self
        for child in self.children:
            yield from child