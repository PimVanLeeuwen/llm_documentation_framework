# needed for the LLM interface
import os
import warnings
import ollama

from tree.tree_nodes import ASTNode, ASTNodeType
from llm.prompt import METHOD_PROMPT

def document_node(node: ASTNode):
	"""given a method node and the corresponding tree, query the LLM to generate documentation and return the output"""

	# set the repo name
	prompt = METHOD_PROMPT.replace("{project_structure_prefix}", node.get_path().split("/")[0])
	# set the path of the node
	prompt = prompt.replace("{file_path}", node.get_path())
	# set the name of the method/class
	prompt = prompt.replace("{name}", node.get_name())
	# set the content of the code
	prompt = prompt.replace("{code_content}", node.get_content())

	# set the type of the node
	# This will warn if we document an unsupported node
	match node.get_type():
		case ASTNodeType.METHOD:
			prompt = prompt.replace("{type}", "Method")
		case ASTNodeType.OBJECT:
			prompt = prompt.replace("{type}", "Class")
		case _ :
			warnings.warn("You are trying to document the following node: " + str(node))

	# fetch the parameters and add these
	param_list = node.get_parameters()

	param_prompt = ""
	if param_list:
		param_prompt += "**Parameters**:\\\n"
		for param in param_list:
			param_prompt += f"`{param}`: *FILL IN* \\\n"
	prompt = prompt.replace("{parameters_or_attribute}", param_prompt)

	# fetch the calls and add these
	call_list = node.get_calls()

	call_prompt = ""
	if call_list:
		call_prompt += "## Calls \\\n This code calls the following methods within the repository: \\\n"
		for call in call_list:
			# This should become the documentation
			call_prompt += f"### {call.get_path()}.{call.name} \\\n"
			# if call.has_documentation():
			# 	call_prompt += f"{call.get_documentation()} \\\n"

	prompt = prompt.replace("{function_calls}", call_prompt)

	# fetch the calls and add these
	children = node.get_children()

	children_prompt = ""
	if children:
		children_prompt += "## Children \\\n This code contains the following methods/classes: \\\n"
		for child in children:
			# This should become the documentation
			children_prompt += f"### {child.get_path()}.{child.name} \\\n"
			# if child.has_documentation():
			# 	children_prompt += f"{child.get_documentation()} \\\n"
	prompt = prompt.replace("{children}", children_prompt)

	# add the prompt so that we can inspect it later
	os.makedirs(os.path.dirname(f"prompts/{node.get_path()}/{node.get_name()}.md"), exist_ok=True)
	with open(f"prompts/{node.get_path()}/{node.get_name()}.md", "w") as f:
		f.write("# PROMPT")
		f.write(prompt)

	# prompt the llm
	response = ollama.chat(model='llama3.1', messages=[
		{
			'role': 'user',
			'content': prompt,
		},
	])

	# set the comment in the node
	node.set_documentation(response['message']['content'])

	# write the comment to the documentation
	os.makedirs(os.path.dirname(f"documentation/{node.get_path()}/{node.get_name()}.md"), exist_ok=True)
	with open(f"documentation/{node.get_path()}/{node.get_name()}.md", "w") as f:
		f.write(node.get_documentation())
