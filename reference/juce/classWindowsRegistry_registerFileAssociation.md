#### registerFileAssociation()


 static bool JUCE\_CALLTYPE WindowsRegistry::registerFileAssociation ( const String & fileExtension, const String & symbolicDescription, const String & fullDescription, const File & targetExecutable, int iconResourceNumber, bool registerForCurrentUserOnly, WoW64Mode mode = WoW64\_Default ) static 
 

Creates a file association in the registry.This lets you set the executable that should be launched by a given file extension.Parameters

 fileExtension the file extension to associate, including the initial dot, e.g. ".txt" 
 
 symbolicDescription a spacefree short token to identify the file type 
 fullDescription a humanreadable description of the file type 
 targetExecutable the executable that should be launched 
 iconResourceNumber the icon that gets displayed for the file type will be found by looking up this resource number in the executable. Pass 0 here to not use an icon 
 registerForCurrentUserOnly if false, this will try to register the association for all users (you might not have permission to do this unless running in an installer). If true, it will register the association in HKEY\_CURRENT\_USER. 
 mode the WoW64 mode to use for choosing the database