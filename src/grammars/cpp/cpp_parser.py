import warnings

from antlr4 import *

from src.grammars.cpp.CPP14Lexer import CPP14Lexer
from src.grammars.cpp.CPP14Parser import CPP14Parser
from src.grammars.cpp.CPP14ParserListener import CPP14ParserListener
from src.tree.tree_nodes import ASTNodeType, ASTNode

# Create a listener for the CPP14 project, from this we create the nodes and content of the nodes into the target
# format. Overrides the methods from CPP14ParserListener
class MyCPPListener(CPP14ParserListener):

    def __init__(self, current_node:ASTNode=None):
        # At the start this is the file node
        self.current_node = current_node
        self.return_node = current_node

    def get_return_node(self):
        return self.return_node

    # Import declarations, this is at the beginning of a file and comes in a file node
    def enterPreprocessorDirective(self, ctx: CPP14Parser.PreprocessorDirectiveContext):
        if not self.current_node.get_type() == ASTNodeType.FILE:
            warnings.warn("You are appending imports to non-file node: " + str(self.current_node))
        self.current_node.add_import(ctx.Directive().getText())

    # Enter Method Creation
    def enterFunctionDefinition(self, ctx:CPP14Parser.FunctionDefinitionContext):
        method_node = ASTNode(ctx.declarator().getText(), ASTNodeType.METHOD, parent_node=self.current_node,
                              content=ctx.functionBody().getText())
        # TODO: Parameters?

        self.current_node.add_child(method_node)
        self.current_node = method_node

    # Exit method
    def exitFunctionDefinition(self, ctx:CPP14Parser.FunctionDefinitionContext):
        self.current_node = self.current_node.get_parent()


    # Enter class creations
    def enterNamespaceDefinition(self, ctx:CPP14Parser.NamespaceDefinitionContext):
        object_node = ASTNode(ctx.Identifier().getText(), ASTNodeType.OBJECT, parent_node=self.current_node, content=ctx.getText())
        self.current_node.add_child(object_node)
        self.current_node = object_node

    # Exits classes, go back to parent node
    def exitNamespaceDefinition(self, ctx:CPP14Parser.NamespaceDefinitionContext):
        self.current_node = self.current_node.get_parent()

    def enterUnaryExpression(self, ctx:CPP14Parser.UnaryExpressionContext):
        print()

    # Call another method
    def enterPostfixExpression(self, ctx: CPP14Parser.PostfixExpressionContext):
        # self.current_node.add_call(ctx.getText())
        print("=== BEGIN ===")
        print(ctx.getText())
        if ctx.LeftParen(): print("Left: " + ctx.LeftParen().getText())
        if ctx.RightParen(): print("Right: " + ctx.RightParen().getText())
        if ctx.bracedInitList(): print("Braced: " + ctx.bracedInitList().getText())
        if ctx.expressionList(): print("Espression: " + ctx.expressionList().getText())
        if ctx.primaryExpression(): print("primary: " + ctx.primaryExpression().getText())
        if ctx.simpleTypeSpecifier(): print("simpleType: " + ctx.simpleTypeSpecifier().getText())
        if ctx.typeNameSpecifier(): print("TypeName: " + ctx.typeNameSpecifier().getText())
        print()
        print("==== END ====")

        # if text[-1] == ")":
        #     # print(text.split(".")[-1])
        #     self.current_node.add_call(text)

    def enterEveryRule(self, ctx):
        rule_name = CPP14Parser.ruleNames[ctx.getRuleIndex()]
        print(f"Entering rule: {rule_name}")

def parse_cpp_file(path, file):
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