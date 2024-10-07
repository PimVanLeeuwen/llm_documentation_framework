# needed for the LLM interface
from openai import OpenAI
from llm.prompt import SYS_PROMPT, USR_PROMPT



def query_llm(client, tree, node):
	"""given a file and the corresponding tree, query the LLM to generate documentation and return the output"""

	prompt = SYS_PROMPT.replace("{project_structure_prefix}", tree.root.name)
	prompt = prompt.replace("{project_structure}", str(tree))
	prompt = prompt.replace("{file_path}", node.get_path())
	prompt = prompt.replace("{name}", node.name)
	prompt = prompt.replace("{code_content}", node.content)

	history = [
		{"role": "system",
		 "content": prompt},
		{"role": "user",
		 "content": USR_PROMPT},
	]

	print("-- START PROMPT --")
	print(prompt)
	print("-- END PROMPT --")

	completion = client.chat.completions.create(
		model="TheBloke/CodeLlama-7B-GGUF",
		messages=history,
		temperature=0.7,
		stream=False,
	)

	result = completion.choices[0].message.content
	print("-- START RESULT --")
	print(result)
	print("-- END RESULT --")
