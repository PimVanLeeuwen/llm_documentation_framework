#### outputDebugString()


 static void JUCE\_CALLTYPE Logger::outputDebugString ( const String & text ) static 
 

Writes a message to the standard error stream.This can be called directly, or by using the DBG() macro in juce\_PlatformDefs.h (which will avoid calling the method in nondebug builds).