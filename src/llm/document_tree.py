import warnings

from collections import deque
from src.llm.document_node import document_node
from src.tree.tree_nodes import ASTNodeType
from src.tree.abstract_tree import AbstractSyntaxTree
from tqdm import tqdm

def document_tree(tree: AbstractSyntaxTree):
    """
	This method recusively goes over the tree to create documentation.

	Args:
		tree (AbstractSyntaxTree): The tree to document.
	"""

    # queue of nodes that can be documented
    documentation_queue = deque([node for node in tree if
                                 (node.can_document() and
                                  (node.get_type() == ASTNodeType.METHOD or node.get_type() == ASTNodeType.OBJECT))])

    # Number of nodes to do for progress bar
    total_nodes_to_document = len([node for node in tree if (node.get_type() == ASTNodeType.METHOD or node.get_type() == ASTNodeType.OBJECT)])

    with tqdm(total=total_nodes_to_document, dynamic_ncols=True, leave=True, desc="Creating Documentation", unit="nodes") as pbar:
        while documentation_queue:
            # get the node to proces
            node = documentation_queue.popleft()

            # process the node
            document_node(node)

            # this is just for the progress bar, which is nice if your program runs for quite a while
            pbar.update(1)

            # if the queue is emtpy we fill it again
            if not documentation_queue:
                documentation_queue = deque([node for node in tree if
                                             (node.can_document() and not node.has_documentation() and
                                              (node.get_type() == ASTNodeType.METHOD or node.get_type() == ASTNodeType.OBJECT))])


                if not documentation_queue:
                    warnings.warn("No suitable targets for documentations")
                    for node in tree:
                        if not node.has_documentation() and (node.get_type() == ASTNodeType.METHOD or node.get_type() == ASTNodeType.OBJECT):
                            documentation_queue = deque([node])
                            break


    # Check if everything is documented, as it should be now
    if not tree.has_documentation():
        warnings.warn("Not the entire tree has been documented!!")