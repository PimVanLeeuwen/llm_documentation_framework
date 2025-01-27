#### currentFileIsValid()


 bool FileBrowserComponent::currentFileIsValid ( ) const 
 

Returns true if the currently selected file(s) are usable.This can be used to decide whether the user can press "ok" for the current file. What it does depends on the mode, so for example in an "open" mode, this only returns true if a file has been selected and if it exists. In a "save" mode, a nonexistent file would also be valid.