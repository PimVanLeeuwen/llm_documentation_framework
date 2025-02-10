#### closeFiles()


 void ApplicationProperties::closeFiles ( ) 
 

Flushes and closes both files if they are open.This flushes any pending changes to disk with PropertiesFile::saveIfNeeded() and closes both files. They will then be reopened the next time getUserSettings() or getCommonSettings() is called.