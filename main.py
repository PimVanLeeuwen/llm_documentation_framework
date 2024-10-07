"""
Main file in the LLM Documentation Framework
Autor -- Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""

from tree import abstract_tree
from openai import OpenAI
from tree.abstract_tree import ASTNode, ASTNodeType, AbstractSyntaxTree
from folder_operations.folders_and_files import contains_files, create_tree_from_files
from llm.llm_query import query_llm

repo_path = '/home/pimvanleeuwen/Documents/Train-Ticket-Reservation-System'

if __name__ == '__main__':
	# setup the LLM client
	client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

	print("-- START AST GENERATION --")
	ast = create_tree_from_files(repo_path, ".java")
	print("-- END AST GENERATION --")

	# print(ast)

	counter = 0
	for node in ast:
		if counter == 3:
			break
		elif node.node_type == ASTNodeType.METHOD:
			query_llm(client, ast, node)
			counter += 1







