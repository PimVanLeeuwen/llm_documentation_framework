"""
File that handles convertion from AbstractSyntaxTree to mkdocs format

Author:
	Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""

from src.tree.abstract_tree import AbstractSyntaxTree
from src.tree.tree_nodes import ASTNodeType, ASTNode


def tree_to_mkdocs(tree: AbstractSyntaxTree):
     """This will go through the tree and create the mkdocs.yml file.

    Args:
        tree (AbstractSyntaxTree): tree to process.
    """

     # It needs an index file so we will write one with the project title
     f = open("docs/index.md", "w")
     f.write(f"# {tree.get_root().get_name()}")
     f.close()

     # Set up the basics of the file
     f = open("mkdocs.yml", "w")
     f.write(f"site_name: {tree.get_root().get_name()}\n")
     f.write(f"theme: readthedocs\n\nnav:\n  - Index: index.md\n  - Files:\n")

     # Add every file node to a list, since mkdocs have limited depth, but infinite length, this is the most reliable
     for node in tree:
          if node.get_type() == ASTNodeType.FILE and node.get_children():
               f.write(f"    - {node.get_name()}:\n")
               for entry in get_children(node):
                    f.write(entry)

     f.close()

def get_children(node: ASTNode):
     """This method adds all the yml entries for the mkdocs config.

    Args:
        node (ASTNode): node to add entries for.

    Returns:
        str: output for the mkdocs config.
    """
     to_process = node.get_children()
     output = set()

     # Keep processing nodes to also cover methods of objects and nested objects
     while to_process:
          p_node = to_process.pop()
          # We only want methods and objects
          if p_node.get_type() == ASTNodeType.METHOD or p_node.get_type() == ASTNodeType.OBJECT:
               # Get potential children also recursively
               for c_node in p_node.get_children():
                    to_process.append(c_node)
               # Add the mkdocs listing
               output.add(f"      - {'M' if p_node.get_type() == ASTNodeType.METHOD else 'O'} | "
                          f"{p_node.get_name()}: {p_node.get_path()}/{p_node.get_name()}.md\n")

     return output


