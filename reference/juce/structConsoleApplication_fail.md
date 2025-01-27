#### fail()


 static void ConsoleApplication::fail ( String errorMessage, int returnCode = 1 ) static 
 

Throws a failure exception to cause a commandline app to terminate.This is intended to be called from code in a Command, so that the exception will be automatically caught and turned into a printed error message and a return code which will be returned from main().See alsoConsoleApplication::invokeCatchingFailures()