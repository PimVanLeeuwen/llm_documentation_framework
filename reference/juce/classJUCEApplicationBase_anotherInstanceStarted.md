#### anotherInstanceStarted()


 virtual void JUCEApplicationBase::anotherInstanceStarted ( const String & commandLine ) pure virtual 
 

Indicates that the user has tried to start up another instance of the app.This will get called even if moreThanOneInstanceAllowed() is false. It is currently only implemented on Windows and Mac.See alsomoreThanOneInstanceAllowed Implemented in JUCEApplication.