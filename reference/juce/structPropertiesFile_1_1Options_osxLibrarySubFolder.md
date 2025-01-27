#### osxLibrarySubFolder


 String PropertiesFile::Options::osxLibrarySubFolder 
 

If you're using properties files on a Mac, you must set this value failure to do so will cause a runtime assertion.The PropertiesFile class always used to put its settings files in "Library/Preferences", but Apple have changed their advice, and now stipulate that settings should go in "Library/Application Support".Because older apps would be broken by a silent change in this class's behaviour, you must now explicitly set the osxLibrarySubFolder value to indicate which path you want to use.In newer apps, you should always set this to "Application Support" or "Application Support/YourSubFolderName".If your app needs to load settings files that were created by older versions of juce and you want to maintain backwardscompatibility, then you can set this to "Preferences". But.. for better Applecompliance, the recommended approach would be to write some code that finds your old settings files in ~/Library/Preferences, moves them to ~/Library/Application Support, and then uses the new path.