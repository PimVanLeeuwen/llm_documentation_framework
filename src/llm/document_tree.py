"""
Methods to document a AbstractSyntaxTree.

Author:
	Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""

import warnings

from collections import deque
from src.llm.document_node import document_node
from src.tree.tree_nodes import ASTNodeType
from src.tree.abstract_tree import AbstractSyntaxTree
from tqdm import tqdm

def document_tree(tree: AbstractSyntaxTree, llm_provider: str = "azure", llm_model: str = "openai.gpt-4o"):
    """
	This method recursively goes over the tree to create documentation.

	Args:
		tree (AbstractSyntaxTree): The tree to document.
		llm_provider (str, default = "azure") The provider to use for the LLM used in documentation
        llm_model (str, default = "openai.gpt-4o") The LLM model to use for documentation.
	"""

    # queue of nodes that can be documented
    documentation_queue = deque([node for node in tree if
                                 (node.can_document() and (node.get_type() in {ASTNodeType.METHOD, ASTNodeType.OBJECT}))])

    # Number of nodes to do for progress bar
    total_nodes_to_document = len([node for node in tree if (node.get_type() in {ASTNodeType.METHOD, ASTNodeType.OBJECT})])

    with tqdm(total=total_nodes_to_document, dynamic_ncols=True, leave=True, desc="Creating Documentation", unit="nodes") as pbar:
        while documentation_queue:
            # get the node to proces
            node = documentation_queue.popleft()

            # process the node
            document_node(node, llm_provider, llm_model)

            # this is just for the progress bar, which is nice if your program runs for quite a while
            pbar.update(1)

            # if the queue is emtpy we fill it again
            if not documentation_queue:
                documentation_queue = deque([node for node in tree if
                                             (node.can_document() and not node.has_documentation() and
                                              (node.get_type() in {ASTNodeType.METHOD, ASTNodeType.OBJECT}))])


                if not documentation_queue:
                    warnings.warn("No suitable targets for documentations")
                    documentation_queue = deque([node for node in tree if not node.has_documentation() and
                                                 node.get_type() in {ASTNodeType.METHOD, ASTNodeType.OBJECT}][:1])



    # Check if everything is documented, as it should be now
    if not tree.has_documentation():
        warnings.warn("Not the entire tree has been documented!!")