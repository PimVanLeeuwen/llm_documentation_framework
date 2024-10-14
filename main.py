"""
Main file in the LLM Documentation Framework
Autor -- Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""

from openai import OpenAI
from folder_operations.folders_and_files import create_tree_from_files

repo_path = '/home/pimvanleeuwen/Documents/employer-worker-registration-system'

if __name__ == '__main__':
	# setup the LLM client
	client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

	ast = create_tree_from_files(repo_path, ".java")
	print(ast)

	# print(ast)

	# counter = 0
	# for node in ast:
	# 	if counter == 3:
	# 		break
	# 	elif node.node_type == ASTNodeType.METHOD:
	# 		query_llm(client, ast, node)
	# 		counter += 1







