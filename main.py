"""
Main file in the LLM Documentation Framework
Autor -- Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""
repo_path = '/home/pimvanleeuwen/Documents/zerocode'

from ASTExtractor.astextractor import ASTExtractor
import json

def print_ast(node, indent=0):
	"""Recursively print the AST with indentation."""
	if isinstance(node, dict):
		for key, value in node.items():
			# print(type(key))
			# print(type(value))
			# print(' ' * indent + str(key) + ':')
			print_ast(value, indent + 2)
	elif isinstance(node, list):
		for item in node:
			print_ast(item, indent)
	else:
		if "/" in str(node) or "import" in str(node):
			print(' ' * indent + str(node))


if __name__ == '__main__':
	'''Used as a test for the python bindings'''
	ast_extractor = ASTExtractor("ASTExtractor/ASTExtractor-0.5.jar", "ASTExtractor/ASTExtractor.properties")
	ast = ast_extractor.parse_folder(repo_path, representation="JSON")
	# ast = json.loads(ast_extractor.parse_folder(repo_path, representation="JSON"))
	print(ast)
	# print_ast(ast, 0)
	ast_extractor.close()



