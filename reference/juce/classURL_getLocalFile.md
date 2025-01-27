#### getLocalFile()


 File URL::getLocalFile ( ) const 
 

Returns the file path of the local file to which this URL refers to.If the URL does not represent a local file URL (i.e. the URL's scheme is not 'file') then this method will assert.This method also supports converting Android's content:// URLs to local file paths.See alsoisLocalFile