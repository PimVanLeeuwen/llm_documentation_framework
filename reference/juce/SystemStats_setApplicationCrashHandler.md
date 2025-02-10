#### setApplicationCrashHandler()


 static void SystemStats::setApplicationCrashHandler ( CrashHandlerFunction ) static 
 

Sets up a global callback function that will be called if the application executes some kind of illegal instruction.You may want to call getStackBacktrace() in your handler function, to find out where the problem happened and log it, etc.