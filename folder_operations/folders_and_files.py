import os
import warnings

from tree.abstract_tree import *
from tree.tree_nodes import *
from grammars.java.java_parser import parse_java_file
from tqdm import tqdm

def calls_mapped(tree):
	"""check if all calls are mapped to nodes, if so return true, else return false"""
	for n in tqdm(tree, total=tree.get_nr_nodes() ,desc="Check if all calls are mapped", unit="nodes"):
		if n.get_calls():
			for call in n.get_calls():
				if not isinstance(call, ASTNode):
					return False

	return True

def get_classes_from_file(node):
	"""Return the classes in a file"""
	return_array = []
	for n in node:
		if n.get_type() == ASTNodeType.CLASS:
			return_array.append(n)

	return return_array

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
	nr_files = 0

	# Small check for the status bar, adds negligible time
	for root, dirs, files in os.walk(directory):
		for file in files:
			if file.endswith('.java'):
				nr_files += 1

	# Do an OSWalk through the project directory
	for root, dirs, files in tqdm(os.walk(directory), total=nr_files, desc="Creating Tree", unit="files"):
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


	for node in tqdm(tree, total=tree.get_nr_nodes() ,desc="Indexing Sources", unit="nodes"):
		# only interested in the methods
		if not node.get_type() == ASTNodeType.METHOD:
			continue

		# find an identifying parent, pref a class but file will suffice (usually not needed)
		p_node = node.get_parent()
		while not (p_node.get_type() == ASTNodeType.CLASS or p_node.get_type() == ASTNodeType.FILE):
			p_node = p_node.get_parent()

		# add it to the dictionary
		class_method_calls[f"{p_node.get_name()}.{node.get_name()}"] = node


	for node in tqdm(tree, total=tree.get_nr_nodes() ,desc="Converting Calls", unit="nodes"):

		# get the calls and we will construct the converted calls
		calls = node.get_calls()
		new_calls = set()

		# folders are not relevant here
		if node.get_type() == ASTNodeType.FOLDER:
			continue

		# check for all calls if we can convert them, if not, drop them
		for call in calls:
			# these are all the hits for a node call
			node_calls = [key for key in class_method_calls.keys() if call.split('(')[0] == key.split(".")[-1]]

			match len(node_calls):
				case 0:
					# if there are no matching calls, just remove this, then there is no content that we can add
					continue
				case 1:
					# if there is only one, no checks are needed and we can just add that one, since there is no doubt.
					new_calls.add(class_method_calls[node_calls[0]])
					continue
				case _:
					# in this case we need to check if we can find the method that is most relevant
					# we are interested in the nearest file node
					current_node = node

					# recurse up until we find it
					while not current_node.get_type() == ASTNodeType.FILE:
						current_node = current_node.get_parent()

					# get the internal sources, file name and classes within the file
					local_sources = get_classes_from_file(current_node)
					if not current_node.get_name().split(".")[0] in local_sources:
						local_sources.append(current_node.get_name().split(".")[0])

					# get the imports, so external sources
					external_sources = [source.split(".")[-1] for source in current_node.get_imports()]

					# preferably we have an internal source, but otherwise an external
					for source in local_sources, external_sources:
						hits = []
						for local in source:
							# check if we can math any of the sources with the calls
							hits = [key for key in node_calls if key.split(".")[0] == local]
						if hits:
							# this should not occur, because then we are not certain that we have the right one
							if len(hits) > 1:
								warnings.warn("There are more than 1 hits in this: " + str(hits))
							# get this new hit
							new_calls.add(class_method_calls[hits[0]])
							# we break because in this case we do not need to cover the external sources (if happens in internal)
							break

		# set updated array
		node.set_calls([call for call in new_calls])

	# We should warn the user when we are returning still unmapped errors.
	if not calls_mapped(tree):
		warnings.warn("There are unmapped calls and this tree is being returned, this should not happen")


	return tree
