#### createTempFile()


 static File File::createTempFile ( StringRef fileNameEnding ) static 
 

Returns a temporary file in the system's temp directory.This will try to return the name of a nonexistent temp file. To get the temp folder, you can use getSpecialLocation (File::tempDirectory).