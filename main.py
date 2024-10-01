"""
Main file in the LLM Documentation Framework
Autor -- Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""

# Needed for the files
from llm import prompt
from tree import abstract_tree
from openai import OpenAI
from tree.abstract_tree import ASTNode, ASTNodeType, AbstractSyntaxTree
from folder_operations.folders_and_files import contains_files, create_tree_from_files

repo_path = '/home/pimvanleeuwen/Documents/Train-Ticket-Reservation-System'

if __name__ == '__main__':
	# setup the LLM client
	client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

	print(create_tree_from_files(repo_path, ".java"))

	# query_llm("\n".join(java_files),
	# 		  "zerocode/core/src/main/java/org/jsmart/zerocode/core/domain/MockSteps.java",
	# 		  "getMocks()")




