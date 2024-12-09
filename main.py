"""
Main file in the LLM Documentation Framework
Autor -- Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""

import argparse
import os
import sys
import logging
import mkdocs.commands.build
import mkdocs.commands.serve
import mkdocs.config
from src.documentation_combiner.tree_to_mkdocs import tree_to_mkdocs
from src.folder_operations.folders_and_files import create_tree_from_files
from src.llm.document_tree import document_tree

if __name__ == '__main__':

	# Initialize parser
	parser = argparse.ArgumentParser()

	# Adding optional argument
	parser.add_argument("-d", "--Gen-Doc", help="Generate Documentation, requires path of the repo")
	parser.add_argument("-w", "--Run-Website", action="store_true", help="Run the website, requires documentation to have been generated (before)")


	# Read arguments from command line
	args = parser.parse_args()

	if not (args.Gen_Doc or args.Run_Website):
		parser.print_help(sys.stderr)

	if args.Gen_Doc:
		# generate the AST
		tree = create_tree_from_files(args.Gen_Doc, tuple([".java", ".cpp"]))

		# Write the Tree
		with open("AbstractSyntaxTree.txt", "w") as f:
			f.write(tree.root.__repr__(recursive=True, extended=True))

		# Put the documentation in the tree
		document_tree(tree)

		# Put the documentation in the right format
		tree_to_mkdocs(tree)

	if args.Run_Website:
		# If there is no documentation, raise exception
		if not (os.path.isdir("docs") and os.path.isfile("mkdocs.yml")):
			raise Exception("Missing documentation, use -d flag to also generate documentation")

		# Run the local server for the documentation
		logging.basicConfig(level=logging.INFO, format='mkdocs: %(message)s')
		mkdocs.commands.serve.serve(open_in_browser=True)