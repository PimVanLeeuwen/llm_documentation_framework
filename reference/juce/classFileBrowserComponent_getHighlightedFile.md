#### getHighlightedFile()


 File FileBrowserComponent::getHighlightedFile ( ) const noexcept 
 

This returns the last item in the view that the user has highlighted.This may be different from getCurrentFile(), which returns the value that is shown in the filename box, and if there are multiple selections, this will only return one of them.See alsogetSelectedFile