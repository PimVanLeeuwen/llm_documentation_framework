import os
import json
from ASTExtractor.astextractor import ASTExtractor
from tree.abstract_tree import *
from tree.tree_nodes import *
from folder_operations.parse_json import find_declarations
from grammars.java.java_parser import parse_java_file

def contains_files(dir_path, extension=".java"):
	"""Check if a directory or any of its subdirectories contain .x files."""
	for root, dirs, files in os.walk(dir_path):
		if any(file.endswith(extension) for file in files):
			return True
	return False

def parse_file(path, file):
	"""process one project file, creates a node of that file and attaches any info we want in the AST
	@:return The file node with the added information
	"""

	# print(file)
	file_node = parse_java_file(path, file)
	# print()

	# Return the node
	return file_node

def create_tree_from_files(directory, extension=".java"):
	"""Creates a tree like structure adding the files with a certain extension"""
	tree = AbstractSyntaxTree(ASTNode(os.path.basename(directory), ASTNodeType.FOLDER))
	# Do an OSWalk through the project directory
	for root, dirs, files in os.walk(directory):
		# If the folder contains any files with a certain extension it is worth looking into
		if contains_files(root, extension):
			# Current depth of the folder
			level = root.replace(directory, '').count(os.sep)
			# We compute the parent node, since we are doing a pre-order traversal we know where to find the parent
			parent_node = tree.root
			for _ in range(level):
				if parent_node.children:
					parent_node = parent_node.children[-1]

			# Create the node for this folder and add to parent
			dir_node = ASTNode(os.path.basename(root), ASTNodeType.FOLDER, parent_node=parent_node)
			parent_node.add_child(dir_node)

			# Process any non-folder items in this folder
			for file in files:
				if file.endswith(".java"):
					file_node = parse_file(os.path.join(root, file), file)
					file_node.parent_node = parent_node
					dir_node.add_child(file_node)
	return tree
