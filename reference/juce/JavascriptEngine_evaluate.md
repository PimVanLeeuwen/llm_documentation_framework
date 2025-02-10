#### evaluate()


 var JavascriptEngine::evaluate ( const String & javascriptCode, 
 
 Result \* errorMessage = nullptr ) 

Attempts to parse and run a javascript expression, and returns the result.If there's a syntax error, or the expression can't be evaluated, the return value will be var::undefined(). The errorMessage parameter gives you a way to find out any parsing errors. If the expression is successfully evaluated but yields no result the return value will be a void var. You can specify a maximum time for which the program is allowed to run, and it'll return with an error message if this time is exceeded.