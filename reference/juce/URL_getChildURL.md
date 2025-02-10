#### getChildURL()


 URL URL::getChildURL ( const String & subPath ) const 
 

Returns a new URL that refers to a subpath relative to this one.e.g. if the URL is "http://www.xyz.com/foo" and you call this with "bar", it'll return "http://www.xyz.com/foo/bar".Note that there's no way for this method to know whether the original URL is a file or directory, so it's up to you to make sure it's a directory. It also won't attempt to be smart about the content of the childPath string, so if this string is an absolute URL, it'll still just get bolted onto the end of the path.See alsoFile::getChildFile