#### getNumSelectedFiles()


 int FileBrowserComponent::getNumSelectedFiles ( ) const noexcept 
 

Returns the number of files that the user has got selected.If multiple select isn't active, this will only be 0 or 1. To get the complete list of files they've chosen, pass an index to getCurrentFile().