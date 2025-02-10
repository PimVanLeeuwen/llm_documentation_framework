#### setApplicationReturnValue()


 void JUCEApplicationBase::setApplicationReturnValue ( int newReturnValue ) noexcept 
 

Sets the value that should be returned as the application's exit code when the app quits.This is the value that's returned by the main() function. Normally you'd leave this as 0 unless you want to indicate an error code.See alsogetApplicationReturnValue