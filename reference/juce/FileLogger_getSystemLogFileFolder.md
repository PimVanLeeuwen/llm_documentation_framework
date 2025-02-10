#### getSystemLogFileFolder()


 static File FileLogger::getSystemLogFileFolder ( ) static 
 

Returns an OSspecific folder where logfiles should be stored.On Windows this will return a logger with a path such as: c:\Documents and Settings\username\Application Data\[logFileSubDirectoryName]\[logFileName]On the Mac it'll create something like: ~/Library/Logs/[logFileSubDirectoryName]/[logFileName]See alsocreateDefaultAppLogger