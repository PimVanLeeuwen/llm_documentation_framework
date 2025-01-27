#### setCurrentLogger()


 static void JUCE\_CALLTYPE Logger::setCurrentLogger ( Logger \* newLogger ) staticnoexcept 
 

Sets the current logging class to use.Note that the object passed in will not be owned or deleted by the logger, so the caller must make sure that it is not deleted while still being used. A null pointer can be passedin to reset the system to the default logger.