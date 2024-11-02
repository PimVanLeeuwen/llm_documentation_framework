import warnings

from antlr4 import *

from grammars.java.JavaLexer import JavaLexer
from grammars.java.JavaParser import JavaParser
from grammars.java.JavaParserListener import JavaParserListener
from tree.tree_nodes import *

# Create a listener for the Java project, from this we create the nodes and content of the nodes into the target
# format. Overrides the methods from JavaParserListener
class MyJavaListener(JavaParserListener):

    def __init__(self, current_node:ASTNode=None):
        # At the start this is the file node
        self.current_node = current_node
        self.return_node = current_node

    def get_return_node(self):
        return self.return_node

    # Import declarations, this is at the beginning of a file and comes in a file node
    def enterImportDeclaration(self, ctx: JavaParser.ImportDeclarationContext):
        if not self.current_node.get_type() == ASTNodeType.FILE:
            warnings.warn("You are appending imports to non-file node: " + str(self.current_node))
        self.current_node.add_import(ctx.qualifiedName().getText())

    # Enter class creations
    def enterClassDeclaration(self, ctx:JavaParser.classDeclaration):
        class_node = ASTNode(ctx.identifier().getText(), ASTNodeType.OBJECT, parent_node=self.current_node, content=ctx.getText())
        self.current_node.add_child(class_node)
        self.current_node = class_node

    # Exits classes, go back to parent node
    def exitClassDeclaration(self, ctx:JavaParser.classDeclaration):
        self.current_node = self.current_node.get_parent()

    # Call another method
    def enterMethodCall(self, ctx: JavaParser.MethodCallContext):
        self.current_node.add_call(ctx.getText())

    # Enter method creation
    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        method_node = ASTNode(ctx.identifier().getText(), ASTNodeType.METHOD, parent_node=self.current_node,
                             content=ctx.getText())
        self.current_node.add_child(method_node)
        self.current_node = method_node

        # Adding parameters to the method node
        if ctx.formalParameters().formalParameterList() is not None:
            for param in ctx.formalParameters().formalParameterList().formalParameter():
                start = param.start.start
                stop = param.stop.stop
                input_stream = param.start.getInputStream()
                text = input_stream.getText(start, stop)
                self.current_node.add_param(text)

    # Exit method
    def exitMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        self.current_node = self.current_node.get_parent()

def parse_java_file(path, file):
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