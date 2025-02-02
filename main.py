"""
Main file in the LLM Documentation Framework

Author:
	Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
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
from src.eval.evaluate import evaluate_documentation

API_KEY = os.environ.get('CAPGEMINI_API_KEY')
MODEL_PROVIDER = os.environ.get('MODEL_PROVIDER')
MODEL_NAME = os.environ.get('MODEL_NAME')
REPOSITORY_PATH = os.environ.get('REPOSITORY_PATH')
PROVIDE_CONTEXT = os.environ.get('PROVIDE_CONTEXT')
USE_LOCAL_LLM = os.environ.get('USE_LOCAL_LLM')

if __name__ == '__main__':
	# Initialize parser
	parser = argparse.ArgumentParser()

	# Adding optional argument
	parser.add_argument("-d", "--Gen-Doc", action="store_true", help="Generate Documentation")
	parser.add_argument("-w", "--Run-Website", action="store_true", help="Run the website, requires documentation to have been generated (before)")
	parser.add_argument("-e", "--Evaluate", action="store_true", help="Give the evaluation of a generated documentation, for this reference documentation must be placed in the reference folder. The same layout is used as the generated documentation.")

	# Read arguments from command line
	args = parser.parse_args()

	if not (args.Gen_Doc or args.Run_Website or args.Evaluate):
		parser.print_help(sys.stderr)

	if not (API_KEY and MODEL_PROVIDER and MODEL_NAME and REPOSITORY_PATH and PROVIDE_CONTEXT and USE_LOCAL_LLM):
		raise Exception("Not all env variables are defined, please define them according to .env.example")

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

	if args.Evaluate:
		# Evaluate using ROUGE and BLUE
		print("Eval")
		evaluate_documentation()
