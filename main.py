"""
Main file in the LLM Documentation Framework
Autor -- Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""

from openai import OpenAI
from folder_operations.folders_and_files import create_tree_from_files
from tree.tree_nodes import ASTNodeType, ASTNode

repo_path = '/home/pimvanleeuwen/Documents/employer-worker-registration-system'

if __name__ == '__main__':
	# setup the LLM client
	client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

	ast = create_tree_from_files(repo_path, ".java")

	with open("out.txt", "w") as f:
		f.write(str(ast))
		f.write("\n")

		method_list = []

		for n in ast:
			if n.get_type() == ASTNodeType.METHOD:
				# Only methods of classes are interesting here
				if n.get_parent().get_type() == ASTNodeType.CLASS:
					method_list.append(f"{n.get_parent().get_name()}.{n.get_name()}")
		f.write(str(method_list))







