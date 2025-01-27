#### execute()


 Result JavascriptEngine::execute ( const String & javascriptCode ) 
 

Attempts to parse and run a block of javascript code.If there's a parse or execution error, the error description is returned in the result. You can specify a maximum time for which the program is allowed to run, and it'll return with an error message if this time is exceeded.