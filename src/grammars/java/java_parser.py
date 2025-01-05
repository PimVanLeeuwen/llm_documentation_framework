"""
Parser for Java files to AbstractSyntaxTree.

Author:
	Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""

import warnings

from antlr4 import *

from typing import override
from src.grammars.java.JavaLexer import JavaLexer
from src.grammars.java.JavaParser import JavaParser
from src.grammars.java.JavaParserListener import JavaParserListener
from src.tree.tree_nodes import ASTNodeType, ASTNode


# Create a listener for the Java project, from this we create the nodes and content of the nodes into the target
# format. Overrides the methods from JavaParserListener
class MyJavaListener(JavaParserListener):
    """Listener class to convert ANTLR AST to a AbstractSyntaxTree

    Args:
        (JavaParserListener): Abstract listener from ANTLR that is inherited from.
	"""

    def __init__(self, current_node:ASTNode=None):
        """initialize a MyJavaListener object

        Args:
            current_node (ASTNode): The node that is currently being processed.
        """
        # At the start this is the file node
        self.current_node = current_node
        self.return_node = current_node

    def get_return_node(self):
        """Returns the current node that is being processed.

        Returns:
            ASTNode: The current node.
        """
        return self.return_node

    @override
    def enterImportDeclaration(self, ctx: JavaParser.ImportDeclarationContext):
        """Enter an import declaration, this is at the beginning of a file and occurs in a ASTNodeType.FILE node

        Args:
            ctx (JavaParser.ImportDeclarationContext): context to parse along (from super).
        """
        if not self.current_node.get_type() == ASTNodeType.FILE:
            warnings.warn("You are appending imports to non-file node: " + str(self.current_node))
        self.current_node.add_import(ctx.qualifiedName().getText())

    @override
    def enterClassDeclaration(self, ctx: JavaParser.classDeclaration):
        """Enter class declaration, this produces a new ASTNodeType.CLASS node and makes it the current node.

        Args:
            ctx (JavaParser.classDeclaration): context to parse along (from super).
        """
        class_node = ASTNode(ctx.identifier().getText(), ASTNodeType.OBJECT, parent_node=self.current_node,
                             content=ctx.start.getInputStream().getText(ctx.start.start, ctx.stop.stop))
        self.current_node.add_child(class_node)
        self.current_node = class_node

    @override
    def exitClassDeclaration(self, ctx: JavaParser.classDeclaration):
        """Exit class declaration, this makes the current node the parent again.

        Args:
            ctx (JavaParser.classDeclaration): context to parse along (from super).
        """
        self.current_node = self.current_node.get_parent()

    @override
    def enterMethodCall(self, ctx: JavaParser.MethodCallContext):
        """Enter method call, this adds a call to the ASTNode calls variable via the ASTNode.add_call() method.

        Args:
            ctx (JavaParser.MethodCallContext): context to parse along (from super).
        """
        self.current_node.add_call(ctx.getText())

    @override
    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        """Enter method creation, this adds ASTNodeType.METHOD node and makes it the current node. It also adds
        parameters to the method node.

        Args:
            ctx (JavaParser.MethodDeclarationContext): context to parse along (from super).
        """
        method_node = ASTNode(ctx.identifier().getText(), ASTNodeType.METHOD, parent_node=self.current_node,
                             content=ctx.start.getInputStream().getText(ctx.start.start, ctx.stop.stop))

        self.current_node.add_child(method_node)
        self.current_node = method_node

        # Adding parameters to the method node
        if ctx.formalParameters().formalParameterList() is not None:
            for param in ctx.formalParameters().formalParameterList().formalParameter():
                start = param.start.start
                stop = param.stop.stop
                input_stream = param.start.getInputStream()
                text = input_stream.getText(start, stop)
                self.current_node.add_parameter(text)

    @override
    def exitMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        """exit method creation, set current node to parent again.

        Args:
            ctx (JavaParser.MethodDeclarationContext): context to parse along (from super).
        """
        self.current_node = self.current_node.get_parent()

def parse_java_file(path, file):
    """Parse a java file and return the tree rooted at the ASTNodeType.FILE node for this file.

    Args:
        path (str): Path to the java file.
        file (str): Name of the java file.

    Returns:
        ASTNode: Tree rooted at the ASTNodeType.FILE node.
    """
    input_stream = FileStream(path, encoding='utf-8')
    lexer = JavaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    tree = parser.compilationUnit()

    # This will be the full node of the file
    return_node = ASTNode(file, ASTNodeType.FILE)

    # This is a default Tree Walker
    walker = ParseTreeWalker()
    # This is the adapter JavaParserListener that we created above to adapt to our tree
    listener = MyJavaListener(return_node)
    # Perform the walk
    walker.walk(listener, tree)

    # return the processed node
    return listener.get_return_node()