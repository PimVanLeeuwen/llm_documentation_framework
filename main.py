"""
Main file in the LLM Documentation Framework
Autor -- Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""
from prompt import SYS_PROMPT, USR_PROMPT

repo_path = '/home/pimvanleeuwen/Documents/zerocode'

from ASTExtractor.astextractor import ASTExtractor
import json
# Needed for the files
import os
# needed for the LLM interface
from openai import OpenAI
import prompt

def contains_java_files(dir_path):
		"""Check if a directory or any of its subdirectories contain .java files."""
		for root, dirs, files in os.walk(dir_path):
			if any(file.endswith(".java") for file in files):
				return True
		return False

def list_java_files(directory, prefix=""):
	"""given a directory, create a string that outputs all of the .java files in a tree-like structure"""
	java_files = []
	for root, dirs, files in os.walk(directory):
		# Filter out directories that do not contain any .java files
		if contains_java_files(root):
			level = root.replace(directory, '').count(os.sep)
			indent = '    ' * (level)
			sub_indent = '    ' * (level + 1)
			java_files.append(f"{indent}└── {os.path.basename(root)}/")
			for file in files:
				if file.endswith(".java"):
					java_files.append(f"{sub_indent}└── {file}")
	return java_files

def print_tree(files):
	"""Print an entire str file to display the tree"""
	for line in files:
		print(line)

def query_llm(tree, file, method):
	"""given a file and the corresponding tree, query the LLM to generate documentation and return the output"""

	prompt = SYS_PROMPT.replace("{project_structure_prefix}", "zerocode")
	prompt = prompt.replace("{project_structure}", tree)
	prompt = prompt.replace("{file_path}", file)
	prompt = prompt.replace("{method_name}", method)
	prompt = prompt.replace("{code_content}", """
												public List<MockStep> getMocks() {
													return mocks == null ? (new ArrayList<>()) : mocks;
												}""")

	history = [
		{"role": "system",
		 "content": prompt},
		{"role": "user",
		 "content": USR_PROMPT},
	]


	completion = client.chat.completions.create(
		model="TheBloke/CodeLlama-7B-GGUF",
		messages=history,
		temperature=0.7,
		stream=False,
	)

	result = completion.choices[0].message.content
	print(result)


if __name__ == '__main__':
	# setup the LLM client
	client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

	# ast_extractor = ASTExtractor("ASTExtractor/ASTExtractor-0.5.jar", "ASTExtractor/ASTExtractor.properties")
	# ast = ast_extractor.parse_folder(repo_path, representation="JSON")
	# # ast = json.loads(ast_extractor.parse_folder(repo_path, representation="JSON"))
	# print(ast)
	# # print_ast(ast, 0)
	# ast_extractor.close()

	java_files = list_java_files(repo_path)
	print_tree(java_files)

	print("STARTING PROMPT")

	query_llm("\n".join(java_files),
			  "zerocode/core/src/main/java/org/jsmart/zerocode/core/domain/MockSteps.java",
			  "getMocks()")




