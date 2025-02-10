#### createDateStampedLogger()


 static FileLogger \* FileLogger::createDateStampedLogger ( const String & logFileSubDirectoryName, const String & logFileNameRoot, const String & logFileNameSuffix, const String & welcomeMessage ) static 
 

Helper function to create a log file in the correct place for this platform.The filename used is based on the root and suffix strings provided, along with a time and date string, meaning that a new, empty log file will be always be created rather than appending to an existing one.The method might return nullptr if the file can't be created for some reason.Parameters

 logFileSubDirectoryName the name of the subdirectory to create inside the logs folder (as returned by getSystemLogFileFolder). It's best to use something like the name of your application here. 
 
 logFileNameRoot the start of the filename to use, e.g. "MyAppLog\_". This will have a timestamp and the logFileNameSuffix appended to it 
 logFileNameSuffix the file suffix to use, e.g. ".txt" 
 welcomeMessage a message that will be written to the log when it's opened.