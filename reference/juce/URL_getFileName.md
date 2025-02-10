#### getFileName()


 String URL::getFileName ( ) const 
 

Returns the file name.For all but Android's content:// scheme, it will simply return the last segment of the URL, e.g. for "http://www.xyz.com/foo/bar.txt", this will return "bar.txt".For Android's content:// scheme, it will attempt to resolve the filename located under the URL.