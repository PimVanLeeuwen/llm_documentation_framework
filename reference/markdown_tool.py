"""
Small script to convert html to markdown.

Author:
	Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""

import os
import re
from markdownify import markdownify as md

CONVERT_JAVA = False
CONVERT_CPP = False

######################################################################################################################################
# The piece below is for the Java Util generation, these are not very fancy/structured because they are very specific and incidental #
######################################################################################################################################

if CONVERT_CPP:
	for root, dirs, files in os.walk("juce_official"):
		for file in files:
			if file.endswith(".html"):
				# print(file)
				html_file_path = os.path.join(root, file)
				with open(html_file_path, 'r', encoding='utf-8') as f:
					html_content = f.read()
					markdown_content = md(html_content, convert=['dd', 'pre', 'tt', 'tr', 'td', 'h4', 'h3', 'h2', 'code', 'table', 'div', 'dt', 'span'])

				# Trim everything before the first code block
				if len(markdown_content.split("Detailed Description\n--------------------", 1)) > 1:
					markdown_content = markdown_content.split("Detailed Description\n--------------------", 1)[1].strip()
				else:
					continue

				# Trim everything after the information
				markdown_content = markdown_content.split("The documentation for this class was generated from the following", 1)[0].strip()

				# Trim everything between "See Also:" and "### Method Detail" (keep "### Method Detail")
				markdown_content = re.sub(r'\n.*?(?=Member Function Documentation)', '\n', markdown_content, flags=re.DOTALL)
				markdown_content = markdown_content.replace('|', '').replace('-', '')
				markdown_content = re.sub(r' {2,}', ' ', markdown_content)

				markdown_class_summary = markdown_content.split("Member Function Documentation\n")[0]

				markdown_methods = []
				for method in markdown_content.split('◆')[1:]:
					markdown_methods.append("#### " + method.strip())

				file_base = '.'.join(file.rsplit('.', 1)[:-1])
				markdown_file_path = os.path.join(root, file_base + '.md')
				with open(markdown_file_path, 'w', encoding='utf-8') as f:
					f.write(markdown_class_summary)
				for method in markdown_methods:
					try:
						file_path = os.path.join(root, file_base + "_" + re.split(r'[\s\n]+', method)[1].replace('()', '') + '.md')
						with open(file_path, 'w', encoding='utf-8') as f:
							f.write(method)
					except FileNotFoundError:
						print(method)
######################################################################################################################################
# The piece below is for the Java Util generation, these are not very fancy/structured because they are very specific and incidental #
######################################################################################################################################

if CONVERT_JAVA:
	for root, dirs, files in os.walk("."):
		for file in files:
			if file.endswith(".html"):
				print(file)
				html_file_path = os.path.join(root, file)
				with open(html_file_path, 'r', encoding='utf-8') as f:
					html_content = f.read()
					markdown_content = md(html_content, convert=['dd', 'pre', 'tt', 'h4', 'h3', 'code', 'table', 'div', 'dt', 'span'])

				# Trim everything before the first code block
				markdown_content = "```" + markdown_content.split("```", 1)[1] if len(markdown_content.split("```", 1)) > 1 else markdown_content

				# Trim everything after the information
				markdown_content = markdown_content.split("Skip navigation links", 1)[0]

				markdown_class_summary = markdown_content.split("\n### ")[0]
				markdown_methods_all = ""
				for section in markdown_content.split("\n### ")[1:]:
					if "Method Detail" in section:
						markdown_methods_all += "\n### " + section

				markdown_methods = []
				for method in markdown_methods_all.split("####")[1:]:
					markdown_methods.append("####" + method)

				# # Trim everything after and including the sentence "Skip navigation links"
				# markdown_content = re.sub(r'Skip navigation links.*$', '', markdown_content, flags=re.DOTALL)
				#
				# # Trim everything between "See Also:" and "### Method Detail" (keep "### Method Detail")
				# markdown_content = re.sub(r'See Also:.*?(?=### Method Detail)', '', markdown_content, flags=re.DOTALL)

				file_base = '.'.join(file.rsplit('.', 1)[:-1])
				markdown_file_path = os.path.join(root, file_base + '.md')
				with open(markdown_file_path, 'w', encoding='utf-8') as f:
					f.write(markdown_class_summary)
				for method in markdown_methods:
					file_path = os.path.join(root, file_base + "_" + re.split(r'[\s\n]+', method)[1] + '.md')
					with open(file_path, 'w', encoding='utf-8') as f:
						f.write(method)

