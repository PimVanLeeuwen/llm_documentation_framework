#### getLocationToBrowse()


 virtual File FilenameComponent::getLocationToBrowse ( ) virtual 
 

This can be overridden to return a custom location that you want the dialog box to show when the browse button is pushed.The default implementation of this method will return either the current file (if one has been chosen) or the location that was set by setDefaultBrowseTarget().