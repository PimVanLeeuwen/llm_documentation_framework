#### getSubPath()


 String URL::getSubPath ( bool includeGetParameters = false ) const 
 

Returns the path part of the URL.e.g. for "http://www.xyz.com/foo/bar?x=1", this will return "foo/bar".Parameters

 includeGetParameters if this is true and any parameters have been set with the withParameter() method, then the string will have these appended on the end and URLencoded. 
 



See alsogetQueryString