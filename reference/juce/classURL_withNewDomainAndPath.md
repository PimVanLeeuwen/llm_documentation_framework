#### withNewDomainAndPath()


 URL URL::withNewDomainAndPath ( const String & newFullPath ) const nodiscard 
 

Returns a new version of this URL with a different domain and path.e.g. if the URL is "http://www.xyz.com/foo?x=1" and you call this with "abc.com/zzz", it'll return "http://abc.com/zzz?x=1".See alsowithNewSubPath