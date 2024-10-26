import os
import warnings
import ollama

from collections import deque
from llm.document_node import document_node
from tree.tree_nodes import ASTNodeType
from tree.abstract_tree import AbstractSyntaxTree
from tqdm import tqdm

def document_tree(tree: AbstractSyntaxTree):

    # queue of nodes that can be documented
    documentation_queue = deque([node for node in tree if
                                 (node.can_document() and
                                  (node.get_type() == ASTNodeType.METHOD or node.get_type() == ASTNodeType.CLASS))])

    total_nodes_to_document = len([node for node in tree if (node.get_type() == ASTNodeType.METHOD or node.get_type() == ASTNodeType.CLASS)])

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
                                              (node.get_type() == ASTNodeType.METHOD or node.get_type() == ASTNodeType.CLASS))])


                if not documentation_queue:
                    warnings.warn("No suitable targets for documentations")
                    for node in tree:
                        if not node.has_documentation() and (node.get_type() == ASTNodeType.METHOD or node.get_type() == ASTNodeType.CLASS):
                            documentation_queue = deque([node])
                            break



    if not tree.has_documentation():
        warnings.warn("Not the entire tree has been documented!!")