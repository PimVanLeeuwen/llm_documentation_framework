"""
Main file in the LLM Documentation Framework
Autor -- Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""

from openai import OpenAI
from folder_operations.folders_and_files import create_tree_from_files
from tree.tree_nodes import ASTNodeType, ASTNode
from llm.llm_query import query_llm
from tqdm import tqdm

repo_path = '/home/pimvanleeuwen/Documents/employer-worker-registration-system'

if __name__ == '__main__':
	# setup the LLM client
	client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

	# generate the AST
	ast = create_tree_from_files(repo_path, ".java")

	with open("outputs/ast.txt", "w") as f:
		f.write(str(ast))

	counter = 0

	for n in tqdm(ast, total=ast.get_nr_nodes(), desc="Generate Documentation from the LLM", unit="nodes"):
	# for n in tqdm(ast, total=ast.get_nr_nodes() ,desc="Check if all calls are mapped", unit="files"):
		if n.get_type() == ASTNodeType.METHOD:
			query_llm(client, ast, n)
			counter += 1
		if counter == 3:
			break







