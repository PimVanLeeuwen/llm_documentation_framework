import os
from tree.abstract_tree import *
from tree.tree_nodes import *
from grammars.java.java_parser import parse_java_file
from tqdm import tqdm

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
	# TODO: add total files to this counter such that it is more representable
	for root, dirs, files in tqdm(os.walk(directory), desc="Creating Tree", unit="files"):
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

	# we need to make a dict with names -> nodes with one pass
	# then another pass to replace the names with nodes

	# This will contain all the methods calls from objects
	class_method_calls = {}

	for node in tqdm(tree, total=tree.get_nr_nodes() ,desc="Creating Tree", unit="files"):
		if node.get_type() == ASTNodeType.METHOD and node.get_parent().get_type() == ASTNodeType.CLASS:
			class_method_calls[f"{node.get_parent().get_name()}.{node.get_name()}"] = node

	for node in tqdm(tree, total=tree.get_nr_nodes() ,desc="Creating Tree", unit="files"):
		if len(node.get_calls()) > 0:
			for call in node.get_calls():
				listing = [key for key in class_method_calls.keys() if call.split('(')[0] == key.split(".")[1]]
				if len(listing) > 0:
					print(listing)

	return tree
