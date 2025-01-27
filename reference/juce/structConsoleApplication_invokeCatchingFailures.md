#### invokeCatchingFailures()


 static int ConsoleApplication::invokeCatchingFailures ( std::function< int()> && functionToCall ) static 
 

Invokes a function, catching any fail() calls that it might trigger, and handling them by printing their error message and returning their error code.See alsoConsoleApplication::fail()