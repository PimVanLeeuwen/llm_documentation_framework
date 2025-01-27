#### getResults()


 Array< File > FileChooser::getResults ( ) const noexcept 
 

Returns a list of all the files that were chosen during the last call to a browse method.On mobile platforms, the file browser may return a URL instead of a local file. Therefore, on mobile platforms, you should call getURLResults() instead.This array may be empty if no files were chosen, or can contain multiple entries if multiple files were chosen.See alsogetURLResults, getResult