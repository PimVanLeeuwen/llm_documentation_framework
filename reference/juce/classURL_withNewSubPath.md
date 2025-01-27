#### withNewSubPath()


 URL URL::withNewSubPath ( const String & newPath ) const nodiscard 
 

Returns a new version of this URL with a different subpath.e.g. if the URL is "http://www.xyz.com/foo?x=1" and you call this with "bar", it'll return "http://www.xyz.com/bar?x=1".See alsowithNewDomainAndPath