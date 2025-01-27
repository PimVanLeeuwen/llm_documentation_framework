#### getDefaultFile()


 File PropertiesFile::Options::getDefaultFile ( ) const 
 

This can be called to suggest a file that should be used, based on the values in this structure.So on a Mac, this will return a file called: ~/Library/[osxLibrarySubFolder]/[folderName]/[applicationName].[filenameSuffix]On Windows it'll return something like: C:\Documents and Settings\username\Application Data\[folderName]\[applicationName].[filenameSuffix]On Linux it'll return ~/[folderName]/[applicationName].[filenameSuffix]If the folderName variable is empty, it'll use the app name for this (or omit the folder name on the Mac).The paths will also vary depending on whether commonToAllUsers is true.

Member Data Documentation