"""
Parser for cpp files to AbstractSyntaxTree.

Author:
	Pim van Leeuwen (1303422, p.p.h.v.leeuwen@student.tue.nl)
"""

import warnings

from antlr4 import *

from src.grammars.cpp.CPP14Lexer import CPP14Lexer
from src.grammars.cpp.CPP14Parser import CPP14Parser
from src.grammars.cpp.CPP14ParserListener import CPP14ParserListener
from src.tree.tree_nodes import ASTNodeType, ASTNode

# Create a listener for the CPP14 project, from this we create the nodes and content of the nodes into the target
# format. Overrides the methods from CPP14ParserListener
class MyCPPListener(CPP14ParserListener):
    """Listener class to convert ANTLR AST to a AbstractSyntaxTree

    Args:
        (CPP14ParserListener): Abstract listener from ANTLR that is inherited from.
	"""

    def __init__(self, current_node:ASTNode=None):
        """initialize a MyCPPListener object

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

    #@override
    def enterPreprocessorDirective(self, ctx: CPP14Parser.PreprocessorDirectiveContext):
        """Enter an include statement, this is at the beginning of a file and occurs in a ASTNodeType.FILE node

        Args:
            ctx (CPP14Parser.PreprocessorDirectiveContext): context to parse along (from super).
        """
        if not self.current_node.get_type() == ASTNodeType.FILE:
            warnings.warn("You are appending imports to non-file node: " + str(self.current_node))
        self.current_node.add_import(ctx.Directive().getText())

    #@override
    def enterFunctionDefinition(self, ctx: CPP14Parser.FunctionDefinitionContext):
        """Enter method declaration, this produces a new ASTNodeType.METHOD node and makes it the current node.
        It also parses along the parameters of the method.

        Args:
            ctx (CPP14Parser.FunctionDefinitionContext): context to parse along (from super).
        """
        method_node = ASTNode(ctx.declarator().getText().split("(")[0].split("::")[-1], ASTNodeType.METHOD, parent_node=self.current_node,
                              content=ctx.start.getInputStream().getText(ctx.start.start, ctx.stop.stop))

        self.current_node.add_child(method_node)
        self.current_node = method_node

        # add the parameters
        try:
            for param in ctx.declarator().start.getInputStream().getText(ctx.declarator().start.start,
                                                                         ctx.declarator().stop.stop).split("(")[1].split(")")[0].split(","):
                if param: self.current_node.add_parameter(param.strip())
        except IndexError:
            warnings.warn("Parameters not found but somehow I am checking for it")

    #@override
    def exitFunctionDefinition(self, ctx: CPP14Parser.FunctionDefinitionContext):
        """Exit method declaration, this makes the current node the parent again.

        Args:
            ctx (CPP14Parser.FunctionDefinitionContext): context to parse along (from super).
        """
        self.current_node = self.current_node.get_parent()


    #@override
    def enterNamespaceDefinition(self, ctx: CPP14Parser.NamespaceDefinitionContext):
        """Enter namespace definition, this creates a ASTNodeType.OBJECT node and makes it the current node.

        Args:
            ctx (CPP14Parser.NamespaceDefinitionContext): context to parse along (from super).
        """
        object_node = ASTNode(ctx.Identifier().getText(), ASTNodeType.OBJECT, parent_node=self.current_node, content=ctx.start.getInputStream().getText(ctx.start.start, ctx.stop.stop))
        self.current_node.add_child(object_node)
        self.current_node = object_node

    #@override
    def exitNamespaceDefinition(self, ctx:CPP14Parser.NamespaceDefinitionContext):
        """exit namespace definition, make parent node the current node again.

        Args:
            ctx (CPP14Parser.NamespaceDefinitionContext): context to parse along (from super).
        """
        self.current_node = self.current_node.get_parent()

    #@override
    def enterPostfixExpression(self, ctx: CPP14Parser.PostfixExpressionContext):
        """make a call to another method, add that to the current ASTNode.

        Args:
            ctx (CPP14Parser.PostfixExpressionContext): context to parse along (from super).
        """
        self.current_node.add_call(ctx.getText())

    #DISADVANTAGE: ANTLR Parser for CPP does not support class creation listings



def parse_cpp_file(path, file):
    """Parse a cpp file and return the tree rooted at the ASTNodeType.FILE node for this file.

    Args:
        path (str): Path to the java file.
        file (str): Name of the java file.

    Returns:
        ASTNode: Tree rooted at the ASTNodeType.FILE node.
    """

    input_stream = FileStream(path, encoding='utf-8')
    lexer = CPP14Lexer(input_stream)
    # not all c++ projects adhere fully to the grammar, ignore the errors
    lexer.removeErrorListeners()
    stream = CommonTokenStream(lexer)
    parser = CPP14Parser(stream)
    # not all c++ projects adhere fully to the grammar, ignore the errors
    parser.removeErrorListeners()
    tree = parser.translationUnit()

    # This will be the full node of the file
    return_node = ASTNode(file, ASTNodeType.FILE)

    # This is a default Tree Walker
    walker = ParseTreeWalker()
    # This is the adapter JavaParserListener that we created above to adapt to our tree
    listener = MyCPPListener(return_node)
    # Perform the walk
    walker.walk(listener, tree)

    # return the processed node
    return listener.get_return_node()