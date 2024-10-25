# needed for the LLM interface
from llm.prompt import SYS_PROMPT
import ollama


def query_llm(client, tree, node):
	"""given a file and the corresponding tree, query the LLM to generate documentation and return the output"""

	prompt = SYS_PROMPT.replace("{project_structure_prefix}", tree.root.name)
	# prompt = prompt.replace("{project_structure}", str(tree))
	prompt = prompt.replace("{file_path}", node.get_path())
	prompt = prompt.replace("{name}", node.name)
	prompt = prompt.replace("{code_content}", node.content)
	param_list = node.get_param()
	call_list = node.get_calls()

	param_prompt = ""
	if param_list:
		param_prompt += "**Parameters**:\n"
		for param in param_list:
			param_prompt += f"`{param}`: *FILL IN* \n"
	prompt = prompt.replace("{parameters_or_attribute}", param_prompt)

	call_prompt = ""
	if call_list:
		call_prompt += "## Calls \ \n This code calls the following methods within the repository: \ \n"
		for call in call_list:
			call_prompt += f"`{call.get_path()}.{call.name}` \\n"
	prompt = prompt.replace("{function_calls}", call_prompt)

	with open(f"outputs/{node.name}_prompt.md", "w") as f:
		f.write("# PROMPT")
		f.write(prompt)

	response = ollama.chat(model='llama3.1', messages=[
		{
			'role': 'user',
			'content': prompt,
		},
	])

	with open(f"outputs/{node.name}_result.md", "w") as f:
		f.write(response['message']['content'])

		# completion = client.chat.completions.create(
		# 	model="lmstudio-community/Qwen2.5-Coder-7B-Instruct-GGUF",
		# 	messages=[{"role": "system", "content": prompt}],
		# 	temperature=0,
		# 	stream=False,
		# )

		# result = completion.choices[0].message.content

		# Some weird exclamation mark glitch
