import os
import json
from ASTExtractor.astextractor import ASTExtractor
from tree.abstract_tree import ASTNode, ASTNodeType, AbstractSyntaxTree
from folder_operations.parse_json import find_declarations

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
	# For java we use this ASTExtractor
	ast_extractor = ASTExtractor("ASTExtractor/ASTExtractor-0.5.jar", "ASTExtractor/ASTExtractor.properties")
	# Then we get all methods and imports
	all_methods = list(find_declarations(json.loads(ast_extractor.parse_file(path, representation="JSON")), "MethodDeclaration"))
	all_imports = list(find_declarations(json.loads(ast_extractor.parse_file(path, representation="JSON")), "ImportDeclaration"))

	# Create the node for the project file
	file_node = ASTNode(file, ASTNodeType.FILE)

	# Attach the children for the imports
	for imp, imp_content in all_imports:
		import_node = ASTNode(imp, ASTNodeType.IMPORT, content=imp_content, parent_node=file_node)
		file_node.add_child(import_node)

	# Attach the children for the methods
	for method, method_content in all_methods:
		method_node = ASTNode(method, ASTNodeType.METHOD, content=method_content, parent_node=file_node)
		file_node.add_child(method_node)

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
