def find_declarations(data, field):
	"""Function to recursively search for a certain field in the JSON data"""
	if isinstance(data, dict):
		for key, value in data.items():
			if key == field:
				values = value if isinstance(value, list) else [value]
				for v in values:
					# Skip the comments, we want the first line that is not a comment
					for line in str(v).split('\n'):
						if not '*' in line and not line[:-1].strip() == "":
							yield line[:-1].strip() # leave out last bracket
							break
			# Recursively find methods
			elif isinstance(value, (dict, list)):
				yield from find_declarations(value, field)
	# Recursively find methods
	elif isinstance(data, list):
		for item in data:
			yield from find_declarations(item, field)