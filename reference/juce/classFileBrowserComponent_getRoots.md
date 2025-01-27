#### getRoots()


 virtual void FileBrowserComponent::getRoots ( StringArray & rootNames, StringArray & rootPaths ) protectedvirtual 
 

Returns a list of names and paths for the default places the user might want to look.By default this just calls getDefaultRoots(), but you may want to override it to return a custom list.