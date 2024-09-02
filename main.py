"""
Main file in the LLM Documentation Framework
Autor -- Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""
repo_path = '/home/pimvanleeuwen/Documents/zerocode'

from ASTExtractor.astextractor import ASTExtractor

if __name__ == '__main__':
	'''Used as a test for the python bindings'''
	ast_extractor = ASTExtractor("ASTExtractor/ASTExtractor-0.5.jar", "ASTExtractor/ASTExtractor.properties")
	ast = ast_extractor.parse_folder(repo_path, representation="JSON")
	print(ast)
	ast_extractor.close()



