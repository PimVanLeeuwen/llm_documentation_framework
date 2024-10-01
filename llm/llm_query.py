# needed for the LLM interface
from openai import OpenAI



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