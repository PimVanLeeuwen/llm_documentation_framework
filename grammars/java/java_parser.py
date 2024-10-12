from antlr4 import *
from grammars.java.JavaLexer import JavaLexer
from grammars.java.JavaParser import JavaParser
from grammars.java.JavaParserListener import JavaParserListener
from tree.abstract_tree import *

# Create a listener for the Java project, from this we create the nodes and content of the nodes into the target
# format. Overrides the methods from JavaParserListener
class MyJavaListener(JavaParserListener):

    # Import declarations
    def enterImportDeclaration(self, ctx: JavaParser.ImportDeclarationContext):
        print("Import:", ctx.qualifiedName().getText())

    # Enter class creations
    def enterClassDeclaration(self, ctx:JavaParser.classDeclaration):
        print("Enter ClassBody:", ctx.identifier().getText())

    # Exits classes
    def exitClassDeclaration(self, ctx:JavaParser.classDeclaration):
        print("Exit ClassBody:", ctx.identifier().getText())

    # Call another method
    def enterMethodCall(self, ctx: JavaParser.MethodCallContext):
        print("Enter Method Call:", ctx.identifier().getText())
        print("Method Params:", ctx.arguments().getText())

    # Enter method creation
    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        print("Enter Method Declaration:", ctx.identifier().getText())
        print("Method content:", ctx.getText())

    # Exit method
    def exitMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        print("Exit Method Declaration:", ctx.identifier().getText())

def parse_java_file(path, file):
    input_stream = FileStream(path, encoding='utf-8')
    lexer = JavaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    tree = parser.compilationUnit()

    # This will be the full node of the file
    return_node = ASTNode(file, ASTNodeType.FILE)
    # This will be the node that we are currently add throughout the process. Since we only go up or down one level
    # at a time this should work out
    # Still need to work out how to do this through the listener
    current_node = return_node

    # This is a default Tree Walker
    walker = ParseTreeWalker()
    # This is the adapter JavaParserListener that we created above to adapt to our tree
    listener = MyJavaListener()
    # Perform the walk
    walker.walk(listener, tree)

    # return the node of this file and then we parsed a Java file
    return return_node