"""
Small script to convert html to markdown.

Author:
	Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""

import os
import re
from markdownify import markdownify as md

for root, dirs, files in os.walk("."):
	for file in files:
		if file.endswith(".html"):
			print(file)
			html_file_path = os.path.join(root, file)
			with open(html_file_path, 'r', encoding='utf-8') as f:
				html_content = f.read()
				markdown_content = md(html_content, convert=['dd', 'pre', 'tt', 'h4', 'h3', 'code', 'table', 'div', 'dt', 'span'])

			# Trim everything before the first code block
			markdown_content = re.sub(r'^.*?(´´´)', r'\1', markdown_content, flags=re.DOTALL)

			# # Trim everything after and including the sentence "Skip navigation links"
			# markdown_content = re.sub(r'Skip navigation links.*$', '', markdown_content, flags=re.DOTALL)
			#
			# # Trim everything between "See Also:" and "### Method Detail" (keep "### Method Detail")
			# markdown_content = re.sub(r'See Also:.*?(?=### Method Detail)', '', markdown_content, flags=re.DOTALL)

			file_base = '.'.join(file.rsplit('.', 1)[:-1])
			markdown_file_path = os.path.join(root, file_base + '.md')
			with open(markdown_file_path, 'w', encoding='utf-8') as f:
				f.write(markdown_content)
