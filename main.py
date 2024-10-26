"""
Main file in the LLM Documentation Framework
Autor -- Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""

import os
from folder_operations.folders_and_files import create_tree_from_files
from llm.document_tree import document_tree
from tree.tree_nodes import ASTNodeType, ASTNode
from llm.document_node import document_node

repo_path = '/home/pimvanleeuwen/Documents/employer-worker-registration-system'

if __name__ == '__main__':
	# generate the AST
	tree = create_tree_from_files(repo_path, ".java")

	# Write the Tree
	with open("AbstractSyntaxTree.txt", "w") as f:
		f.write(str(tree))

	document_tree(tree)










