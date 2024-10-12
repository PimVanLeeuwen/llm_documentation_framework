from antlr4 import *
from grammars.java.JavaLexer import JavaLexer
from grammars.java.JavaParser import JavaParser
from grammars.java.JavaParserListener import JavaParserListener
from tree.abstract_tree import *

def parse_java_file(path, file):
    input_stream = FileStream(path, encoding='utf-8')
    lexer = JavaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    tree = parser.compilationUnit()

    return_node = ASTNode(file, ASTNodeType.FILE)
    current_node = return_node

    # Create a listener for the Java project
    class MyJavaListener(JavaParserListener):

        def enterImportDeclaration(self, ctx: JavaParser.ImportDeclarationContext):
            print("Import:", ctx.qualifiedName().getText())

        def enterClassDeclaration(self, ctx:JavaParser.classDeclaration):
            print("Enter ClassBody:", ctx.identifier().getText())

        def exitClassDeclaration(self, ctx:JavaParser.classDeclaration):
            print("Exit ClassBody:", ctx.identifier().getText())

        def enterMethodCall(self, ctx: JavaParser.MethodCallContext):
            print("Enter Method Call:", ctx.identifier().getText())
            print("Method Params:", ctx.arguments().getText())

        def exitMethodCall(self, ctx: JavaParser.MethodCallContext):
            print("Exit Method Call:", ctx.identifier().getText())

        def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
            print("Enter Method Declaration:", ctx.identifier().getText())
            print("Method content:", ctx.getText())

        def exitMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
            print("Exit Method Declaration:", ctx.identifier().getText())


        #
        # def enterMethodCall(self, ctx: JavaParser.MethodCallContext):
        #     print("Method Call:", ctx.getText())
        #
        # def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        #     print("Method Declaration:", ctx.getText())

    walker = ParseTreeWalker()
    listener = MyJavaListener()
    walker.walk(listener, tree)