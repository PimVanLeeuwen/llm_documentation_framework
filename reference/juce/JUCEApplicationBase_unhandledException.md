#### unhandledException()


 virtual void JUCEApplicationBase::unhandledException ( const std::exception \* , const String & sourceFilename, int lineNumber ) pure virtual 
 

If any unhandled exceptions make it through to the message dispatch loop, this callback will be triggered, in case you want to log them or do some other type of errorhandling.If the type of exception is derived from the std::exception class, the pointer passedin will be valid. If the exception is of unknown type, this pointer will be null.Implemented in JUCEApplication.