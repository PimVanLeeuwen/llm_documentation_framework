#### createDefaultAppLogger()


 static FileLogger \* FileLogger::createDefaultAppLogger ( const String & logFileSubDirectoryName, const String & logFileName, const String & welcomeMessage, const int64 maxInitialFileSizeBytes = 128 \*1024 ) static 
 

Helper function to create a log file in the correct place for this platform.The method might return nullptr if the file can't be created for some reason.Parameters

 logFileSubDirectoryName the name of the subdirectory to create inside the logs folder (as returned by getSystemLogFileFolder). It's best to use something like the name of your application here. 
 
 logFileName the name of the file to create, e.g. "MyAppLog.txt". 
 welcomeMessage a message that will be written to the log when it's opened. 
 maxInitialFileSizeBytes (see the FileLogger constructor for more info on this)